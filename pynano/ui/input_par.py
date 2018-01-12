# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_par.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 350)
        Dialog.setMinimumSize(QtCore.QSize(305, 350))
        Dialog.setMaximumSize(QtCore.QSize(305, 350))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(165, 270, 70, 70))
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    \n"
"    image: url(:/img/img32.ico);\n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    \n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 270, 70, 70))
        self.pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{\n"
"    \n"
" image: url(:/img/img29.ico);\n"
"    \n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img29s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 261, 223))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_sam = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_sam.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox_sam.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox_sam.setMaximum(250000)
        self.spinBox_sam.setProperty("value", 100000)
        self.spinBox_sam.setObjectName("spinBox_sam")
        self.gridLayout.addWidget(self.spinBox_sam, 1, 1, 1, 1)
        self.checkBox_resam = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_resam.setMinimumSize(QtCore.QSize(90, 30))
        self.checkBox_resam.setMaximumSize(QtCore.QSize(90, 30))
        self.checkBox_resam.setObjectName("checkBox_resam")
        self.gridLayout.addWidget(self.checkBox_resam, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setMinimumSize(QtCore.QSize(90, 30))
        self.radioButton_3.setMaximumSize(QtCore.QSize(90, 30))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 0, 1, 1)
        self.doubleSpinBox_base = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_base.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_base.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_base.setDecimals(4)
        self.doubleSpinBox_base.setMinimum(-1e+29)
        self.doubleSpinBox_base.setMaximum(1e+26)
        self.doubleSpinBox_base.setObjectName("doubleSpinBox_base")
        self.gridLayout.addWidget(self.doubleSpinBox_base, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 25))
        self.label_2.setMaximumSize(QtCore.QSize(120, 25))
        self.label_2.setStyleSheet("background-color: rgba(52, 152, 219, 0);\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setMinimumSize(QtCore.QSize(90, 30))
        self.radioButton_4.setMaximumSize(QtCore.QSize(90, 30))
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 25))
        self.label_5.setMaximumSize(QtCore.QSize(100, 25))
        self.label_5.setStyleSheet("background-color: rgba(52, 152, 219, 0);\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.spinBox_endnum = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_endnum.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox_endnum.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox_endnum.setMaximum(99999999)
        self.spinBox_endnum.setProperty("value", 50)
        self.spinBox_endnum.setObjectName("spinBox_endnum")
        self.gridLayout.addWidget(self.spinBox_endnum, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(120, 25))
        self.label_3.setMaximumSize(QtCore.QSize(120, 25))
        self.label_3.setStyleSheet("background-color: rgba(52, 152, 219, 0);\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.doubleSpinBox_endth = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_endth.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_endth.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_endth.setMaximum(9999999999.0)
        self.doubleSpinBox_endth.setObjectName("doubleSpinBox_endth")
        self.gridLayout.addWidget(self.doubleSpinBox_endth, 3, 1, 1, 1)
        self.spinBox_basenum = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_basenum.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox_basenum.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox_basenum.setMaximum(99999999)
        self.spinBox_basenum.setProperty("value", 500)
        self.spinBox_basenum.setObjectName("spinBox_basenum")
        self.gridLayout.addWidget(self.spinBox_basenum, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(100, 25))
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        self.label_4.setStyleSheet("background-color: rgba(52, 152, 219, 0);\n"
"")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 278, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_1.setMinimumSize(QtCore.QSize(70, 25))
        self.label_1.setMaximumSize(QtCore.QSize(70, 25))
        self.label_1.setStyleSheet("background-color: rgba(52, 152, 219, 0);\n"
"")
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox_baseline = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_baseline.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_baseline.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_baseline.setDecimals(4)
        self.doubleSpinBox_baseline.setMinimum(-1e+21)
        self.doubleSpinBox_baseline.setMaximum(1e+17)
        self.doubleSpinBox_baseline.setObjectName("doubleSpinBox_baseline")
        self.gridLayout_2.addWidget(self.doubleSpinBox_baseline, 0, 1, 1, 1)
        self.doubleSpinBox_th = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_th.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_th.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_th.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_th.setDecimals(4)
        self.doubleSpinBox_th.setMaximum(5000.0)
        self.doubleSpinBox_th.setObjectName("doubleSpinBox_th")
        self.gridLayout_2.addWidget(self.doubleSpinBox_th, 0, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox_resam.setText(_translate("Dialog", "resample"))
        self.radioButton_3.setText(_translate("Dialog", "downwards"))
        self.label_2.setText(_translate("Dialog", "Signal Threshold"))
        self.radioButton_4.setText(_translate("Dialog", "upwards"))
        self.label_5.setText(_translate("Dialog", "Terminal Param"))
        self.label_3.setText(_translate("Dialog", "Terminal Threshold"))
        self.label_4.setText(_translate("Dialog", "BaseLine Param"))
        self.label_1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Noise(RMS)</p></body></html>"))
        self.label.setText(_translate("Dialog", "BaseLine"))

import ui.images
