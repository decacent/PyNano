#!/usr/bin/env python

# encoding: utf-8

'''

@author: decacent

@license: Copyright (C) 2017-2018 decacent. All rights reserved.

@contact: shaochuang_routine@outlook.com

@software: pycharm

@file: PyNano.py

@time: 2018/1/14 18:27

@desc:

You are not expected to understand this.

'''

import gc
import os
import sys
import time
from requests import get
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
#import PySide.QtCore.pyqtSignal
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QSplashScreen, QDialog

import matplotlib as mpl

mpl.use('Qt5Agg')
import numpy as np
import scipy.io as sio
from scipy import sparse
from scipy.sparse.linalg import spsolve
from requests import get
import matplotlib.pyplot as plt
import analysis, ui, tool
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from analysis.scat_analy import signal_extract, collision_analy, markov, signal_extract3, \
    signal_extract_cluster, signal_extract2, pointsaltation,signal_adept2
#from analysis.pointSaltation import signal_extract2
from matplotlib.widgets import SpanSelector, Cursor, Slider
from analysis.axonio import Abf_io
from analysis.xdatio import Xdat_io
from analysis.tdmsio import Tdms_io
from tool.tool import Analy_tool
from ui.pynano_ui import Ui_mainWindow
from ui.input_par import Ui_Dialog
from ui.about import Ui_about

# from ui.languist import Ui_languist

mpl.rcParams['agg.path.chunksize'] = 10000


class Extract_1(QtCore.QThread):
    '''
    信号提取线程，用于数据处理部分，该过程消耗时间较长。
    '''
    trigger = pyqtSignal(list)

    def __init__(
            self,
            init_time,
            data,
            model,
            peak_th,
            base,
            endth,
            base_num,
            end_num,
            is_up,
            sigma=3,
            th=100,
            sam=100000,
            filter=3000,
            is_filter=False,
            n_cluster=2,
            kernel_size=51,
            parent=None):
        super(Extract_1, self).__init__()
        self.init_time = init_time
        self.data = data
        self.model = model
        self.peak_th = peak_th
        self.base = base
        self.th = th
        self.sam = sam
        self.is_filter = is_filter
        self.filter = filter
        self.is_up = is_up
        self.endth = endth
        self.base_num = base_num
        self.end_num = end_num
        self.is_success = False
        self.n_cluster = n_cluster
        self.k_size = kernel_size
        self.sigma = sigma

    def run(self):
        try:
            if self.model == 0:
                self.extracted_signal, self.fit_data = signal_extract(
                    self.data, th=self.th, sam=self.sam, is_filter=self.is_filter, filter=self.filter)
            elif self.model == 1:
                self.extracted_signal, self.fit_data = collision_analy(data=self.data, th=self.th, sam=self.sam,
                                                                       end_th=self.endth, peak_th=self.peak_th,
                                                                       base_num=self.base_num,
                                                                       end_num=self.end_num, is_up=self.is_up)
            elif self.model == 2:
                self.extracted_signal, self.fit_data = signal_extract2(init_time=self.init_time, data=self.data,
                                                                       peak_th=self.peak_th, base=self.base,
                                                                       th=self.th,
                                                                       sam=self.sam, is_filter=self.is_filter,
                                                                       filter=self.filter, is_up=self.is_up)
            elif self.model == 3:
                self.extracted_signal, self.fit_data = signal_extract3(init_time=self.init_time, data=self.data,
                                                                       peak_th=self.peak_th, base=self.base,
                                                                       th=self.th,
                                                                       sam=self.sam, is_filter=self.is_filter,
                                                                       filter=self.filter, is_up=self.is_up)
            elif self.model == 4:
                self.extracted_signal, *self.fit_data = signal_extract_cluster(init_time=self.init_time, data=self.data,
                                                                               peak_th=self.peak_th, base=self.base,
                                                                               th=self.th, sam=self.sam,
                                                                               n_cluster=self.n_cluster,
                                                                               kernel_size=self.k_size, is_up=False
                                                                               )
            elif self.model == 5:
                self.extracted_signal, self.fit_data = pointsaltation(init_time=self.init_time, data=self.data,
                                                                               sigma=self.sigma,
                                                                               sam=self.sam,
                                                                               is_up=False
                                                                               )
            else:
                self.extracted_signal, self.fit_data = signal_adept2(init_time=self.init_time, data=self.data,
                                                                       peak_th=self.peak_th, base=self.base,
                                                                       th=self.th,
                                                                       sam=self.sam, is_filter=self.is_filter,
                                                                       filter=self.filter, is_up=self.is_up)                


            self.is_success = True
            self.trigger.emit(
                [self.extracted_signal, self.fit_data, self.is_success])
        except Exception as e:
            print(e)
            self.extracted_signal = None
            self.fit_data = None
            self.is_success = False
            self.trigger.emit(
                [self.extracted_signal, self.fit_data, self.is_success])
            # return self.extracted_signal,self.fit_data


def update_download(version, url):
    '''
    在线更新
    已停止服务
    Args:
        version:
        url:

    Returns:

    '''
    r = get('https://decacent.github.io/PyNano/data.json')
    now_version = r.json()['Version']
    if now_version != version:
        try:
            r = get(url)
            with open("PyNano.zip", "wb") as code:
                code.write(r.content)
        except BaseException:
            pass


def error(func,**kwargs):
    def wrapper(self, *args, **kwargs):
        try:
            u = func(self,**kwargs)
            return u
        except Exception as e:
            QMessageBox.information(self, self.tr("Notice"), self.tr(traceback.format_exc()), QMessageBox.Ok)
    return wrapper


def baselineflat(y, lamp=12, p=0.01, niter=10):
    """
    拉平基线
    """
    lam = 10 ** lamp
    L = len(y)
    D = sparse.csc_matrix(np.diff(np.eye(L), 2))
    w = np.ones(L)
    z = 0
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w * y)
        w = p * (y > z) + (1 - p) * (y < z)
    return z


