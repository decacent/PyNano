#!/usr/bin/env python

# encoding: utf-8

'''

@author: decacent

@license: Copyright (C) 2017-2018 decacent. All rights reserved.

@contact: shaochuang_routine@outlook.com

@software: pycharm

@python version: python3.5, python3.6

@file: scat_analy.py

@time: 2017/5/14 18:27

@desc:

'''

import numpy as np
import pywt
import pywt._extensions._cwt
from time import strftime
from itertools import groupby, chain

from scipy.signal import butter, lfilter, freqz
import sklearn
from sklearn.cluster import  KMeans, DBSCAN
from itertools import groupby, chain
from scipy.signal import  medfilt
from scipy.signal import butter, lfilter, freqz
from sklearn.preprocessing import StandardScaler
from scipy.cluster.vq import kmeans, kmeans2


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
        coeffs[len(coeffs) - 1] *= 0
        coeffs[len(coeffs) - 2] *= 0
        # 重构
        meta = pywt.waverec(coeffs, db4)
        return meta


def dbscan_cluster(data, eps=0.2, min_sam=10):
    '''
    DBSCAN聚类算法
    '''
    X = StandardScaler().fit_transform(data)
    db = DBSCAN(eps=eps, min_samples=min_sam).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    return labels


def signal_cluster(data, fs=100000, cluster=2, kernel_size=51, th=5):
    '''
    K_means 聚类
    '''

    time_temp = []
    #    X = StandardScaler().fit_transform(i[:,:2])
    #    db = DBSCAN(eps=0.2, min_samples=10).fit(X)
    #    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    #    core_samples_mask[db.core_sample_indices_] = True
    #    labels = db.labels_
    # k= labels.max()+1 if labels.max()>0 else 1
    data[:, 1] = medfilt(data[:, 1], kernel_size)  # 中值滤波
    # centers,labels = kmeans2(i2,k=cluster)
    try:
        clf = KMeans(n_clusters=cluster).fit(data)
    except:
        return None
    labels = clf.labels_.copy()
    #       label_t=np.array(list(OrderedDict(zip(labels,[1]*len(labels))).keys()))
    centers = clf.cluster_centers_

    for t1 in range(cluster):
        time_temp.append(np.count_nonzero(labels == t1))

    res_temp = np.column_stack((centers, np.array(time_temp) * (1 / fs * 1000), np.arange(cluster)))
    res_temp = res_temp[res_temp[:, 1].argsort()]

    t3 = np.abs(res_temp[0:-1, 1] - res_temp[1:, 1]) < th
    while True in t3:
        t_index = np.where(t3)[0][0]
        res_temp[t_index, 1] = (res_temp[t_index, 1] + res_temp[t_index + 1, 1]) / 2
        labels[labels == res_temp[t_index + 1, 3]] = res_temp[t_index, 3]
        res_temp = np.delete(res_temp, t_index + 1, 0)
        t3 = np.abs(res_temp[0:-1, 1] - res_temp[1:, 1]) < th

    res_temp = res_temp[:, 1:3]
    #    nums = list(itertools.combinations(current_temp,2))
    #    index = list(itertools.combinations([x for x in range(cluster)],2))
    if 0 in res_temp:
        return None
    if res_temp.shape[0] < cluster:
        res_temp = np.row_stack((res_temp, np.zeros((cluster - res_temp.shape[0], 2))))

    res_temp = res_temp[np.lexsort(-res_temp[:, ::-1].T)].ravel()

    return res_temp, labels


def find_peaks(data):
    '''
    寻找数据䣌极值点，
    输入： 二维数据，第一列为时间，第二列为电流数据
    输出：二维数据，只包含极值点
    '''
    time = data[:, 0]
    current = data[:, 1]
    temp1 = np.logical_or(np.logical_and(current[0:-2] <= current[1:-1],
                                         current[1:-1] >= current[2:]),
                          np.logical_and(current[0:-2] >= current[1:-1],
                                         current[1:-1] <= current[2:]))
    peak_current = current[1:-1][temp1]
    peak_time = time[1:-1][temp1]
    return np.array((peak_time, peak_current)).T

