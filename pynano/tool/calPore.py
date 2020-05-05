# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalPore.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow
from sympy import symbols, solve, Eq
from math import pi, sqrt
#from ui import images
from ui.calPore_ui import Ui_CaclNanopore


class Cacl(QMainWindow, Ui_CaclNanopore):
    def __init__(self, parent=None):
        super(Cacl, self).__init__(parent)
        self.setupUi(self)
        self.d0 = 0
        self.textEdit.setText('0')
        self.textEdit_lq.setText('0')
        self.pushButton_11.clicked.connect(self.poresize)
        self.doubleSpinBox_2.editingFinished.connect(self.poresize)
        self.doubleSpinBox_3.editingFinished.connect(self.poresize)
        self.doubleSpinBox_4.editingFinished.connect(self.poresize)
        self.doubleSpinBox_5.editingFinished.connect(self.poresize)
        self.doubleSpinBox_5.editingFinished.connect(self.poresize)
        self.doubleSpinBox_lq.editingFinished.connect(self.poresize)

    def poresize(self):
        try:
            x = self.doubleSpinBox_2.value()
            y = self.doubleSpinBox_3.value()
            m = self.doubleSpinBox_4.value()
            n = self.doubleSpinBox_5.value()

            d = symbols('d')

            a = y / x * (1e-6)
            l = m * (1e-9)
            ss = solve(Eq(n * (4 * l / (pi * (d ** 2)) + 1 / d) ** (-1), a), d)
            if ss == []:
                self.d0 = 0
            else:
                self.d0 = round(ss[-1] * 1000000000, 2)
            self.textEdit.setText(str(self.d0))
            if self.doubleSpinBox_lq.value() > 0:
                d1 = sqrt(self.d0**2 - self.doubleSpinBox_lq.value()**2)
                g0 = n / (4 * m / (pi * (self.d0**2)) + 1 / self.d0)
                g1 = n / (4 * m / (pi * (d1**2)) + 1 / d1)
                i = g1 / g0
                i = round(i, 3)
                self.textEdit_lq.setText(str(i))
        except BaseException:
            pass
