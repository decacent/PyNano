import numpy as np
import matplotlib.pyplot as plt
from Clusters import k_means_cluster


def fitting_data(data, baseline, rms):
    # copy the current data to do the fittness
    modified_c = data.copy()
    sample_num = np.shape(data)[0]
    shrehold = 3 * rms  # set the shrehold which is usually used as 3 xita
    for i in range(sample_num):
        if abs(modified_c[i] - baseline) <= shrehold:
            modified_c[i] = baseline
    # point out the signal segment
    i = 0
    while(i < sample_num):
        if abs(modified_c[i] - baseline) > 0.00000001:
            signal_start = i
            while(abs(modified_c[i] - baseline) > 0.00000001):
                i += 1
            signal_end = i
        else:
            i += 1
    # subsititute the signal segment with mean value of it
    modified_c[signal_start:signal_end +
               1] = modified_c[signal_start:signal_end + 1].mean()
    return modified_c


def annalysis(dataset, shrehold=35):
    sample_num = np.shape(dataset)[0]
    data = dataset.copy()
    extreme_points = []
    # find out the etreme points
    for i in range(sample_num - 2):
        if data[i + 1] > data[i] and data[i + 1] > data[i + 2]:
            extreme_points.append(i + 1)
        elif data[i + 1] < data[i] and data[i + 1] < data[i + 2]:
            extreme_points.append(i + 1)
    startp = []
    endp = []
    # find out the start point and end point of signal according to seted
    # shrehold
    for i in range(len(extreme_points) - 1):
        if data[extreme_points[i]] - data[extreme_points[i + 1]] > shrehold:
            startp.append(extreme_points[i])
        elif data[extreme_points[i + 1]] - data[extreme_points[i]] > shrehold:
            endp.append(extreme_points[i])
     # for each signal,do the cluster annlysis
    for i in range(len(startp)):
        start = startp[i]
        end = endp[i]
        buffer = data[start - 50:end + 50].copy()
        baseline, rms = k_means_cluster(buffer)
        new = fitting_data(buffer, baseline, rms)
        data[start - 50:end + 50] = new
    return data


if __name__ == '__main__':
    current = np.fromfile('current.bin', dtype=np.float32)
    sample_num = np.shape(current)[0]
    sample_rate = 100000
    time_series = np.arange(0, sample_num / sample_rate, 1 / sample_rate)
    modified_c = annalysis(current)
    plt.plot(time_series, current, color='b')
    plt.plot(time_series, modified_c, color='r')
#    sp,ep=annalysis(current)
#    start=sp[4]
#    end=ep[4]
#    plt.plot(time_series[start-50:end+50],current[start-50:end+50])
#