def markov(data, ss, stage_index=0):
    """
    计算马尔科夫链转移概率
    input：data：signal_extract 输出数据，二维数据，电流时间
           ss: 台阶分类的参照，元素为Tuple的列表。
    output：
        t2:转移数count
        t3:转移概率
        t4: 时间电流的分类数据,字典
        t3.ravel(): 展平的一维转移概率

    """
    if stage_index == 4:
        stage_index = 2

    ss.sort(reverse=1)
    level = len(ss) - 1
    data = data[1:-1, :]
    #    current = np.copy(data[1:-1,0])
    #    time=np.copy(data[1:-1,1])
    #    normI

    t1 = np.zeros(len(data), dtype='int')

    t4 = {}

    for index, value in enumerate(ss[0:-1]):
        temp = np.logical_and(
            data[:, stage_index] < ss[index], data[:, stage_index] >= ss[index + 1])
        t1[temp] = index
        t4['stage{0}'.format(index + 1)] = data[temp]

    t2 = np.zeros((level, level), dtype=int)

    for i, j in enumerate(t1[0:-1]):
        t2[t1[i], t1[i + 1]] += 1

    t3 = t2 / np.sum(t2, axis=1)[:, None]
    t5 = []
    for i in range(level):
        for j in range(level):
            t5.append(10 * (i + 1) + j + 1)
    t5 = np.array(t5)
    t4['count'] = t2
    t4['probability'] = t3
    t4['revel_prob'] = np.array((t5, t3.ravel())).T

    return t4


def signal_extract(data, th=100, sam=100000,filter=3000,is_filter=False):
    """
    拟合多台阶电流数据，适用于长时间单分子捕获
    数据输入：data：原始数据，单行或单列电流信号
             th, 最小电流台阶阈值,小于该值将合并为一个台阶
             sam, 数据采样率，默认为100K
             is_resam: 是否进行数据冲采样，适用于250K采样，信号分析结构较差时使用。
                         使用重采样必须设置数据范围。
            resam：重采样的采样率
    数据输出：1：data1，散点数据，包含电流台阶和对应的时间，I/I0
             2：data2，重构的拟合曲线
    """
    current = np.array(data).reshape(-1, )
    current = wavelet_denoising(data)
    if is_filter:
        current = butter_lowpass_filter(current, filter, 100000, 5) # 低通滤波

    time = np.arange(len(current))
    #    print('寻找极值点 1')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))
    temp1 = np.logical_or(np.logical_and(current[0:-2] <= current[1:-1],
                                         current[1:-1] >= current[2:]),
                          np.logical_and(current[0:-2] >= current[1:-1],
                                         current[1:-1] <= current[2:]))
    peak_current = current[1:-1][temp1]
    peak_time = time[1:-1][temp1]
    #    print('寻找极值点 2')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))

    temp2 = np.logical_or(np.abs(peak_current[1:-
    1] -
                                 peak_current[0:-
                                 2]) >= th, np.abs(peak_current[1:-
    1] -
                                                   peak_current[2:]) >= th)
    re_peak_time = peak_time[1:-1][temp2]
    re_peak_current = peak_current[1:-1][temp2]

    #    print('合并台阶')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))

    tq = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) < th
    while True in tq:
        tq = np.insert(tq, -1, 0)
        re_peak_time = re_peak_time[~tq]
        re_peak_current = re_peak_current[~tq]
        tq = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) < th
    # 我也不知道当初写这个是干嘛的啦    

    #    tq = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) > th
    #    while False in tq:
    #        re_peak_time = re_peak_time[0:-1][tq]
    #        re_peak_current = re_peak_current[0:-1][tq]
    #        tq = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) > th

    t1 = np.arange(len(peak_time))[np.in1d(peak_time, re_peak_time)]
    t1 += 1
    t2 = np.insert(t1[0:-1], 0, 0)

    def foo(x, y):
        nonlocal peak_current
        return np.mean(peak_current[x:y])
        
    re_peak_current = np.array(list(map(foo, t2, t1)))
    t3 = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) < th

    while True in t3:
        for i in np.where(t3)[0]:
            re_peak_current[i + 1] = (re_peak_current[i] * (t1[i] - t2[i]) + re_peak_current[i + 1] * (
                    t1[i + 1] - t2[i + 1])) / ((t1[i] - t2[i]) + (t1[i + 1] - t2[i + 1]))
        t3 = np.insert(t3, -1, 0)
        re_peak_current = re_peak_current[~t3]
        re_peak_time = re_peak_time[~t3]
        t3 = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) < th

    #    print('重构拟合曲线 1')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))
    re_current = np.zeros(len(current))
    j = 0
    for i, v in enumerate(re_peak_time):
        re_current[j:v + 1] = re_peak_current[i]
        j = v + 1
    re_current[re_peak_time[-2] + 1:] = np.mean(current[re_peak_time[-1] + 1:])

    re_peak_current[-1] = np.mean(current[re_peak_time[-1] + 1:])
    re_peak_time = np.insert(re_peak_time, 0, 0)
    scat_time = (re_peak_time[1:] - re_peak_time[0:-1]) * 1000 / sam
    norm_re_peakcurrent = re_peak_current / re_peak_current[0]
    data1 = np.array((re_peak_current, scat_time, norm_re_peakcurrent))

    #    print('数据分析完成')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))

    return data1.T, re_current


