# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(500, 250)
        about.setMinimumSize(QtCore.QSize(500, 250))
        about.setMaximumSize(QtCore.QSize(500, 250))
        font = QtGui.QFont()
        font.setFamily("Courier")
        about.setFont(font)
        about.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(about)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 91))
        self.label.setStyleSheet("QLabel{\n"
                                 "    image: url(:/img/img2.png);\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(about)
        self.label_2.setGeometry(QtCore.QRect(120, 0, 90, 41))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(about)
        self.label_5.setGeometry(QtCore.QRect(110, 180, 281, 21))
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(about)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 210, 421, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.about_update = QtWidgets.QPushButton(self.layoutWidget)
        self.about_update.setMaximumSize(QtCore.QSize(100, 16777215))
        self.about_update.setStyleSheet(
            "\n"
            "QPushButton{\n"
            "    \n"
            "    \n"
            "    background-color: rgb(222, 222, 222);\n"
            "   \n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
            "{\n"
            "    \n"
            "    \n"
            "    border:none;\n"
            "    \n"
            "    \n"
            "}")
        self.about_update.setObjectName("about_update")
        self.gridLayout.addWidget(self.about_update, 0, 0, 1, 1)
        self.about_help = QtWidgets.QPushButton(self.layoutWidget)
        self.about_help.setMaximumSize(QtCore.QSize(100, 100))
        self.about_help.setStyleSheet(
            "\n"
            "QPushButton{\n"
            "    \n"
            "    \n"
            "    background-color: rgb(222, 222, 222);\n"
            "   \n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
            "{\n"
            "    \n"
            "    \n"
            "    border:none;\n"
            "    \n"
            "    \n"
            "}")
        self.about_help.setObjectName("about_help")
        self.gridLayout.addWidget(self.about_help, 0, 1, 1, 1)
        self.about_close = QtWidgets.QPushButton(self.layoutWidget)
        self.about_close.setMaximumSize(QtCore.QSize(100, 16777215))
        self.about_close.setStyleSheet(
            "\n"
            "QPushButton{\n"
            "    \n"
            "    \n"
            "    background-color: rgb(222, 222, 222);\n"
            "   \n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
            "{\n"
            "    \n"
            "    \n"
            "    border:none;\n"
            "    \n"
            "    \n"
            "}")
        self.about_close.setObjectName("about_close")
        self.gridLayout.addWidget(self.about_close, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(about)
        self.textBrowser.setGeometry(QtCore.QRect(120, 90, 301, 90))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
                                       "    border:0px solid gray;\n"
                                       "}")
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setOpenExternalLinks(False)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget1 = QtWidgets.QWidget(about)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 30, 169, 44))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About"))
        self.label.setText(
            _translate(
                "about",
                "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(
            _translate(
                "about",
                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#0000ff;\">PyNano</span></p></body></html>"))
        self.label_5.setText(
            _translate(
                "about",
                "<html><head/><body><p align=\"center\">Copyright (C) 2019 Decacent </p></body></html>"))
        self.about_update.setText(_translate("about", "Updata"))
        self.about_help.setText(_translate("about", "Help"))
        self.about_close.setText(_translate("about", "Close"))
        self.textBrowser.setHtml(
            _translate(
                "about",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Calibri\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">PyNano is a brief and powerful nano science data analysis software. </span></p></body></html>"))
        self.label_3.setText(
            _translate(
                "about",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Current version：</span></p></body></html>"))
        self.label_4.setText(
            _translate(
                "about",
                "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">2.0</span></p></body></html>"))


import ui.images
