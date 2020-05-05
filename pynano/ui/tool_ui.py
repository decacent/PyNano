# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_toolbox(object):
    def setupUi(self, toolbox):
        toolbox.setObjectName("toolbox")
        toolbox.resize(908, 661)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img46.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        toolbox.setWindowIcon(icon)
        toolbox.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(toolbox)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_tool = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_tool.sizePolicy().hasHeightForWidth())
        self.widget_tool.setSizePolicy(sizePolicy)
        self.widget_tool.setMinimumSize(QtCore.QSize(120, 0))
        self.widget_tool.setMaximumSize(QtCore.QSize(120, 16777215))
        self.widget_tool.setStyleSheet("background-color: rgba(52, 152, 219, 50);")
        self.widget_tool.setObjectName("widget_tool")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_tool)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.poresize = QtWidgets.QPushButton(self.widget_tool)
        self.poresize.setMinimumSize(QtCore.QSize(90, 90))
        self.poresize.setMaximumSize(QtCore.QSize(90, 90))
        self.poresize.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img47.ico);\n"
"    \n"
"    border:none;\n"
"background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img47s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.poresize.setObjectName("poresize")
        self.gridLayout_2.addWidget(self.poresize, 0, 0, 1, 1)
        self.tdms = QtWidgets.QPushButton(self.widget_tool)
        self.tdms.setMinimumSize(QtCore.QSize(90, 90))
        self.tdms.setMaximumSize(QtCore.QSize(90, 90))
        self.tdms.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img47.ico);\n"
"    border:none;\n"
"    \n"
"background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img47s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.tdms.setObjectName("tdms")
        self.gridLayout_2.addWidget(self.tdms, 1, 0, 1, 1)
        self.emd = QtWidgets.QPushButton(self.widget_tool)
        self.emd.setMinimumSize(QtCore.QSize(90, 90))
        self.emd.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.emd.setFont(font)
        self.emd.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img47.ico);\n"
"    \n"
"    border:none;\n"
"background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img47s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.emd.setObjectName("emd")
        self.gridLayout_2.addWidget(self.emd, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_tool, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_tool = QtWidgets.QVBoxLayout()
        self.verticalLayout_tool.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_tool.setSpacing(0)
        self.verticalLayout_tool.setObjectName("verticalLayout_tool")
        self.horizontalLayout.addLayout(self.verticalLayout_tool)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        toolbox.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(toolbox)
        self.statusbar.setObjectName("statusbar")
        toolbox.setStatusBar(self.statusbar)

        self.retranslateUi(toolbox)
        QtCore.QMetaObject.connectSlotsByName(toolbox)

    def retranslateUi(self, toolbox):
        _translate = QtCore.QCoreApplication.translate
        toolbox.setWindowTitle(_translate("toolbox", "MainWindow"))
        self.poresize.setText(_translate("toolbox", "CaclPore"))
        self.tdms.setText(_translate("toolbox", "Read\nTDMS"))
        self.emd.setText(_translate("toolbox", "EMD"))

import ui.images