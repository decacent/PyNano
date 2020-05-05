# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tdms_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Read_Tdms(object):
    def setupUi(self, Read_Tdms):
        Read_Tdms.setObjectName("Read_Tdms")
        Read_Tdms.resize(712, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img19.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Read_Tdms.setWindowIcon(icon)
        Read_Tdms.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Read_Tdms)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(70, 25))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 9, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(70, 25))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 13, 1, 1)
        self.plotdata = QtWidgets.QPushButton(self.centralwidget)
        self.plotdata.setMinimumSize(QtCore.QSize(70, 70))
        self.plotdata.setMaximumSize(QtCore.QSize(70, 70))
        self.plotdata.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img43.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img43s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.plotdata.setText("")
        self.plotdata.setObjectName("plotdata")
        self.gridLayout.addWidget(self.plotdata, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 12, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 1)
        self.checkBox_5_tdms = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5_tdms.setMinimumSize(QtCore.QSize(80, 25))
        self.checkBox_5_tdms.setMaximumSize(QtCore.QSize(70, 25))
        self.checkBox_5_tdms.setObjectName("checkBox_5_tdms")
        self.gridLayout.addWidget(self.checkBox_5_tdms, 0, 7, 1, 1)
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setMinimumSize(QtCore.QSize(70, 70))
        self.openfile.setMaximumSize(QtCore.QSize(70, 70))
        self.openfile.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img18.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img17.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.openfile.setText("")
        self.openfile.setObjectName("openfile")
        self.gridLayout.addWidget(self.openfile, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.spinBox_9_tdms = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_9_tdms.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox_9_tdms.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox_9_tdms.setMaximum(999999999)
        self.spinBox_9_tdms.setProperty("value", 0)
        self.spinBox_9_tdms.setObjectName("spinBox_9_tdms")
        self.gridLayout.addWidget(self.spinBox_9_tdms, 0, 15, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 10, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 16, 1, 1)
        self.savedata = QtWidgets.QPushButton(self.centralwidget)
        self.savedata.setMinimumSize(QtCore.QSize(70, 70))
        self.savedata.setMaximumSize(QtCore.QSize(70, 70))
        self.savedata.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img45.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img45s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}url(:/img/img45s.ico)")
        self.savedata.setText("")
        self.savedata.setObjectName("savedata")
        self.gridLayout.addWidget(self.savedata, 0, 5, 1, 1)
        self.spinBox_8_tdms = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_8_tdms.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox_8_tdms.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox_8_tdms.setMaximum(999999999)
        self.spinBox_8_tdms.setObjectName("spinBox_8_tdms")
        self.gridLayout.addWidget(self.spinBox_8_tdms, 0, 11, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 14, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_tdms = QtWidgets.QVBoxLayout()
        self.verticalLayout_tdms.setObjectName("verticalLayout_tdms")
        self.verticalLayout_2.addLayout(self.verticalLayout_tdms)
        Read_Tdms.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Read_Tdms)
        self.statusbar.setObjectName("statusbar")
        Read_Tdms.setStatusBar(self.statusbar)

        self.retranslateUi(Read_Tdms)
        QtCore.QMetaObject.connectSlotsByName(Read_Tdms)

    def retranslateUi(self, Read_Tdms):
        _translate = QtCore.QCoreApplication.translate
        Read_Tdms.setWindowTitle(_translate("Read_Tdms", "MainWindow"))
        self.label.setText(_translate("Read_Tdms", "Start"))
        self.label_2.setText(_translate("Read_Tdms", "End"))
        self.checkBox_5_tdms.setText(_translate("Read_Tdms", "Set Range"))

import ui.images
