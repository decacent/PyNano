# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalPore.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaclNanopore(object):
    def setupUi(self, CaclNanopore):
        CaclNanopore.setObjectName("CaclNanopore")
        CaclNanopore.resize(400, 400)
        CaclNanopore.setMinimumSize(QtCore.QSize(400, 400))
        CaclNanopore.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        CaclNanopore.setFont(font)
        CaclNanopore.setStyleSheet("background-color: rgb(166, 206, 232);")
        self.centralwidget = QtWidgets.QWidget(CaclNanopore)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 250, 80, 80))
        self.pushButton_11.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_11.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(
            "QPushButton\n"
            "\n"
            "{ image: url(:/img/img47.ico);\n"
            "    border:none;\n"
            "    \n"
            "    background-color: rgba(230, 126, 34,0);\n"
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
        self.pushButton_11.setObjectName("pushButton_11")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 70, 70, 40))
        self.textEdit.setMinimumSize(QtCore.QSize(70, 40))
        self.textEdit.setMaximumSize(QtCore.QSize(70, 40))
        self.textEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 15pt \"Times New Roman\";")
        self.textEdit.setObjectName("textEdit")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(290, 40, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(52, 152, 219, 0);")
        self.label_14.setObjectName("label_14")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(52, 152, 219, 0);")
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 251, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setMinimumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_3.setMaximumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_3.setMaximum(100000.0)
        self.doubleSpinBox_3.setSingleStep(10.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_2.addWidget(self.doubleSpinBox_3, 1, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_5.setMinimumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_5.setMaximumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_5.setProperty("value", 10.5)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(120, 25))
        self.label_10.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(120, 25))
        self.label_11.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_4.setMinimumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_4.setMaximumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_4.setMaximum(50.0)
        self.doubleSpinBox_4.setProperty("value", 3.7)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(120, 25))
        self.label_13.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setEnabled(True)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_2.setMaximumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_2.setMaximum(1000.0)
        self.doubleSpinBox_2.setSingleStep(50.0)
        self.doubleSpinBox_2.setProperty("value", 100.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_2.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(120, 25))
        self.label_12.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(120, 25))
        self.label.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.doubleSpinBox_lq = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_lq.setMinimumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_lq.setMaximumSize(QtCore.QSize(70, 30))
        self.doubleSpinBox_lq.setObjectName("doubleSpinBox_lq")
        self.gridLayout_2.addWidget(self.doubleSpinBox_lq, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 130, 70, 25))
        self.label_2.setMinimumSize(QtCore.QSize(70, 25))
        self.label_2.setMaximumSize(QtCore.QSize(70, 25))
        self.label_2.setObjectName("label_2")
        self.textEdit_lq = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_lq.setGeometry(QtCore.QRect(290, 160, 70, 40))
        self.textEdit_lq.setMinimumSize(QtCore.QSize(70, 40))
        self.textEdit_lq.setMaximumSize(QtCore.QSize(70, 40))
        self.textEdit_lq.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 15pt \"Times New Roman\";")
        self.textEdit_lq.setObjectName("textEdit_lq")
        self.label_tex = QtWidgets.QLabel(self.centralwidget)
        self.label_tex.setGeometry(QtCore.QRect(100, 340, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_tex.setFont(font)
        self.label_tex.setObjectName("label_tex")
        CaclNanopore.setCentralWidget(self.centralwidget)

        self.retranslateUi(CaclNanopore)
        QtCore.QMetaObject.connectSlotsByName(CaclNanopore)

    def retranslateUi(self, CaclNanopore):
        _translate = QtCore.QCoreApplication.translate
        CaclNanopore.setWindowTitle(_translate("CaclNanopore", "MainWindow"))
        self.pushButton_11.setText(_translate("CaclNanopore", "Run"))
        self.textEdit.setHtml(
            _translate(
                "CaclNanopore",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:18pt; color:#000000;\">15</span></p></body></html>"))
        self.label_14.setText(
            _translate(
                "CaclNanopore",
                "<html><head/><body><p>Diameter/nm</p></body></html>"))
        self.label_9.setText(
            _translate(
                "CaclNanopore",
                "<html><head/><body><p><span style=\" font-size:10pt;\">Caculate the pore size of solid state nanopore</span></p></body></html>"))
        self.label_10.setText(_translate("CaclNanopore", "Voltage/mv"))
        self.label_11.setText(
            _translate(
                "CaclNanopore",
                "<html><head/><body><p>Current/nA</p></body></html>"))
        self.label_13.setText(_translate("CaclNanopore", "Conductivity"))
        self.label_12.setText(_translate("CaclNanopore", "Thickness/nm"))
        self.label.setText(
            _translate(
                "CaclNanopore",
                "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Analyte DIA/nm</span></p></body></html>"))
        self.label_2.setText(
            _translate(
                "CaclNanopore",
                "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">I/I0</span></p></body></html>"))
        self.textEdit_lq.setHtml(
            _translate(
                "CaclNanopore",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_tex.setText(
            _translate(
                "CaclNanopore",
                "<html><head/><body><p><span style=\" font-family:\'Calibri\'; font-size:20pt; font-style:italic;\">G=σ[4l/πd</span><span style=\" font-family:\'Calibri\'; font-size:20pt; font-style:italic; vertical-align:super;\">2</span><span style=\" font-family:\'Calibri\'; font-size:20pt; font-style:italic;\">+1/d]</span><span style=\" font-family:\'Calibri\'; font-size:20pt; font-style:italic; vertical-align:super;\">-1</span></p></body></html>"))


import ui.images