class Scat_analy(QMainWindow, Ui_mainWindow):

    def __init__(self, langues, parent=None):
        super(Scat_analy, self).__init__(parent)
        self.setupUi(self)
        # _translate = QtCore.QCoreApplication.translate
        self.toolWindow = Analy_tool()
        self.verticalLayout_11.addWidget(self.toolWindow)
        self.version = 2.8
        self.language = langues
        self.comboBox.setCurrentIndex(2)
        # 初始化信号提取部分变量
        self.fn = ''  # abf文件路径
        self.sam = 100000  # abf 文件采样率
        self.sweeps = 0  # abf文件sweep的个数
        self.data = None  # 读取的abf 数据
        self.time = None  # abf数据时间序列
        self.extracted_signal = None  # 提取的信号
        self.fit_data = None  # 拟合的数据序列
        self.is_extracted = False  # 是否设置了部分提取
        self.sweep = 0  # 当前分析的sweep
        self.channel = 2  # abf 的通道数，即是否包含电压通道
        self.spinBox.setValue(10)
        self.is_part = False  # 是否部分提取
        self.markov_stage = []
        self.line = []
        # 设置初始态
        self.statusBar().showMessage("Ready")
        self.label_8.setText('0 mv')
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.gaptime = self.spinBox.value()
        self.gap_initime = self.spinBox_2.value()
        # 添加signal 提取部分初始态
        self.is_view = False
        self.is_view_signal = False
        self.is_partview = False
        self.is_read = False
        self.is_markov = False
        self.markov_ready = False
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        self.figure1 = plt.figure(1, facecolor='#f0f0f0')
        self.ax1 = self.figure1.add_subplot(111)
        self.figure1.subplots_adjust(left=0.08, right=0.95, top=0.90)
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.verticalLayout.addWidget(self.toolbar1)
        self.verticalLayout.addWidget(self.canvas1)
        self.canvas1.setSizePolicy(sizePolicy)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.figure2 = plt.figure(2, facecolor='#f0f0f0')
        self.ax2 = self.figure2.add_subplot(111)
        self.figure2.subplots_adjust(top=0.90)
        self.canvas2 = FigureCanvas(self.figure2)
        self.canvas2.setMinimumWidth(300)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        # self.toolbar2.setMaximumWidth(400)
        self.verticalLayout_5.addWidget(self.toolbar2)
        self.verticalLayout_5.addWidget(self.canvas2)
        self.canvas2.setSizePolicy(sizePolicy)
        self.figure3 = plt.figure(3, facecolor='#f0f0f0')
        self.ax3 = self.figure3.add_subplot(111)
        self.figure3.subplots_adjust(top=0.90)
        self.canvas3 = FigureCanvas(self.figure3)
        # self.canvas3.setMinimumWidth(300)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        # self.toolbar3.setMaximumWidth(400)
        self.verticalLayout_3.addWidget(self.toolbar3)
        self.verticalLayout_3.addWidget(self.canvas3)
        # markov 概率表格图
        self.figure4 = plt.figure(4, facecolor='#f0f0f0')
        self.ax4 = self.figure4.add_subplot(111)
        self.figure4.subplots_adjust(left=0.14, right=0.95, top=0.97)
        self.ax4.set_axis_off()
        self.ax4.text(0.5, 0.5, 'Markov Chain', color='r',
                      fontsize=40, fontname=['Courier', 'DejaVu Sans Mono'],
                      horizontalalignment='center',
                      verticalalignment='center',
                      transform=self.ax4.transAxes,
                      )
        self.canvas4 = FigureCanvas(self.figure4)
        # self.canvas4.setMaximumWidth(600)
        self.canvas4.setMinimumWidth(400)
        self.canvas4.setSizePolicy(sizePolicy)
        self.verticalLayout_7.addWidget(self.canvas4)
        # 初始化widget
        self.widget_2.hide()
        self.widget_2s1.hide()
        self.widget_2s2.hide()
        self.widget_4.hide()
        # 主面板按钮动作
        self.pushButton.clicked.connect(self.loadabf)
        self.pushButton_2.clicked.connect(self.viewdata)
        self.pushButton_3.clicked.connect(self.extract)
        self.pushButton_4.clicked.connect(self.viewsignal)
        self.pushButton_5.clicked.connect(self.sweep_plot_previous)
        self.pushButton_6.clicked.connect(self.sweep_plot_next)
        self.pushButton_7.clicked.connect(self.save_result)
        self.pushButton_8.clicked.connect(self.child_about)

        self.pushButton_9.clicked.connect(self.previous_view)
        self.pushButton_10.clicked.connect(self.next_view)
        self.pushButton_11.clicked.connect(self.gap_refresh)
        self.pushButton_12.clicked.connect(self.all_hist)

        self.pushButton_13.clicked.connect(self.plot_currentHist)
        self.pushButton_14.clicked.connect(self.plot_Scattering)
        self.pushButton_15.clicked.connect(self.markov_analy)
        self.pushButton_16.clicked.connect(self.hist_refresh)
        self.pushButton_17.clicked.connect(self.markov_save)
        self.pushButton_18.clicked.connect(self.widget_result)
        self.pushButton_19.clicked.connect(self.widget_markov)
        # self.pushButton_allhist.clicked.connect(self.all_hist)
        # self.previous_t1.clicked.connect(self.previous_view)
        # self.next_t1.clicked.connect(self.next_view)
        # self.part_view_init.clicked.connect(self.gap_refresh)
        # 画布事件
        self.cid = self.figure1.canvas.mpl_connect(
            'button_press_event', self.onclick)  # 双击图片获取电压
        self.span = SpanSelector(
            self.ax1,
            self.onselect,
            'horizontal',
            useblit=True,
            button=3,
            rectprops=dict(
                alpha=0.3,
                facecolor='g'))
        self.cursor = Cursor(
            self.ax3,
            useblit=True,
            horizOn=False,
            color='red',
            linewidth=2)
        self.cid2 = self.figure3.canvas.mpl_connect(
            'button_press_event', self.onclick1)

        # 信号槽
        self.spinBox.editingFinished.connect(self.gap_refresh)
        self.spinBox_2.editingFinished.connect(self.gap_refresh)
        self.comboBox_2.currentIndexChanged['int'].connect(
            self.plot_currentHist)
        self.spinBox_3.editingFinished.connect(self.plot_currentHist)
        self.double_SpinBox_4.editingFinished.connect(self.plot_currentHist)
        self.spinBox_5.editingFinished.connect(self.plot_currentHist)
        self.spinBox_6.editingFinished.connect(self.plot_Scattering)
        self.comboBox_3.currentIndexChanged['int'].connect(
            self.plot_Scattering)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            self.tr('Warning'),
            self.tr('Please save result,\nExit really?'),
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
#           self.set_writeini()
            event.accept()
        else:
            event.ignore()

    @error
    def set_writeini(self):
        pass
        setting = QtCore.QSettings('a.ini', QtCore.QSettings.IniFormat)
        setting.beginGroup('window')
        setting.setIniCodec('UTF-8')
        s1 = setting.setValue('model', self.comboBox.currentIndex())
        setting.setValue('language', self.language)
        setting.setValue('window_size', self.geometry())
        setting.endGroup()
        return True

    @error
    def all_hist(self):
        if not self.is_read:
            return None
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.15)
        bin_num = 300

        def init_plot():
            nonlocal ax, bin_num
            ax.cla()
            if self.is_part:

                if self.channel != 0:
                    s1 = min(self.data[self.sweep]
                             [self.star_point:self.end_point, 0])
                    s2 = max(self.data[self.sweep]
                             [self.star_point:self.end_point, 0])
                    ax.hist(self.data[self.sweep][self.star_point:self.end_point, 0],
                            bins=bin_num, range=(s1, s2), facecolor='blue')
                    ax.set_xlim(s1, s2)
                else:
                    s1 = min(self.data[self.sweep]
                             [self.star_point:self.end_point])
                    s2 = max(self.data[self.sweep]
                             [self.star_point:self.end_point])
                    ax.hist(self.data[self.sweep][self.star_point:self.end_point],
                            bins=bin_num, range=(s1, s2), facecolor='blue')
                    ax.set_xlim(s1, s2)

            else:

                if self.channel != 0:
                    s1 = min(self.data[self.sweep][:, 0])
                    s2 = max(self.data[self.sweep][:, 0])
                    ax.hist(self.data[self.sweep][:, 0], bins=bin_num,
                            normed=1, range=(s1, s2), facecolor='blue')
                    ax.set_xlim(s1, s2)

                else:
                    s1 = min(self.data[self.sweep][:])
                    s2 = max(self.data[self.sweep][:])
                    ax.hist(self.data[self.sweep][:], bins=bin_num,
                            normed=1, range=(s1, s2), facecolor='blue')
                    ax.set_xlim(s1, s2)

        init_plot()
        fig.show()
        axcolor = 'lightgoldenrodyellow'
        axfreq = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
        sfreq = Slider(axfreq, 'Bins', 1, 1000, valinit=300)

        def update(val):
            nonlocal bin_num
            bin_num = int(sfreq.val)
            init_plot()

        sfreq.on_changed(update)

    @error
    def widget_result(self):
        if self.widget_2s2.isHidden():
            self.widget_2.show()
            self.widget_2s1.show()
            self.widget_2s2.show()
            self.widget_4.hide()
        else:
            self.widget_2.hide()
            self.widget_2s1.hide()
            self.widget_2s2.hide()
            self.widget_4.hide()

    @error
    def widget_markov(self):
        if self.widget_4.isHidden():
            self.widget_2.show()
            self.widget_2s1.show()
            self.widget_2s2.hide()
            self.widget_4.show()
        else:
            self.widget_2.hide()
            self.widget_2s1.hide()
            self.widget_2s2.hide()
            self.widget_4.hide()

    def onclick1(self, event):
        if self.is_extracted and self.markov_ready and event.dblclick:
            line = self.ax3.axvline(event.xdata, color='r')
            self.line.append(line)
            self.canvas3.draw()
            self.markov_stage.append(event.xdata)

    @error
    def hist_refresh(self):
        if len(self.line) > 0:
            try:
                for i in self.line:
                    i.remove()
            except BaseException:
                pass
            self.line = []
            self.canvas3.draw()
        else:
            pass

    @error
    def markov_analy(self):
        if self.is_extracted is False or not self.markov_ready:
            self.statusBar().showMessage(self.tr("No markov analysis result"))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No markov analysis result"),
                QMessageBox.Ok)
        elif self.markov_stage == []:
            self.statusBar().showMessage(self.tr("No markov analysis result"))
            QMessageBox.information(self, self.tr("Notice"), self.tr(
                "Please setup Markov Chain stage"), QMessageBox.Ok)

        else:
            self.markov_level = len(self.markov_stage) + 1
            self.markov_stage.append(float('-inf'))
            self.markov_stage.append(float('inf'))
            try:
                self.markov_data = markov(
                    self.extracted_signal,
                    ss=self.markov_stage,
                    stage_index=self.comboBox_2.currentIndex())
                self.markov_stage = []
                self.hist_refresh()
                self.is_markov = True
                self.plottable()
                self.statusBar().showMessage(self.tr('Markov chain analysis'))
            except BaseException:
                QMessageBox.information(self, self.tr("Errors"), self.tr(
                    "Please setup the right parameters"), QMessageBox.Ok)

    @error
    def markov_save(self):
        if not self.is_markov:
            self.statusBar().showMessage(self.tr("No markov analysis result"))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No markov analysis result"),
                QMessageBox.Ok)
            return None
        file_choices = "mat (*.mat)"
        path = QFileDialog.getSaveFileName(
            self, self.tr('Save Result'), '', file_choices)
        if path[0] != '':
            if path[1] == 'mat (*.mat)':
                self.markov_data['Current'] = self.extracted_signal[:, 0]
                self.markov_data['Time'] = self.extracted_signal[:, 1]
                self.markov_data['normI'] = self.extracted_signal[:, 2]
                sio.savemat(path[0], self.markov_data)
                self.figure4.savefig(path[0].split('.')[0] + '.jpg', dpi=150)
                k = int(np.ceil(self.markov_level / 2))
                fig = plt.figure()
                for i in range(self.markov_level):
                    ax = fig.add_subplot(2, k, i + 1)
                    ax.hist(self.markov_data['stage{0}'.format(i + 1)][:, 1],
                            bins=150, normed=0,
                            range=(0, np.max(self.markov_data['stage{0}'.format(i + 1)][:, 1])),
                            facecolor='blue', edgecolor='b')
                    ax.set_yticklabels(
                        np.round(ax.get_yticks() / len(self.markov_data['stage{0}'.format(i + 1)]), 2))
                    # ax.set_title('stage{0}'.format(i + 1))
                fig.suptitle("Time distribution")
                fig.subplots_adjust(wspace=0.2)
                fig.savefig(path[0].split('.')[0] + '_time.jpg', dpi=150)
                self.figure1.savefig(
                    path[0].split('.')[0] + '_data.jpg', dpi=150)
                self.figure2.savefig(
                    path[0].split('.')[0] + '_scatter.tif', dpi=150)
                self.figure3.savefig(
                    path[0].split('.')[0] + '_hist.tif', dpi=150)
                self.statusBar().showMessage(
                    self.tr('Saved to') + '%s' % path[0])
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Save Success"),
                    QMessageBox.Ok)
            else:
                QMessageBox.information(self, self.tr("Alert"), self.tr(
                    "please save to .mat  format"), QMessageBox.Ok)

        else:
            self.statusBar().showMessage(self.tr("Save failed"))
            QMessageBox.information(
                self,
                self.tr("Alert"),
                self.tr("Save Success"),
                QMessageBox.Ok)
            pass

    @error
    def plottable(self):

        if self.is_markov:
            self.statusBar().showMessage(self.tr('Markov chain transfer probability'))
            self.ax4.cla()
            a = ['stage' + str(x + 1) for x in range(self.markov_level)]
            the_table = self.ax4.table(
                cellText=np.round(
                    self.markov_data['probability'],
                    3),
                cellLoc='center',
                rowLabels=a,
                rowLoc='center',
                cellColours=plt.cm.GnBu(
                    np.round(
                        self.markov_data['probability'],
                        3)),
                colLabels=a,
                colColours=None,
                colLoc='center',
                loc='center',
                bbox=[
                    0,
                    0,
                    1,
                    1],
                fontsize=60)
            self.ax4.set_axis_off()
            self.canvas4.draw()

    @error
    def child(self):
        self.statusBar().showMessage(self.tr('Setup the analysis parameters'))
        self.is_set = False
        self.input_dialog = Ui_Dialog()
        self.Dialog_p = QDialog(self)
        self.input_dialog.setupUi(self.Dialog_p)
        if self.comboBox.currentIndex() != 1:
            self.input_dialog.label_3.hide()
            self.input_dialog.label_4.hide()
            self.input_dialog.label_5.hide()
            self.input_dialog.doubleSpinBox_endth.hide()
            self.input_dialog.spinBox_basenum.hide()
            self.input_dialog.spinBox_endnum.hide()

        if self.comboBox.currentIndex() != 4:
            self.input_dialog.label_ksize.hide()
            self.input_dialog.label_cluster.hide()
            self.input_dialog.spinBox_ksize.hide()
            self.input_dialog.spinBox_cluster.hide()

        if self.comboBox.currentIndex() != 5:
            self.input_dialog.label_sigma.hide()
            self.input_dialog.doubleSpinBox_sigma.hide()
        
        if self.comboBox.currentIndex() == 5:
            self.input_dialog.doubleSpinBox_baseline.hide()
            self.input_dialog.radioButton_3.hide()
            self.input_dialog.radioButton_4.hide()
            self.input_dialog.doubleSpinBox_base.hide()
            self.input_dialog.spinBox_cluster.hide()
            self.input_dialog.spinBox_ksize.hide()
            self.input_dialog.label_ksize.hide()
            self.input_dialog.label_cluster.hide()
            self.input_dialog.doubleSpinBox_th.hide()
            self.input_dialog.label_2.hide()
            self.input_dialog.label.hide()
            self.input_dialog.label_1.hide()

        if self.comboBox.currentIndex() == 0:
            self.input_dialog.doubleSpinBox_baseline.setEnabled(False)
            self.input_dialog.radioButton_3.setEnabled(False)
            self.input_dialog.radioButton_4.setEnabled(False)
            self.input_dialog.doubleSpinBox_base.setEnabled(False)
            self.input_dialog.spinBox_cluster.setEnabled(False)
            self.input_dialog.spinBox_ksize.setEnabled(False)
            self.input_dialog.label_ksize.setEnabled(False)
            self.input_dialog.label_cluster.setEnabled(False)
        try:
            self.input_dialog.doubleSpinBox_th.setValue(self.th)
            self.input_dialog.doubleSpinBox_base.setValue(self.peak_th)
            self.input_dialog.doubleSpinBox_endth.setValue(self.endth)
            self.input_dialog.spinBox_basenum.setValue(self.base_num)
            self.input_dialog.spinBox_endnum.setValue(self.end_num)
            self.input_dialog.doubleSpinBox_baseline.setValue(self.baseline)
            self.input_dialog.checkBox_resam.setChecked(self.is_filter)
            self.input_dialog.spinBox_sam.setValue(self.filter)
            self.input_dialog.radioButton_4.setChecked(self.is_up)
            self.input_dialog.spinBox_ksize.setValue(self.k_size)
            self.input_dialog.spinBox_cluster.setValue(self.n_cluster)
        except BaseException:
            pass
        self.input_dialog.pushButton.clicked.connect(self.get_param)
        self.input_dialog.pushButton_2.clicked.connect(self.APPclose)
        self.Dialog_p.exec_()

    @error
    def child_about(self):
        self.about_dia = Ui_about()
        self.Dialog_d = QDialog(self)
        self.about_dia.setupUi(self.Dialog_d)
        self.about_dia.label_4.setText(str(self.version))
        self.about_dia.about_close.clicked.connect(self.about_close)
        self.about_dia.about_help.clicked.connect(self.about_help)
        self.about_dia.about_update.clicked.connect(self.about_update)
        self.Dialog_d.exec_()

    @error
    def about_help(self):
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl('https://decacent.github.io/PyNano/'))

    @error
    def about_update(self):
        r = get('https://decacent.github.io/PyNano/data.json')
        new_version = float(r.json()['Version'])
        feature=r.json()['Feature']
        if self.version < new_version:
            QMessageBox.information(
                self, self.tr("Update"), self.tr(
                        "Version {} is available\nPlease  execution command to update\n>> git fetch --all \n>> git reset --hard origin/master\n>>git pull\n{}".format(new_version,feature)), QMessageBox.Ok)
            QtGui.QDesktopServices.openUrl(
                    QtCore.QUrl('https://github.com/decacent/PyNano/releases'))
        else:
            QMessageBox.information(
                self,
                self.tr("Update"),
                self.tr("No update available"),
                QMessageBox.Ok)
        # except BaseException:
        #     QMessageBox.information(
        #         self,
        #         self.tr("Update"),
        #         self.tr("Internet connect error"),
        #         QMessageBox.Ok)

    @error
    def init_update(self):
        try:
            r = get('https://decacent.github.io/PyNano/data.json')
            new_version = float(r.json()['Version'])
            feature=r.json()['Feature']
            if self.version < new_version:
                QMessageBox.information(
                    self, self.tr("Update"), self.tr(
                        "Version {} is available\nPlease  execution command to update\n>> git fetch --all \n>> git reset --hard origin/master\n>>git pull\n{}".format(new_version,feature)), QMessageBox.Ok)
                QtGui.QDesktopServices.openUrl(
                    QtCore.QUrl('https://github.com/decacent/PyNano/releases'))
            else:
                pass

        except BaseException:
            pass

    @error
    def about_close(self):
        self.Dialog_d.close()

    @error
    def get_param(self):
        self.th = self.input_dialog.doubleSpinBox_th.value()
        self.peak_th = self.input_dialog.doubleSpinBox_base.value()
        self.endth = self.input_dialog.doubleSpinBox_endth.value()
        self.base_num = self.input_dialog.spinBox_basenum.value()
        self.end_num = self.input_dialog.spinBox_endnum.value()
        self.baseline = self.input_dialog.doubleSpinBox_baseline.value()
        self.is_filter = self.input_dialog.checkBox_resam.isChecked()
        self.filter = self.input_dialog.spinBox_sam.value()
        self.is_up = False if self.input_dialog.radioButton_3.isChecked() else True
        self.n_cluster = self.input_dialog.spinBox_cluster.value()
        self.k_size = self.input_dialog.spinBox_ksize.value()
        self.is_set = True
        self.sigma=self.input_dialog.doubleSpinBox_sigma.value()
        self.Dialog_p.close()

    @error
    def APPclose(self):
        self.is_set = False
        self.statusBar().showMessage(self.tr('Cancel anslysis'))
        self.Dialog_p.close()

    @error
    def figure_init(self):
        self.ax1.cla()
        gc.collect()

    @error
    def save_result(self):
        # 保存信号提取结果
        if self.extracted_signal is None:
            self.statusBar().showMessage(self.tr('No result'))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No result"),
                QMessageBox.Ok)
            return None
        if self.comboBox.currentIndex() == 4:
            file_choices = "CSV (*.csv);"
            path = QFileDialog.getSaveFileName(
                self, self.tr('Save Result'), '', file_choices)
            head_index = np.shape(self.extracted_signal)[1]
            heads = 'init_time,baseline'
            for i in range(int((head_index - 2) / 2)):
                heads += ',Current_{}'.format(i + 1) + ',Time_{}'.format(i + 1)
            self.statusBar().showMessage(
                self.tr('Saved to %s' % path[0]))
            np.savetxt(
                path[0],
                self.extracted_signal,
                delimiter=',',
                header=heads)
            self.statusBar().showMessage(self.tr('Save success'))
            return None

        file_choices = "CSV (*.csv);;mat (*.mat)"
        path = QFileDialog.getSaveFileName(
            self, self.tr('Save Result'), '', file_choices)
        head3 = 'Current(pA),Time(ms),I/I0'
        head6 = 'Current(pA),Time(ms),I/I0,Baseline(pA),Delta I(pA),Charge(pC)'
        head7 = 'Current(pA),Time(ms),I/I0,Baseline(pA),Delta I(pA),Charge(pC),Initial time(ms)'
        head = [
            'Current(pA)',
            'Time (ms)',
            'normI',
            'Baseline (pA)',
            'DeltaI (pA)',
            'Charge (pC)',
            'InitialTime']
        head_index = np.shape(self.extracted_signal)[1]
        if head_index == 3:
            head_row1 = head3
        elif head_index == 6:
            head_row1 = head6
        else:
            head_row1 = head7

        if path[0] != '':
            try:
                if path[1] == 'mat (*.mat)':
                    mat_dict = {}
                    for i in range(head_index):
                        mat_dict[head[i]] = self.extracted_signal[:, i]
                    self.statusBar().showMessage(
                        self.tr('Saved to %s' % path[0]))
                    sio.savemat(path[0], mat_dict)
                elif path[1] == 'CSV (*.csv)':
                    self.statusBar().showMessage(
                        self.tr('Saved to %s' % path[0]))
                    np.savetxt(
                        path[0],
                        self.extracted_signal,
                        delimiter=',',
                        header=head_row1)
                self.statusBar().showMessage(self.tr('Save success'))
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Save success"),
                    QMessageBox.Ok)
            except BaseException:
                QMessageBox.information(self, self.tr("Alert"), self.tr(
                    "Save failed/n Please check whether the file is occupied. "), QMessageBox.Ok)
                self.statusBar().showMessage(self.tr('Save failed'))

        else:
            QMessageBox.information(
                self,
                self.tr("Alert"),
                self.tr("Save failed"),
                QMessageBox.Ok)
            self.statusBar().showMessage(self.tr('Save failed'))
            pass

    @error
    def save_fig(self):
        pass

    def onclick(self, event):
        # 获取电压
        # if event.button != 1:

        if event.dblclick:
            if event.xdata is None or (self.fn == ''):
                pass
            else:
                if self.channel == 0 or self.channel == 1:
                    self.label_8.setText(self.tr('No voltage channel'))

                else:
                    t2 = event.xdata * self.sam
                    t3 = self.data[self.sweep][int(t2), 1]
                    self.label_8.setText('%s' % t3)
                    self.label_8.setAlignment(QtCore.Qt.AlignCenter)

    def onselect(self, xmin, xmax):
        if self.is_view or self.is_partview:
            self.checkBox.setChecked(True)
            self.doubleSpinBox.setValue(xmin)
            self.doubleSpinBox_2.setValue(xmax)
            self.star_point = int(self.doubleSpinBox.value() * self.sam)
            self.end_point = int(self.doubleSpinBox_2.value() * self.sam)
            self.is_part = True
            self.statusBar().showMessage(self.tr('Select the time range'))
        else:
            pass

    @error
    def extract(self):
        # 提取信号
        # if self.fn[0] == '' and self.data is None:
        if self.data is None:
            self.statusBar().showMessage(self.tr("No opened file"))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No opened file"),
                QMessageBox.Ok)
            pass
        else:
            self.child()
            if not self.is_set:
                return None
            # if (self.comboBox.currentIndex() == 0 or self.comboBox.currentIndex(
            # ) == 2) and not self.checkBox.isChecked() and self.is_resam:
            #     QMessageBox.information(self, self.tr("Warning"), self.tr(
            #         "Resampling need set time range"), QMessageBox.Ok)
            #     return None

            if self.comboBox.currentIndex() != 5 and (self.th == 0 or not self.is_set):
                QMessageBox.information(self, self.tr("Warning"), self.tr(
                    "Please setup the threshold"), QMessageBox.Ok)
                pass
            else:
                if self.checkBox.isChecked():  # 设置信号提取区域
                    self.is_part = True
                    self.star_point = int(
                        self.doubleSpinBox.value() * self.sam)
                    self.end_point = int(
                        self.doubleSpinBox_2.value() * self.sam)
                    if self.end_point <= self.star_point:
                        QMessageBox.information(
                            self,
                            self.tr("Warning"),
                            self.tr("Time range set is wrong"),
                            QMessageBox.Ok)
                        return None
                    else:
                        if self.channel != 0:
                            self.analysis_data = self.data[self.sweep][self.star_point:self.end_point, 0]
                        else:
                            self.analysis_data = self.data[self.sweep][self.star_point:self.end_point]
                else:
                    self.is_part = False
                    self.star_point = 0
                    if self.channel != 0:
                        self.analysis_data = self.data[self.sweep][:, 0]
                    else:
                        self.analysis_data = self.data[self.sweep][:]
                try:
                    self.statusBar().showMessage(self.tr("Runing..."))
                    self.extract1 = Extract_1(
                        init_time=self.star_point / 100,
                        data=self.analysis_data,
                        model=self.comboBox.currentIndex(),
                        peak_th=self.peak_th,
                        base=self.baseline,
                        endth=self.endth,
                        base_num=self.base_num,
                        end_num=self.end_num,
                        th=self.th,
                        sigma=self.sigma,
                        sam=self.sam,
                        is_filter=self.is_filter,
                        filter=self.filter,
                        is_up=self.is_up,
                        n_cluster=self.n_cluster,
                        kernel_size=self.k_size
                    )
                    self.widget.setEnabled(False)
                    self.extract1.trigger.connect(self.extract1_end)
                    self.extract1.start()
                except Exception as e:
                    print(e)
                    QMessageBox.information(self, self.tr("Alert"), self.tr(
                        "Errors，please checkup the setup"), QMessageBox.Ok)
                    self.statusBar().showMessage(self.tr("Run extract failed"))
    
    def extract1_end(self, ls):
        if ls[2]:
            self.extracted_signal = ls[0]
            if self.comboBox.currentIndex() == 4:
                self.fit_data = ls[1][0]
            else:
                self.fit_data = ls[1]
            self.is_extracted = True
            self.widget.setEnabled(True)
            QMessageBox.information(
                self,
                self.tr("Notice"),
                self.tr("Analysis success"),
                QMessageBox.Ok)
            self.statusBar().showMessage(self.tr("Analysis success"))
            self.label_10.setText(str(len(self.extracted_signal)))
            self.label_10.setAlignment(QtCore.Qt.AlignCenter)
            if len(self.extracted_signal) > 0 and self.comboBox.currentIndex() != 4:
                self.plot_currentHist()
                self.plot_Scattering()
                if self.widget_2s1.isHidden():
                    self.widget_2.show()
                    self.widget_2s1.show()
                    self.widget_2s2.show()
                    self.widget_4.hide()
        else:
            self.widget.setEnabled(True)
            QMessageBox.information(self, self.tr("Alert"), self.tr(
                "Errors，please checkup the setup"), QMessageBox.Ok)
            self.statusBar().showMessage(self.tr("Run extract failed"))

    @error
    def viewsignal(self):
        # 预览拟合结果
        if self.is_extracted is False:
            self.statusBar().showMessage(self.tr("No result"))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No result"),
                QMessageBox.Ok)
            pass
        else:
            if self.is_part:  # 设置信号提取区域

                self.statusBar().showMessage(self.tr('Plot the fitted signal'))
                self.figure_init()

                if self.channel != 0:
                    self.ax1.plot(self.time[self.star_point:self.end_point],
                                  self.data[self.sweep][self.star_point:self.end_point, 0], ':')
                else:
                    self.ax1.plot(self.time[self.star_point:self.end_point],
                                  self.data[self.sweep][self.star_point:self.end_point], ':')

                self.ax1.plot(
                    self.time[self.star_point:self.end_point], self.fit_data)
                self.ax1.set_xlabel('time/s')
                self.ax1.set_ylabel('Current/pA')
                self.canvas1.draw()
            else:
                self.statusBar().showMessage(self.tr('Plot the fitted signal'))
                self.figure_init()
                if self.channel != 0:
                    self.ax1.plot(self.time, self.data[self.sweep][:, 0], ':')
                else:
                    self.ax1.plot(self.time, self.data[self.sweep], ':')

                self.ax1.plot(self.time, self.fit_data)
                self.ax1.set_xlabel('time/s')
                self.ax1.set_ylabel('Current/pA')
                self.canvas1.draw()
            self.is_view = False
            self.is_view_signal = True
            self.is_partview = False

    @error
    def plot_Scattering(self):
        # 绘制散点图

        if self.is_extracted is False or self.comboBox.currentIndex() == 4:
            self.statusBar().showMessage(self.tr("No result"))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No result"),
                QMessageBox.Ok)
            pass
        else:
            self.ax2.cla()
            self.statusBar().showMessage(self.tr('Plot the scatering'))
            if self.comboBox_3.currentIndex() == 0:
                la = 0
            elif self.comboBox_3.currentIndex() == 1:
                la = 2
            else:
                la = 4
            if self.comboBox.currentIndex() == 0 and la == 4:
                la = 0
                QMessageBox.information(
                    self,
                    self.tr("Warning"),
                    self.tr("No ΔI result"),
                    QMessageBox.Ok)
            self.ax2.scatter(self.extracted_signal[:,
                             la],
                             self.extracted_signal[:,
                             1],
                             marker='o',
                             color='b',
                             s=self.spinBox_6.value())
            self.ax2.set_ylabel('Time/ms')
            self.ax2.set_xlabel('%s/pA' % self.comboBox_3.currentText())
            self.ax2.set_title('Scattering')
            self.ax2.set_xlim(min(self.extracted_signal[:, la]), max(
                self.extracted_signal[:, la]))
            # self.ax2.set_xlim(500, 2500)
            self.ax2.set_ylim(
                0, int(np.ceil((max(self.extracted_signal[:, 1])))))
            # self.ax2.set_ylim(0, 4)
            self.canvas2.draw()

    @error
    def plot_currentHist(self):
        # 绘制电流Hist
        if self.is_extracted is False or self.comboBox.currentIndex() == 4:
            self.statusBar().showMessage(self.tr("No result"))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No result"),
                QMessageBox.Ok)
            pass
        else:
            self.statusBar().showMessage(self.tr('Plot the Histogram'))
            if self.comboBox_2.currentIndex() == 0:
                la = 0
                text = 'I/pA'
                self.markov_ready = True
            elif self.comboBox_2.currentIndex() == 1:
                la = 1
                text = 'Time/ms'
                self.markov_ready = False
            elif self.comboBox_2.currentIndex() == 2:
                la = 2
                text = 'I/I0'
                self.markov_ready = True
            elif self.comboBox_2.currentIndex() == 3:
                la = 4
                text = 'Δ/pA'
                self.markov_ready = False
            else:
                la = 5
                text = 'Q/pC'
                self.markov_ready = True
            s1 = self.spinBox_3.value()
            s2 = self.double_SpinBox_4.value()

            if self.comboBox.currentIndex() == 0 and la == 5:
                QMessageBox.information(
                    self,
                    self.tr("Warning"),
                    self.tr("No charge result"),
                    QMessageBox.Ok)
                pass
            elif self.comboBox.currentIndex() == 0 and la == 4:
                QMessageBox.information(
                    self,
                    self.tr("Warning"),
                    self.tr("No ΔI result"),
                    QMessageBox.Ok)
            else:
                if s2 <= s1:
                    s1 = min(self.extracted_signal[:, la])
                    s2 = max(self.extracted_signal[:, la])
                self.ax3.cla()
                self.statusBar().showMessage(self.tr('Plotting histogram...'))
                self.ax3.hist(self.extracted_signal[:, la], bins=self.spinBox_5.value(
                ), range=(s1, s2))
                self.ax3.set_yticklabels(
                    np.round(self.ax3.get_yticks() / len(self.extracted_signal[:, la]), 2))
                self.ax3.set_ylabel('Probability')
                self.ax3.set_xlabel('%s' % text)
                self.ax3.set_title('Hist')
                self.ax3.set_xlim(s1, s2)
                # self.ax3.set_xlim(500, 2500)
                self.canvas3.draw()
                self.markov_stage = []

    @error
    def loadabf(self):

        self.statusBar().showMessage(self.tr("Open file"))
        self.fn = QFileDialog.getOpenFileName(self, self.tr(
            "Open file"), filter='Abf Files (*.abf);;Xdat Files (*.xdat);;Tdms Files (*.tdms)')
        print(self.fn[0])
        print(self.fn[1])
        if self.fn[0] == '':
            self.statusBar().showMessage(self.tr("No file selected"))
            self.fn = ''
            return None
        elif self.fn[1] == 'Abf Files (*.abf)':
            self.statusBar().showMessage(self.tr("Reading ABF.."))
            try:
                f = Abf_io(self.fn[0])
                self.data, self.sam, self.sweeps = f.read_abf()
                self.time = np.arange(
                    0, len(self.data[0]) / self.sam, 1 / self.sam)
                self.time = self.time[0:len(self.data[0])]
                self.is_read = True
                self.statusBar().showMessage(
                    self.tr('ABF load success..') +
                    os.path.basename(
                        self.fn[0]))
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Load success"),
                    QMessageBox.Ok)
                self.label_6.setText('1/%d' % (self.sweeps))
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_sample_rate.setText('%dk' % (self.sam / 1000))
                self.label_sample_rate.setAlignment(QtCore.Qt.AlignCenter)
            except BaseException:
                self.statusBar().showMessage(self.tr('File load failed'))
                QMessageBox.information(self, self.tr("Alert"), self.tr(
                    "File load error，Abf version should > 2.0 "), QMessageBox.Ok)

            try:
                self.channel = self.data[0].shape[1]
            except BaseException:
                self.channel = 0
        elif self.fn[1] == 'Xdat Files (*.xdat)':
            try:
                f = Xdat_io(self.fn[0])
                self.data, self.sam, self.sweeps = f.read_xdat()
                self.time = np.arange(
                    0, len(self.data[0]) / self.sam, 1 / self.sam)
                self.time = self.time[0:len(self.data[0])]
                self.channel = 2
                self.is_read = True
                self.statusBar().showMessage(
                    self.tr('Load Xdat success..') +
                    os.path.basename(
                        self.fn[0]))
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Load success"),
                    QMessageBox.Ok)
                self.label_6.setText('1/%d' % (self.sweeps))
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_sample_rate.setText('%dk' % (self.sam / 1000))
                self.label_sample_rate.setAlignment(QtCore.Qt.AlignCenter)
            except BaseException:
                self.statusBar().showMessage(self.tr('File load failed'))
                QMessageBox.information(
                    self,
                    self.tr("Alert"),
                    self.tr("Fail load failed"),
                    QMessageBox.Ok)
        elif self.fn[1] == 'Tdms Files (*.tdms)':
            self.statusBar().showMessage(self.tr("Reading TDMS.."))
            print(self.fn[1])
            try:
                print(self.fn[0])
                f = Tdms_io(self.fn[0])
                self.data, self.sam, self.sweeps = f.read()
                print('success')
                self.time = np.arange(
                    0, len(self.data[0]) / self.sam, 1 / self.sam)
                self.time = self.time[0:len(self.data[0])]
                self.is_read = True
                self.statusBar().showMessage(
                    self.tr('TDMS load success..') +
                    os.path.basename(
                        self.fn[0]))
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Load success"),
                    QMessageBox.Ok)
                self.label_6.setText('1/%d' % (self.sweeps))
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_sample_rate.setText('%dk' % (self.sam / 1000))
                self.label_sample_rate.setAlignment(QtCore.Qt.AlignCenter)
            except BaseException as e:
                print(e)
                self.statusBar().showMessage(self.tr('File load failed'))
                QMessageBox.information(self, self.tr("Alert"), self.tr(
                    "File load error，Please chaeck the tdms file formats!"), QMessageBox.Ok)

            try:
                self.channel = self.data[0].shape[1]
            except BaseException:
                self.channel = 0

    @error
    def viewdata(self):
        if self.fn == '' and self.data is None:
            self.statusBar().showMessage(self.tr('No file loaded'))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No filed loaded"),
                QMessageBox.Ok)
            pass
        else:
            if self.sweeps == 0 or self.sweeps > 22:
                self.sweep = 0
                self.statusBar().showMessage(self.tr('View the data'))
                self.figure_init()
                self.time = np.arange(
                    0, len(self.data[0]) / self.sam, 1 / self.sam)
                self.time = self.time[0:len(self.data[0])]
                if self.channel != 0:
                    self.ax1.plot(self.time, self.data[self.sweep][:, 0])
                else:
                    self.ax1.plot(self.time, self.data[self.sweep])
                self.ax1.set_xlabel('time/s')
                self.ax1.set_ylabel('Current/pA')
                self.canvas1.draw()

            else:
                self.sweep = 0
                self.statusBar().showMessage(self.tr('View the data'))
                self.figure_init()
                if self.channel != 0:
                    for i in range(self.sweeps):
                        self.time = np.arange(
                            0, len(self.data[i]) / self.sam, 1 / self.sam)
                        self.time = self.time[0:len(self.data[i])]
                        self.ax1.plot(self.time, self.data[i][:, 0])
                else:

                    for i in range(self.sweep):
                        self.time = np.arange(
                            0, len(self.data[i]) / self.sam, 1 / self.sam)
                        self.time = self.time[0:len(self.data[i])]
                        self.ax1.plot(self.time, self.data[i])
                self.ax1.set_xlabel('time/s')
                self.ax1.set_ylabel('Current/pA')
                self.canvas1.draw()
                self.label_6.setText('all/%d' % (self.sweeps))
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            self.is_view = True
            self.is_partview = False
            self.is_view_signal = False

    @error
    def next_view(self):
        # 部分预览数据
        if self.fn == '' and not self.is_read:
            self.statusBar().showMessage(self.tr('No file loaded'))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No filed loaded"),
                QMessageBox.Ok)
            pass
        else:  # self.is_view or (not self.is_view_signal):
            if self.gaptime > 0 and self.gap_initime < self.time[-1]:
                gap_start = int(self.gap_initime * self.sam)
                gap_end = int((self.gap_initime + self.gaptime) * self.sam)
                if gap_end < len(self.data[self.sweep]):
                    is_end = False
                else:
                    is_end = True
                    gap_end = -1
                self.figure_init()
                if self.channel != 0:
                    self.ax1.plot(
                        self.time[gap_start:gap_end], self.data[self.sweep][gap_start:gap_end, 0])
                else:
                    self.ax1.plot(
                        self.time[gap_start:gap_end], self.data[self.sweep][gap_start:gap_end])
                self.ax1.set_xlabel('time/s')
                self.ax1.set_ylabel('Current/pA')
                self.canvas1.draw()
                self.gap_initime = self.gap_initime + self.gaptime
                self.is_partview = True
                self.is_view = False
                self.is_view_signal = False

                if is_end:
                    # self.statusBar().showMessage('到达数据末尾')
                    QMessageBox.information(
                        self,
                        self.tr("Warning"),
                        self.tr("End of the data"),
                        QMessageBox.Ok)
            else:
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Time range setup wrong"),
                    QMessageBox.Ok)

    @error
    def previous_view(self):
        # 部分预览数据
        if self.fn == '' and not self.is_read:
            self.statusBar().showMessage(self.tr('No file loaded'))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No filed loaded"),
                QMessageBox.Ok)
            pass
        else:  # self.is_view or (not self.is_view_signal):
            if self.gaptime > 0 and self.gap_initime > 0:
                gap_end = int(self.gap_initime * self.sam)
                gap_start = int((self.gap_initime - self.gaptime) * self.sam)
                if gap_start >= 0:
                    is_end = False
                else:
                    is_end = True
                    gap_start = 0
                self.figure_init()
                if self.channel != 0:
                    self.ax1.plot(
                        self.time[gap_start:gap_end], self.data[self.sweep][gap_start:gap_end, 0])
                else:
                    self.ax1.plot(
                        self.time[gap_start:gap_end], self.data[self.sweep][gap_start:gap_end])
                self.ax1.set_xlabel('time/s')
                self.ax1.set_ylabel('Current/pA')
                self.canvas1.draw()
                self.gap_initime = self.gap_initime - self.gaptime
                self.is_partview = True
                self.is_view = False
                self.is_view_signal = False
                if is_end:
                    QMessageBox.information(
                        self,
                        self.tr("Notice"),
                        self.tr("reach the origin"),
                        QMessageBox.Ok)
            else:
                QMessageBox.information(
                    self,
                    self.tr("Notice"),
                    self.tr("Time range setup wrong"),
                    QMessageBox.Ok)

    @error
    def gap_refresh(self):
        self.gap_initime = self.spinBox_2.value()
        self.gaptime = self.spinBox.value()

    @error
    def sweep_plot_next(self):
        self.sweep += 1
        if self.fn == '' and not self.is_read:
            self.statusBar().showMessage(self.tr('No file loaded'))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No filed loaded"),
                QMessageBox.Ok)
            pass
        elif self.sweeps == 0:
            self.statusBar().showMessage(self.tr('No Sweep...'))
            pass
        elif self.sweep < self.sweeps:

            self.statusBar().showMessage(
                self.tr(
                    'Plot Sweep data: sweep %d' %
                    (self.sweep + 1)))
            self.figure_init()
            self.time = np.arange(
                0, len(self.data[self.sweep]) / self.sam, 1 / self.sam)
            self.time = self.time[0:len(self.data[self.sweep])]
            if self.channel != 0:
                self.ax1.plot(self.time, self.data[self.sweep][:, 0])
            else:
                self.ax1.plot(self.time, self.data[self.sweep])
            self.ax1.set_title('sweep%d' % (self.sweep + 1))
            self.ax1.set_xlabel('time/s')
            self.ax1.set_ylabel('Current/pA')
            self.canvas1.draw()
            self.label_6.setText('%d/%d' % ((self.sweep + 1), (self.sweeps)))
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)

            self.is_partview = False
            self.is_view = True
            self.is_view_signal = False
        else:
            self.sweep = 0
            self.statusBar().showMessage(
                self.tr(
                    'Plot sweep data : sweep %d' %
                    (self.sweep + 1)))
            self.figure_init()
            self.time = np.arange(
                0, len(self.data[self.sweep][:, 0]) / self.sam, 1 / self.sam)
            self.time = self.time[0:len(self.data[self.sweep])]
            if self.channel != 0:
                self.ax1.plot(self.time, self.data[self.sweep][:, 0])
            else:
                self.ax1.plot(self.time, self.data[self.sweep])
            self.ax1.set_title('sweep%d' % (self.sweep + 1))
            self.ax1.set_xlabel('time/s')
            self.ax1.set_ylabel('Current/pA')
            self.canvas1.draw()
            self.label_6.setText('1/%s' % (self.sweeps))
            self.is_partview = False
            self.is_view = True
            self.is_view_signal = False

    @error
    def sweep_plot_previous(self):
        self.sweep -= 1
        if self.fn == '' and not self.is_read:
            self.statusBar().showMessage(self.tr('No file loaded'))
            QMessageBox.information(
                self,
                self.tr("Warning"),
                self.tr("No filed loaded"),
                QMessageBox.Ok)
            pass
        elif self.sweeps == 0:
            self.statusBar().showMessage(self.tr('No Sweep...'))
            pass
        elif self.sweep >= 0:
            self.statusBar().showMessage(
                self.tr(
                    'Plot sweep data : sweep %d' %
                    (self.sweep + 1)))
            self.figure_init()
            self.time = np.arange(
                0, len(self.data[self.sweep]) / self.sam, 1 / self.sam)
            self.time = self.time[0:len(self.data[self.sweep])]
            if self.channel != 0:
                self.ax1.plot(self.time, self.data[self.sweep][:, 0])
            else:
                self.ax1.plot(self.time, self.data[self.sweep])
            self.ax1.set_title('sweep%d' % (self.sweep + 1))
            self.ax1.set_xlabel('time/s')
            self.ax1.set_ylabel('Current/pA')
            self.canvas1.draw()
            self.label_6.setText('%d/%d' % ((self.sweep + 1), (self.sweeps)))
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            self.is_partview = False
            self.is_view = True
            self.is_view_signal = False
        else:
            self.sweep = self.sweeps - 1
            self.statusBar().showMessage(
                self.tr(
                    'Plot sweep data : sweep %d' %
                    (self.sweep + 1)))
            self.figure_init()
            self.time = np.arange(
                0, len(self.data[self.sweep]) / self.sam, 1 / self.sam)
            self.time = self.time[0:len(self.data[self.sweep])]
            if self.channel != 0:
                self.ax1.plot(self.time, self.data[self.sweep][:, 0])
            else:
                self.ax1.plot(self.time, self.data[self.sweep])
            self.ax1.set_title('sweep%d' % (self.sweep + 1))
            self.ax1.set_xlabel('time/s')
            self.ax1.set_ylabel('Current/pA')
            self.canvas1.draw()
            self.label_6.setText('%d/%d' % ((self.sweep + 1), (self.sweeps)))
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            self.is_partview = False
            self.is_view = True
            self.is_view_signal = False

    @error
    def msg(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "Error",
                                        "Error internet connect",
                                        QMessageBox.Yes)


