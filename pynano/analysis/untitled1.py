# -*- coding: utf-8 -*-
"""
Created on Sat May 12 10:57:11 2018

@author: wnight
"""

import numpy as np
import pywt
from time import strftime
from scipy.signal import resample
from itertools import groupby, chain

from scipy.signal import butter, lfilter, freqz

import numpy as np
import pywt
from sklearn.cluster import  KMeans
from itertools import groupby, chain
from scipy.signal import  medfilt
from scipy.signal import butter, lfilter, freqz
from sklearn.cluster import DBSCAN  
from sklearn import metrics  
from sklearn.datasets.samples_generator import make_blobs  
from sklearn.preprocessing import StandardScaler
#from scipy.cluster.vq import kmeans, kmeans2
from axonio import  Abf_io
from PyQt5.Qt import  QFileDialog
from collections import OrderedDict

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    '''
    低通滤波函数，用于数据降噪
    '''
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def wavelet_denoising(data):
    '''
    小波降噪
    '''
    
    db4 = pywt.Wavelet('db8')
    if data is not None:
        # 分解
        coeffs = pywt.wavedec(data, db4)
        # 高频系数置零
        coeffs[len(coeffs)-1] *= 0
        coeffs[len(coeffs)-2] *= 0
        # 重构
        meta = pywt.waverec(coeffs, db4)
        return meta


def dbscan_cluster(data,eps=0.2,min_sam=10):
    '''
    DBSCAN聚类算法
    '''
    X = StandardScaler().fit_transform(data)
    db = DBSCAN(eps=eps, min_samples=min_sam).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    
    return labels

def signal_cluster(data,fs=100000,cluster=2,kernel_size=51,th=5):
    '''
    K_means 聚类
    '''
    
    time_temp=[]
    #    X = StandardScaler().fit_transform(i[:,:2])
    #    db = DBSCAN(eps=0.2, min_samples=10).fit(X)
    #    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    #    core_samples_mask[db.core_sample_indices_] = True
    #    labels = db.labels_
        #k= labels.max()+1 if labels.max()>0 else 1
    data[:,1]=medfilt(data[:,1],kernel_size) # 中值滤波
        #centers,labels = kmeans2(i2,k=cluster)
    try:
        clf = KMeans(n_clusters=cluster).fit(data)
    except:
        return None
    labels=clf.labels_.copy() 
#       label_t=np.array(list(OrderedDict(zip(labels,[1]*len(labels))).keys()))
    centers=clf.cluster_centers_
        
    for t1 in range(cluster):
        time_temp.append(np.count_nonzero(labels==t1))
            
    res_temp=np.column_stack((centers,np.array(time_temp)*(1/fs*1000),np.arange(cluster)))
    res_temp=res_temp[res_temp[:,1].argsort()]
        
    t3 = np.abs(res_temp[0:-1,1]-res_temp[1:,1]) < th
    while True in t3:
        t_index=np.where(t3)[0][0]
        res_temp[t_index,1]=(res_temp[t_index,1]+res_temp[t_index+1,1])/2
        labels[labels==res_temp[t_index+1,3]]=res_temp[t_index,3]
        res_temp=np.delete(res_temp,t_index+1,0)
        t3=np.abs(res_temp[0:-1,1]-res_temp[1:,1]) < th

    res_temp=res_temp[:,1:3]        
    #    nums = list(itertools.combinations(current_temp,2))
    #    index = list(itertools.combinations([x for x in range(cluster)],2))
    if 0 in res_temp:
        return None
    if res_temp.shape[0] < cluster:
        res_temp=np.row_stack((res_temp,np.zeros((cluster-res_temp.shape[0],2))))
    
    res_temp=res_temp[np.lexsort(-res_temp[:,::-1].T)].ravel()

    return res_temp,labels

def find_peaks(data):
    '''
    寻找数据䣌极值点，
    输入： 二维数据，第一列为时间，第二列为电流数据
    输出：二维数据，只包含极值点
    '''
    time=data[:,0] 
    current=data[:,1]
    temp1 = np.logical_or(np.logical_and(current[0:-2] <= current[1:-1],
                                         current[1:-1] >= current[2:]),
                          np.logical_and(current[0:-2] >= current[1:-1],
                                         current[1:-1] <= current[2:]))
    peak_current = current[1:-1][temp1]
    peak_time = time[1:-1][temp1]
    return np.array((peak_time,peak_current)).T

