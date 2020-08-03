#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   tdmsio.py
@Time    :   2020/05/30 15:44:18
@Author  :   Wnight
@Version :   1.0
@Contact :   shaochuangliu_routine@outlook.com
@License :   (C)Copyright 2020
@Desc    :   None
'''
import numpy as np
from nptdms import TdmsFile


class Tdms_io():

    def __init__(self, filename=None):
        self.filename=filename

    def read(self):
        fn=TdmsFile(self.filename)
        data=[]
        groups=fn.groups()
        sweeps=len(groups)
        for i in groups:
            data.append(i.as_dataframe().values)
        sam=int(1/np.float32(groups[0].channels()[0].properties['wf_increment']))
        return data, sam, sweeps
