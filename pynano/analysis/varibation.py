# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:05:06 2018

@author: wnight
"""

import numpy as np
from time import strftime
from scipy.signal import resample
from itertools import groupby, chain


def signal_extract(data, th=100, sam=100000, is_resam=False, re_sam=100000):
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
	if is_resam and sam > re_sam:
		#        print('信号重采样1')
		#        print(strftime("%m/%d/%Y %H:%M:%S"))
		current = resample(current, int(len(current) / (sam / re_sam)))
		#        print('信号重采样2')
		#        print(strftime("%m/%d/%Y %H:%M:%S"))
		current = resample(current, int(len(current) * (sam / re_sam)))
	# print('信号重采样完成')
	#        print(strftime("%m/%d/%Y %H:%M:%S"))
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