def signal_extract_cluster(
        init_time,
        data,
        peak_th,
        base,
        th=100,
        sam=100000,
        n_cluster=2,
        kernel_size=51,
        is_up=False):
    """
    拟合单峰电流数据，
    数据输入：data：原始数据，单行或单列电流信号
             peak_th: 信号阈值
             th, 基线噪音值，最小电流台阶阈值,小于该值将合并为一个台阶，
             sam, 数据采样率，默认为100K
             is_resam: 是否进行数据冲采样，适用于250K采样，信号分析结构较差时使用。
                         使用重采样必须设置数据范围。
             is_up: 是否为增强信号


    数据输出：1：data1，散点数据，包含电流台阶和对应的时间，I/I0，基线，
                        Delta I, 积分电荷，信号起始时间
             2：data2，重构的拟合曲线
    """
    current=wavelet_denoising(data)



    time = np.arange(len(current))
    print('寻找极值点 1')
    print(strftime("%m/%d/%Y %H:%M:%S"))
    temp1 = np.logical_or(np.logical_and(current[0:-2] <= current[1:-1],
                                         current[1:-1] >= current[2:]),
                          np.logical_and(current[0:-2] >= current[1:-1],
                                         current[1:-1] <= current[2:]))
    peak_current = current[1:-1][temp1]
    peak_time = time[1:-1][temp1]
    print('寻找极值点 2')
    print(strftime("%m/%d/%Y %H:%M:%S"))

    temp2 = np.logical_or(np.abs(peak_current[1:-
    1] -
                                 peak_current[0:-
                                 2]) >= th, np.abs(peak_current[1:-
    1] -
                                                   peak_current[2:]) >= th)
    re_peak_time = peak_time[1:-1][temp2]
    re_peak_current = peak_current[1:-1][temp2]

    print('合并台阶')
    print(strftime("%m/%d/%Y %H:%M:%S"))

    t1 = np.arange(len(peak_time))[np.in1d(peak_time, re_peak_time)]
    if is_up:
        temp3 = re_peak_current > peak_th  # 信号阈值
    else:
        temp3 = re_peak_current < peak_th
    signal_peak_time = re_peak_time[temp3]
    signal_peak_current = re_peak_current[temp3]
    t3 = np.arange(len(re_peak_time))[np.in1d(re_peak_time, signal_peak_time)]

    result = []
    start_point, end_point = 0, 0
    data1 = current
    data_temp=[]
    if is_up:
        for index, value in enumerate(signal_peak_current):
            if start_point < signal_peak_time[index] < end_point:
                continue

            k = t1[t3[index]] - 1
            while abs(peak_current[k] - base) > th / \
                    3 and peak_current[k] > base:
                k -= 1
            start_point = peak_time[k]
            temp_base = np.mean(peak_current[k - 5:k])
            temp4 = []
            temp4.append(value)
            j = t1[t3[index]]
            while j < len(peak_time):
                if peak_current[j] > peak_th:
                    temp4.append(peak_current[j])
                    j += 1
                elif peak_current[j] < peak_th and abs(peak_current[j] - temp_base) > th / 3 and peak_current[
                    j] > temp_base:
                    j += 1
                else:
                    break
            else:
                j = -1

            end_point = peak_time[j]
            
            data_s=np.array((time[start_point:end_point]/sam,
                             current[start_point:end_point])).T
            res_temp=signal_cluster(data=data_s,fs=sam,cluster=n_cluster,kernel_size=51,th=th/2)
            
            if res_temp is None:
                continue
            else:
                res,labels=res_temp[0],res_temp[1]
                
            res=np.insert(res,0,temp_base)
            result.append(res)
            data1[start_point - 30:start_point + 1] = temp_base
            for ix in range(n_cluster):
               data1[start_point:end_point][labels==ix]= \
                   np.mean(data1[start_point:end_point][labels==ix])
                            
    else:
        for index, value in enumerate(signal_peak_current):
            if start_point < signal_peak_time[index] < end_point:
                continue

            k = t1[t3[index]] - 1
            while abs(peak_current[k] - base) > th / \
                    3 and peak_current[k] < base:
                k -= 1
            start_point = peak_time[k]
            temp_base = np.mean(peak_current[k - 5:k])
            temp4 = []
            temp4.append(value)
            j = t1[t3[index]]
            while j < len(peak_time):
                if peak_current[j] < peak_th:
                    temp4.append(peak_current[j])
                    j += 1
                elif peak_current[j] > peak_th and abs(peak_current[j] - temp_base) > th / 3 and peak_current[
                    j] < temp_base:
                    j += 1
                else:
                    break
            else:
                j = -1

            end_point = peak_time[j]
    #        temp_time = (end_point - start_point) / sam
            
            data_s=np.array((time[start_point:end_point]/sam,
                             current[start_point:end_point])).T
            res_temp=signal_cluster(data=data_ s,fs=sam,cluster=2,kernel_size=51,th=th/2)
            
            if res_temp is None:
                continue
            else:
                res,labels=res_temp[0],res_temp[1]
                data_temp.append(np.array((time[start_point:end_point]/100000,
                                           current[start_point:end_point],
                                           labels)).T)
                
            res=np.insert(res,0,temp_base)
            result.append(res)
            data1[start_point - 30:start_point + 1] = temp_base
            for ix in range(n_cluster):
               data1[start_point:end_point][labels==ix]= \
                   np.mean(data1[start_point:end_point][labels==ix])
                            
    result = np.array(result)
    return result, data1,data_temp


if __name__ == '__main__':
    f=QFileDialog.getOpenFileName()[0]
    a=Abf_io(f)
    data=a.read_abf()[0]
    data=data[0]
    data=data[:,0]
    
    a,*b=signal_extract_cluster(init_time= 0,data=data,peak_th=32,base=45,th=10,sam=100000,n_cluster=2,kernel_size=101)
    