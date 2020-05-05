# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuck_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Fuck(object):
    def setupUi(self, Fuck):
        Fuck.setObjectName("Fuck")
        Fuck.resize(320, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Fuck.sizePolicy().hasHeightForWidth())
        Fuck.setSizePolicy(sizePolicy)
        Fuck.setMinimumSize(QtCore.QSize(320, 230))
        Fuck.setMaximumSize(QtCore.QSize(320, 230))
        self.verticalLayout = QtWidgets.QVBoxLayout(Fuck)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Fuck)
        self.textBrowser.setStyleSheet("background-color: rgb(240, 240, 240); \n"
"border:0px solid gray;")
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(Fuck)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 50))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Fuck)
        QtCore.QMetaObject.connectSlotsByName(Fuck)

    def retranslateUi(self, Fuck):
        _translate = QtCore.QCoreApplication.translate
        Fuck.setWindowTitle(_translate("Fuck", "Dialog"))
        self.pushButton_2.setText(_translate("Fuck", "Quit"))

