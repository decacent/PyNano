#!/usr/bin/env python

# encoding: utf-8

'''

@author: decacent

@license: Copyright (C) 2017-2018 decacent. All rights reserved.

@contact: shaochuang_routine@outlook.com

@software: pycharm

@file: xdatio.py

@time: 2017/11/14 10:27

@desc:

'''

import struct
from io import open, BufferedReader

import numpy as np

xdata_header = [
    ('Version', 'f', 0),
    ('DeviceSeries', 'i', 4),
    ('Vref', 'f', 8),
    ('StartTime', '7i', 12),
    ('StopTime', '7i', 40),
    ('Voffset', 'f', 68),
    ('Ioffset', 'f', 72),
    ('SamplingRate', 'i', 76),
    ('CutoffFrequency', 'i', 80),
    ('DataCount', 'i', 84),
    ('DataByteLength', 'i', 92)
]


sampling = [1000, 10000, 50000, 100000, 250000, 500000]
CutOffFreq = [0, 10000, 5000]


class StructFile(BufferedReader):
    def read_f(self, fmt, offset=None):
        if offset is not None:
            self.seek(offset)
        return struct.unpack(fmt, self.read(struct.calcsize(fmt)))

    def write_f(self, fmt, offset=None, *args):
        if offset is not None:
            self.seek(offset)
        self.write(struct.pack(fmt, *args))


class Xdat_io():
    def __init__(self, filename=None):
        """
        This class read a xdat file.

        Arguments:
            filename : the filename to read
        """

        self.filename = filename

    def read_header(self):
        fid = StructFile(open(self.filename, 'rb'))
        header = {}
        for key, fmt, offset in xdata_header:
            val = fid.read_f(fmt, offset=offset)
            if len(val) == 1:
                header[key] = val[0]
            else:
                header[key] = np.array(val)
        return header

    def read_xdat(self):
        header = self.read_header()
        dt = np.dtype('float32')
        data = np.memmap(self.filename, dt, 'r', offset=96)
        data = data.reshape(-1, 2)
        nbepisod = 0
        sampling_rate = sampling[header['SamplingRate']]
        datas = []
        datas.append(data)
        return datas, sampling_rate, nbepisod