class MovieSplashScreen(QSplashScreen):
    def __init__(self, movie, parent=None):
        QSplashScreen.__init__(self, QPixmap(), QtCore.Qt.WindowStaysOnTopHint)
        self.movie = movie
        self.movie.frameChanged.connect(self.onNextFrame)
        self.movie.start()

    #@QtCore.pyqtSlot()
    @QtCore.Slot()
    def onNextFrame(self):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())


if __name__ == '__main__':
    '''
    主函数
    '''
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    # if os.path.exists('a.ini'):
    #   settings1 = QtCore.QSettings(r'a.ini', QtCore.QSettings.IniFormat)
    #    settings1.beginGroup('window')
    #     settings1.setIniCodec('UTF-8')
    #     langues = settings1.value(r'language')
    # if s1=='zh_CN':
    # chinese = (s1=='zh_CN')
    #    print(langues)

    # else:
    langues = "English"
    # if langues == "zh_CN":
    #    trans = QtCore.QTranslator()
    #   trans.load("zh_CN")
    #   app.installTranslator(trans)
    movie = QMovie(":/img/1.gif")
    splash = MovieSplashScreen(movie)
    splash.show()
    start = time.time()
    mainWindow = Scat_analy(langues=langues)
    while movie.state() == QMovie.Running and time.time() < start + 3:
        app.processEvents()

    mainWindow.show()
    splash.finish(mainWindow)
    sys.exit(app.exec_())
