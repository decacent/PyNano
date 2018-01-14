import numpy as np


def k_means_cluster(data, variety_num=2):
    # initial the center of each variety,each row of data represent one sample
    # and the column means featuer vectors
    sample_num = np.shape(data)[0]
    # randomly select one sample as the first center
    centers = data[np.random.randint(0, len(data) - 1)]
    # from the rest samples selcet one sample which with the largest euclid
    # distance with others as another center
    for i in range(variety_num - 1):
        dis = np.zeros(sample_num)
        for j in range(i + 1):
            if np.shape(centers) == ():
                dis = np.add(cal_dis(data, centers), dis)
                centers = np.vstack((centers, data[np.argmax(dis)]))
            else:
                dis = np.add(cal_dis(data, centers[j]), dis)
                centers = np.vstack((centers, data[np.argmax(dis)]))
    # start the iteration
    while True:
        # cppy the centers in order to exit with judgement
        cen_copy = centers.copy()
        # determine which population the sample belongs
        lable = np.zeros(sample_num)
        dis_2d = cal_dis(data, centers[0])
        for j in range(variety_num - 1):
            dis_2d = np.vstack((dis_2d, cal_dis(data, centers[j + 1])))
        dis_2d = dis_2d.T
        for i in range(sample_num):
            lable[i] = np.argmin(dis_2d[i])

        # recalculate the center of each populaton
        for i in range(variety_num):
            centers[i] = data[lable == i].mean()

        # verify whether the center changes
        if False not in (cen_copy == centers):
            break
        std = np.zeros(variety_num)
        for i in range(variety_num):
            std[i] = data[lable == i].std()
        select_lable = np.argmax(centers)
        return centers[select_lable], std[select_lable]


def cal_dis(data, center):
    # compute the distance between given data set and center
    buffer = np.subtract(data, center)
    buffer = np.square(buffer)
    if buffer.ndim != 1:
        distance = buffer.sum(axis=1)
    else:
        distance = buffer

    return np.sqrt(distance)