def signal_extract2(
        init_time,
        data,
        peak_th,
        base,
        th=100,
        sam=100000,
        filter=3000,
        is_filter=False,
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

    current = np.array(data)
    current = wavelet_denoising(data)
    time = np.arange(len(current))
    if is_filter:
        current = butter_lowpass_filter(current, filter, 100000, 5) # 低通滤波

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

    result = [[], [], [], [], [], [], []]
    start_point, end_point = 0, 0
    data1 = current
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
            temp_time = (end_point - start_point) / sam
            # value=np.mean(peak_current[t1[t3[index]-1]:t1[j]])
            #        if len(temp4)>10:
            #            value=np.mean(temp4)
            #        else:
            #            value=np.max(temp4)
            temp4 = np.array(temp4)

            # k_temp = abs(temp4[0:-1] - temp4[1:]) > th
            # k_num = np.count_nonzero(k_temp)
            #
            # if k_num > 0:
            #     t4 = []
            #     j = 0
            #     for i in np.argwhere(k_temp == 1).reshape(-1):
            #         t4.append(np.mean(temp4[j:i + 1]))
            #         j = i + 1
            #         t4.append(np.mean(temp4[j:]))
            #     value1 = np.mean(t4)
            # #
            # #
            # #                #            k1 = np.arange(len(temp4),dtype='f')
            # #                #            k2=np.array((k1,temp4)).T
            # #                #            res, idx = kmeans2(k2,k_num+1)
            # #                #            value = max(res[:,1])
            # else:
            #     value1 = np.mean(temp4)
            value1 = np.mean(temp4)
            data1[start_point - 30:start_point + 1] = temp_base
            data1[start_point + 1: end_point] = value1
            charge = np.trapz(current[start_point:end_point], dx=1 / sam)
            charge = charge - temp_base * temp_time
            result[0].append(value1)  # 电流
            result[1].append(temp_time * 1000)  # 时间
            result[2].append(value1 / temp_base)  # I/I0
            result[3].append(temp_base)  # 基线
            result[4].append(value1 - temp_base)  # Delta I
            result[5].append(charge)  # 积分电荷
            result[6].append(start_point / sam * 1000 + init_time)  # 信号起始时间

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
            temp_time = (end_point - start_point) / sam
            # value=np.mean(peak_current[t1[t3[index]-1]:t1[j]])
            #        if len(temp4)>10:
            #            value=np.mean(temp4)
            #        else:
            #            value=np.max(temp4)
            temp4 = np.array(temp4)

            # k_temp = abs(temp4[0:-1] - temp4[1:]) > th
            # k_num = np.count_nonzero(k_temp)

            # if k_num > 0:
            #     t4 = []
            #     j = 0
            #     for i in np.argwhere(k_temp == 1).reshape(-1):
            #         t4.append(np.mean(temp4[j:i + 1]))
            #         j = i + 1
            #     t4.append(np.mean(temp4[j:]))
            #     value1 = np.mean(t4)
            #
            #
            #     #            k1 = np.arange(len(temp4),dtype='f')
            #     #            k2=np.array((k1,temp4)).T
            #     #            res, idx = kmeans2(k2,k_num+1)
            #     #            value = max(res[:,1])
            # else:
            #     value1 = np.mean(temp4)
            value1 = np.mean(temp4)
            data1[start_point - 30:start_point + 1] = temp_base
            data1[start_point + 1: end_point] = value1
            charge = np.trapz(current[start_point:end_point], dx=1 / sam)
            charge = temp_base * temp_time - charge
            result[0].append(value1)  # 电流
            result[1].append(temp_time * 1000)  # 时间
            result[2].append(value1 / temp_base)  # I/I0
            result[3].append(temp_base)  # 基线
            result[4].append(temp_base - value1)  # Delta I
            result[5].append(charge)  # 积分电荷
            result[6].append(start_point / sam * 1000 + init_time)  # 信号起始时间

    result = np.array(result).T
    return result, data1

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def wavelet_denoising(data):
    # 小波函数取db4
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
    
def signal_extract3(
        init_time,
        data,
        peak_th,
        base,
        th=100,
        sam=100000,
        filter=3000,
        is_filter=False,
        is_up=False):
    """
    拟合多峰nanopore电流数据，
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

    current = np.array(data)
    current = wavelet_denoising(data)
    if is_filter:
        current = butter_lowpass_filter(current, filter, 100000, 5) # 低通滤波

    time = np.arange(len(current))
    print('寻找极值点 1')
    print(strftime("%m/%d/%Y %H:%M:%S"))
    # 获取信号的极值点
    temp1 = np.logical_or(np.logical_and(current[0:-2] <= current[1:-1],
                                         current[1:-1] >= current[2:]),
                          np.logical_and(current[0:-2] >= current[1:-1],
                                         current[1:-1] <= current[2:]))
    peak_current = current[1:-1][temp1]
    peak_time = time[1:-1][temp1]
    print('寻找极值点 2')
    print(strftime("%m/%d/%Y %H:%M:%S"))
    # 筛选极值点，获取差值大于噪音的点。
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

    # 获取极值点2 在极值点1 中的位置
    t1 = np.arange(len(peak_time))[np.in1d(peak_time, re_peak_time)]

    # 筛选属于信号的极值点
    if is_up:
        temp3 = re_peak_current > peak_th  # 信号阈值
    else:
        temp3 = re_peak_current < peak_th

    signal_peak_time = re_peak_time[temp3]
    signal_peak_current = re_peak_current[temp3]
    t3 = np.arange(len(re_peak_time))[np.in1d(re_peak_time, signal_peak_time)]

    result = [[], [], [], [], [], [], []]
    start_point, end_point = 0, 0
    data1 = current
    if is_up:
        for index, value in enumerate(signal_peak_current):
            if start_point < signal_peak_time[index] < end_point:
                continue

            k = t1[t3[index]] - 1
            ks = 1
            while abs(peak_current[k] - base) > th / \
                    3 and peak_current[k] > base:
                ks += 1
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

            # value=np.mean(peak_current[t1[t3[index]-1]:t1[j]])
            #        if len(temp4)>10:
            #            value=np.mean(temp4)
            #        else:
            #            value=np.max(temp4)

            data1[start_point - 30:start_point + 1] = temp_base
            temp4 = np.array(temp4)

            k_temp = abs(temp4[0:-1] - temp4[1:]) > th
            k_num = np.count_nonzero(k_temp)
            t4 = []
            t5 = []
            s_1 = k + ks  # 开始寻找多峰
            if k_num > 0:

                j = 0

                for i in np.argwhere(k_temp == 1).reshape(-1):
                    t_state = np.mean(temp4[j:i + 1])
                    t4.append(t_state)
                    s_start = peak_time[s_1 + j]
                    s_end = peak_time[s_1 + i + 1]
                    t5.append((s_end - s_start) / sam * 1000)
                    data1[s_start:end_point] = t_state
                    j = i + 1
                data1[start_point + 1:peak_time[k + ks]] = t4[0]
                t5[0] = t5[0] + (peak_time[k + ks] - start_point) / sam * 1000
                t4.append(np.mean(temp4[j:]))
                s_start = peak_time[s_1 + j]
                t5.append((end_point - s_start) / sam * 1000)
                data1[s_start:end_point] = np.mean(temp4[j:])
                value1 = np.array(t4)
                temp_time = t5

                charge = np.trapz(current[start_point:end_point], dx=1 / sam)
                charge = charge - temp_base * (end_point - start_point) / sam

                result[0].append(t4)  # 电流
                result[1].append(t5)  # 时间
                result[2].append(list((value1 / temp_base)))  # I/I0
                result[3].append([temp_base] * len(t4))
                result[4].append(list((value1 - temp_base)))  # Delta I
                result[5].append([charge] * len(t4))
                result[6].append([start_point / sam * 1000 +
                                  init_time] * len(t4))  # 信号起始时间

            #
            #
            #                #            k1 = np.arange(len(temp4),dtype='f')
            #                #            k2=np.array((k1,temp4)).T
            #                #            res, idx = kmeans2(k2,k_num+1)
            #                #            value = max(res[:,1])
            else:
                # value1 = np.mean(temp4)
                # temp_time = (end_point - start_point) / sam*1000
                t4.append(np.mean(temp4))
                data1[start_point + 1: end_point] = np.mean(temp4)
                t5.append((end_point - start_point) / sam * 1000)
                # value1=list(value1)
                # temp_time=list(temp_time)

                charge = np.trapz(current[start_point:end_point], dx=1 / sam)
                charge = charge - temp_base * (end_point - start_point) / sam

                result[0].append(t4)  # 电流
                result[1].append(t5)  # 时间
                result[2].append([t4[0] / temp_base])  # I/I0
                result[3].append([temp_base])
                result[4].append([t4[0] - temp_base])
                result[5].append([charge])
                result[6].append([start_point / sam * 1000 + init_time])

    else:
        for index, value in enumerate(signal_peak_current):
            if start_point < signal_peak_time[index] < end_point:
                continue

            k = t1[t3[index]] - 1
            ks = 0
            while abs(peak_current[k] - base) > th / \
                    3 and peak_current[k] < base:
                ks += 1
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
            # value=np.mean(peak_current[t1[t3[index]-1]:t1[j]])
            #        if len(temp4)>10:
            #            value=np.mean(temp4)
            #        else:
            #            value=np.max(temp4)
            data1[start_point - 30:start_point + 1] = temp_base
            temp4 = np.array(temp4)

            k_temp = abs(temp4[0:-1] - temp4[1:]) > th
            k_num = np.count_nonzero(k_temp)
            t4 = []
            t5 = []

            s_1 = k + ks  # 开始寻找多峰
            if k_num > 0:

                j = 0
                for i in np.argwhere(k_temp == 1).reshape(-1):
                    t_state = np.mean(temp4[j:i + 1])
                    t4.append(t_state)
                    s_start = peak_time[s_1 + j]
                    s_end = peak_time[s_1 + i + 1]
                    t5.append((s_end - s_start) / sam * 1000)
                    data1[s_start:end_point] = t_state
                    j = i + 1

                t5[0] = t5[0] + (peak_time[k + ks] - start_point) / sam * 1000
                data1[start_point:peak_time[k + ks]] = t4[0]
                t4.append(np.mean(temp4[j:]))
                s_start = peak_time[s_1 + j]
                t5.append((end_point - s_start) / sam * 1000)
                data1[s_start:end_point] = np.mean(temp4[j:])
                value1 = t4
                # temp_time = t5

                charge = np.trapz(current[start_point:end_point], dx=1 / sam)
                charge = temp_base * (end_point - start_point) / sam - charge

                result[0].append(t4)  # 电流
                result[1].append(t5)  # 时间
                result[2].append(list((value1 / temp_base)))  # I/I0
                result[3].append([temp_base] * len(t4))
                result[4].append(list((value1 - temp_base)))  # Delta I
                result[5].append([charge] * len(t4))
                result[6].append([start_point / sam * 1000 +
                                  init_time] * len(t4))  # 信号起始时间

                #            k1 = np.arange(len(temp4),dtype='f')
                #            k2=np.array((k1,temp4)).T
                #            res, idx = kmeans2(k2,k_num+1)
                #            value = max(res[:,1])
            else:
                t4.append(np.mean(temp4))
                data1[start_point + 1: end_point] = np.mean(temp4)
                t5.append((end_point - start_point) / sam * 1000)

                charge = np.trapz(current[start_point:end_point], dx=1 / sam)
                charge = temp_base * (end_point - start_point) / sam - charge

                result[0].append(t4)  # 电流
                result[1].append(t5)  # 时间
                result[2].append([t4[0] / temp_base])  # I/I0
                result[3].append([temp_base])
                result[4].append([t4[0] - temp_base])
                result[5].append([charge])
                result[6].append([start_point / sam * 1000 + init_time])

    index = [[i] * len(j) for i, j in zip(range(len(result[0])), result[0])]
    res = []
    for i in range(7):
        res.append(list(chain.from_iterable(result[i])))
    res.append(list(chain.from_iterable(index)))
    res = np.array(res).T
    return res, data1


def block_per(a, le, is_single=True, is_up=False):
    """
    基于signal_extract的散点数据提取
    输入：a: signal_extract 的输出数据1,
          le: 基线阈值
          is_single: 是否合并为单峰信号
          is_up: 是否为增强信号
    """

    a = a.T

    def level(x):
        nonlocal le
        x = x[0]
        if x > le:
            return 0
        else:
            return 1

    def level2(x):
        nonlocal le
        x = x[0]
        if x < le:
            return 0
        else:
            return 1

    k = []
    j = []

    for m, n in groupby(a, key=level if is_up is False else level2):
        j.append(m)
        k.append(np.array(list(n)))

    res = []
    res_1 = np.zeros(np.count_nonzero(j))
    res_2 = np.zeros(np.count_nonzero(j))
    count = 0
    for index, value in enumerate(j):
        if value == 1:
            res.append(k[index])
            res_1[count] = k[index - 1][-1, 0]  # 基线
            res_2[count] = sum(k[index - 1][:, 1])
            count += 1

    if is_single is True:
        for index, value in enumerate(res):
            if len(value) > 1:
                res[index] = np.array((sum(value[:, 0] * value[:, 1]) / sum(value[:, 1]),
                                       sum(value[:, 1]))).reshape(1, -1)
        res = np.array(res)[:, 0, :]

        res_3 = np.zeros(len(res_2))
        res_3[0] = res_2[0]
        res_2 = res_2[1:]
        for index, value in enumerate(res_2):
            res_3[index + 1] = res_3[index] + res[index][1] + value

        data = np.column_stack(
            (res, res_1, res[:, 0] / res_1, np.abs(res[:, 0] - res_1), res_3))
        # 返回数据：电流，时间，基线，I/I0，delta I, 起始时间
        return data
    else:
        res = list(chain.from_iterable(res))
        return np.array(res).T


def rms(x):
    """
    计算数据的均方根偏差
    """
    y = np.sqrt(np.mean(np.power(x, 2)))
    return y


def collision_analy(
        data,
        th,
        sam,
        peak_th,
        end_th=2,
        base_num=500,
        end_num=50,
        is_up=False):
    # warnings.simplefilter("error")
    """
    碰撞电极信号处理

    输入：data：原始数据
    th:极值判断阈值，默认为基线的噪音宽度
    sam:数据采样率
    end_th: 判断信号结束位置参数，当信信号与基线值相差小于该值时，判断为信号结束。
    peak_th: 信号判断参数，大于该阈值认为是信号。
    base_num: 使用多少个点来判断基线
    end_num：使用多少个点判断信号回到基线

    输出：
        1：data1，散点数据，包含电流台阶和对应的时间，I/I0，基线，
                        Delta I, 积分电荷
        2：data2，重构的拟合曲线
    """

    data = np.array(data).reshape(-1, ).astype('f8')
    data1 = data
    time = np.arange(len(data))
    #    print('寻找极值点 1')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))
    temp1 = np.logical_or(np.logical_and(data[0:-2] <= data[1:-1],
                                         data[1:-1] >= data[2:]),
                          np.logical_and(data[0:-2] >= data[1:-1],
                                         data[1:-1] <= data[2:]))
    peak_current = data[1:-1][temp1]
    peak_time = time[1:-1][temp1]
    #    print('寻找极值点 2')
    #    print(strftime("%m/%d/%Y %H:%M:%S"))

    temp2 = np.logical_or(np.abs(peak_current[1:-
    1] -
                                 peak_current[0:-
                                 2]) >= th, np.abs(peak_current[1:-
    1] -
                                                   peak_current[2:]) >= th)
    re_peak_time = peak_time[1:-1][temp2]
    re_peak_current = peak_current[1:-1][temp2]

    tq = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) < th
    while True in tq:
        tq = np.insert(tq, -1, 0)
        re_peak_time = re_peak_time[~tq]
        re_peak_current = re_peak_current[~tq]
        tq = np.abs(re_peak_current[0:-1] - re_peak_current[1:]) < th
    if is_up:
        temp3 = re_peak_current > peak_th
    else:
        temp3 = re_peak_current < peak_th  # 信号阈值
    signal_peak_time = re_peak_time[temp3]
    signal_peak_current = re_peak_current[temp3]
    t1 = np.arange(len(re_peak_time))[np.in1d(re_peak_time, signal_peak_time)]
    result = [[], [], [], [], [], []]
    temp4, temp5 = 0, 0
    if not is_up:
        for index, value in enumerate(signal_peak_current):
            j = signal_peak_time[index]
            if temp4 < j < temp5:
                continue
            temp_base = np.mean(
                data[re_peak_time[t1[index] - 1] - base_num:re_peak_time[t1[index] - 1]])
            start_point = re_peak_time[t1[index] - 1] - base_num
            j = signal_peak_time[index]
            #        while np.mean(data[j:j+end_num])-temp_base >end_th :
            #            j += end_num
            temp6 = True
            temp7 = True
            while temp6:
                try:
                    temp6 = abs(np.mean(data[j:j + end_num]) - temp_base) > end_th and np.mean(
                        data[j:j + end_num]) < temp_base
                    if temp6:
                        j += end_num
                except BaseException:
                    temp7 = False
                    break
            if not temp7:
                continue
            end_point = j + end_num - 1
            temp4 = start_point
            temp5 = end_point
            temp_time = (end_point - re_peak_time[t1[index] - 1]) / sam
            value = np.min(data[re_peak_time[t1[index] - 1]: end_point])
            if value > temp_base:
                continue

            data1[start_point:re_peak_time[t1[index] - 1]] = temp_base
            data1[re_peak_time[t1[index] - 1]: end_point] = value
            charge = np.trapz(
                data[re_peak_time[t1[index] - 1]:end_point], dx=1 / sam)
            charge = temp_base * temp_time - charge
            result[0].append(value)  # 电流
            result[1].append(temp_time * 1000)  # 时间
            result[2].append(value / temp_base)  # I/I0
            result[3].append(temp_base)  # 基线
            result[4].append(temp_base - value)  # Delta I
            result[5].append(charge)  # 积分电荷
    else:
        for index, value in enumerate(signal_peak_current):
            j = signal_peak_time[index]
            if temp4 < j < temp5:
                continue
            temp_base = np.mean(
                data[re_peak_time[t1[index] - 1] - base_num:re_peak_time[t1[index] - 1]])
            start_point = re_peak_time[t1[index] - 1] - base_num
            j = signal_peak_time[index]
            #        while np.mean(data[j:j+end_num])-temp_base >end_th :
            #            j += end_num
            temp6 = True
            temp7 = True
            while temp6:
                try:
                    temp6 = abs(np.mean(data[j:j + end_num]) - temp_base) > end_th and np.mean(
                        data[j:j + end_num]) > temp_base
                    if temp6:
                        j += end_num
                except BaseException:
                    temp7 = False
                    break
            if not temp7:
                continue
            end_point = j + end_num - 1
            temp4 = start_point
            temp5 = end_point
            temp_time = (end_point - re_peak_time[t1[index] - 1]) / sam
            value = np.max(data[re_peak_time[t1[index] - 1]: end_point])
            if value < temp_base:
                continue

            data1[start_point:re_peak_time[t1[index] - 1]] = temp_base
            data1[re_peak_time[t1[index] - 1]: end_point] = value
            charge = np.trapz(
                data[re_peak_time[t1[index] - 1]:end_point], dx=1 / sam)
            charge = charge - temp_base * temp_time
            result[0].append(value)  # 电流
            result[1].append(temp_time * 1000)  # 时间
            result[2].append(value / temp_base)  # I/I0
            result[3].append(temp_base)  # 基线
            result[4].append(value - temp_base)  # Delta I
            result[5].append(charge)  # 积分电荷
    result = np.array(result).T
    return result, data1


def signal_extract_cluster(init_time,
        data,
        peak_th,
        base,
        th=100,
        sam=100000,
        n_cluster=2,
        kernel_size=51,
        is_up=False):
    """
    聚类分析多台阶数据，
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
    current = wavelet_denoising(data)

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
    data_temp = []
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

            data_s = np.array((time[start_point:end_point] / sam,
                               current[start_point:end_point])).T
            res_temp = signal_cluster(data=data_s, fs=sam, cluster=n_cluster, kernel_size=kernel_size, th= th / 2)

            if res_temp is None:
                continue
            else:
                res, labels = res_temp[0], res_temp[1]

            res = np.insert(res, 0, start_point / sam * 1000 + init_time)
            res = np.insert(res, 0, temp_base)
            result.append(res)
            data1[start_point - 30:start_point + 1] = temp_base
            for ix in range(n_cluster):
                data1[start_point:end_point][labels == ix] = \
                    np.mean(data1[start_point:end_point][labels == ix])

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

            data_s = np.array((time[start_point:end_point] / sam,
                               current[start_point:end_point])).T
            res_temp = signal_cluster(data=data_s, fs=sam, cluster=n_cluster, kernel_size=kernel_size, th=th / 2)

            if res_temp is None:
                continue
            else:
                res, labels = res_temp[0], res_temp[1]
                data_temp.append(np.array((time[start_point:end_point] / 100000,
                                           current[start_point:end_point],
                                           labels)).T)
            res = np.insert(res, 0, start_point / sam * 1000 + init_time)
            res = np.insert(res, 0, temp_base)
            result.append(res)
            data1[start_point - 30:start_point + 1] = temp_base
            for ix in range(n_cluster):
                data1[start_point:end_point][labels == ix] = \
                    np.mean(data1[start_point:end_point][labels == ix])

    result = np.array(result)
    return result, data1, data_temp


