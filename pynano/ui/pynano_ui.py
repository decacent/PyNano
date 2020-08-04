# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        mainWindow.resize(1179, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAnimated(False)
        mainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(180, 0))
        self.widget.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: rgba(52, 152, 219, 100);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_6.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_6.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img35.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img35s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(52, 152, 219, 0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(95, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"image: url(:/img/img11.ico);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img29.ico);\n"
"    \n"
"    border:none;\n"
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
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setStyleSheet("QPushButton\n"
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
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_7.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_7.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img45.ico);\n"
"    \n"
"    border:none;\n"
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
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 7, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_8.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img46.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img46s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 7, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img18.ico);\n"
"    border:none;\n"
"    \n"
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
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(70, 25))
        self.label.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(52, 152, 219, 0);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox.setStyleSheet(" \n"
"QDoubleSpinBox {\n"
"    background-color: rgba(52, 152, 219, 0);\n"
"    border: 1px solid blue;\n"
"    border-radius: 5px;\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMaximum(999999999999.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 4, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_4.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img44.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img44s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_2.setMaximumSize(QtCore.QSize(70, 25))
        self.doubleSpinBox_2.setStyleSheet(" \n"
"QDoubleSpinBox {\n"
"    background-color: rgba(52, 152, 219, 0);\n"
"    border: 1px solid blue;\n"
"    border-radius: 5px;\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setMaximum(999999999999.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 5, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setMinimumSize(QtCore.QSize(130, 25))
        self.checkBox.setMaximumSize(QtCore.QSize(130, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox {\n"
"    background-color: rgba(52, 152, 219, 0);\n"
"    spacing: 5px;\n"
"    \n"
"    font: 9pt \"Arial\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    \n"
"    \n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    \n"
"    image: url(:/img/img32.ico);\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/img29s.ico);\n"
"}\n"
"\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_5.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img33.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img33s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 6, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.widget)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setStyleSheet("background-color: #F0F0F0;")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(15)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 0px solid #C2C7CB;\n"
"\n"
"\n"
"    \n"
"}\n"
"QTabWidget{ /* The tab widget frame */\n"
" \n"
"    background-color: rgb(237, 212, 0);\n"
"\n"
"\n"
"    \n"
"}\n"
"QTabBar::tab {\n"
"\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background-color: rgba(0, 170, 255,100);\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setMinimumSize(QtCore.QSize(75, 25))
        self.label_10.setMaximumSize(QtCore.QSize(75, 25))
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 9, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setMinimumSize(QtCore.QSize(75, 25))
        self.label_7.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(50, 30))
        self.label_3.setMaximumSize(QtCore.QSize(50, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMinimumSize(QtCore.QSize(50, 25))
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAccessibleName("")
        self.label_5.setAccessibleDescription("")
        self.label_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 6, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox.setStyleSheet(" \n"
"QSpinBox {\n"
"    background-color: rgba(52, 152, 219, 0);\n"
"    border: 1px solid blue;\n"
"    border-radius: 5px;\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_11.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_11.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ \n"
"    \n"
"    image: url(:/img/img36.ico);\n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"\n"
"    \n"
"    image: url(:/img/img47s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 0, 4, 2, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_12.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_12.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ \n"
"    image: url(:/img/img42.ico);\n"
"    border:none;\n"
"    \n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"\n"
"    \n"
"    \n"
"    image: url(:/img/img42s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 0, 5, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setMinimumSize(QtCore.QSize(75, 25))
        self.label_8.setMaximumSize(QtCore.QSize(75, 25))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 7, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_2.setMinimumSize(QtCore.QSize(70, 25))
        self.spinBox_2.setMaximumSize(QtCore.QSize(70, 25))
        self.spinBox_2.setStyleSheet(" \n"
"QSpinBox {\n"
"    background-color: rgba(52, 152, 219, 0);\n"
"    border: 1px solid blue;\n"
"    border-radius: 5px;\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_10.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_10.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img35.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img35s.ico);\n"
"    \n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 0, 3, 2, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img33.ico);\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img33s.ico);\n"
"    \n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 0, 2, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setMinimumSize(QtCore.QSize(75, 25))
        self.label_9.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 9, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMinimumSize(QtCore.QSize(50, 25))
        self.label_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 6, 1, 1)
        self.label_samp = QtWidgets.QLabel(self.tab)
        self.label_samp.setMinimumSize(QtCore.QSize(75, 25))
        self.label_samp.setMaximumSize(QtCore.QSize(75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_samp.setFont(font)
        self.label_samp.setObjectName("label_samp")
        self.gridLayout_2.addWidget(self.label_samp, 0, 8, 1, 1)
        self.label_sample_rate = QtWidgets.QLabel(self.tab)
        self.label_sample_rate.setObjectName("label_sample_rate")
        self.gridLayout_2.addWidget(self.label_sample_rate, 1, 8, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.tab_2, "")
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_2 = QtWidgets.QSplitter(self.widget_2)
        self.splitter_2.setLineWidth(1)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setHandleWidth(6)
        self.splitter_2.setChildrenCollapsible(True)
        self.splitter_2.setObjectName("splitter_2")
        self.widget_2s1 = QtWidgets.QWidget(self.splitter_2)
        self.widget_2s1.setObjectName("widget_2s1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2s1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2s1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(40, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(55, 16777215))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 1px;\n"
"    min-width: 3em;    \n"
"    \n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"image: url(:/img/img11.ico);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::item { /* shift the text when the popup opens */\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_11 = QtWidgets.QLabel(self.widget_2s1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(45, 0))
        self.label_11.setMaximumSize(QtCore.QSize(45, 25))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget_2s1)
        self.spinBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_3.setStyleSheet(" \n"
"QSpinBox {\n"
"    border: 1px solid blue;\n"
"    border-radius: 1px;\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.spinBox_3.setMinimum(-1000000000)
        self.spinBox_3.setMaximum(1000000000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.double_SpinBox_4 = QtWidgets.QDoubleSpinBox(self.widget_2s1)
        self.double_SpinBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.double_SpinBox_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.double_SpinBox_4.setStyleSheet(" \n"
"QDoubleSpinBox {\n"
"    border: 1px solid blue;\n"
"    border-radius: 1px;\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.double_SpinBox_4.setMaximum(999999999.0)
        self.double_SpinBox_4.setObjectName("double_SpinBox_4")
        self.horizontalLayout.addWidget(self.double_SpinBox_4)
        self.label_12 = QtWidgets.QLabel(self.widget_2s1)
        self.label_12.setMinimumSize(QtCore.QSize(30, 0))
        self.label_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.spinBox_5 = QtWidgets.QSpinBox(self.widget_2s1)
        self.spinBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_5.setStyleSheet(" \n"
"QSpinBox {\n"
"    border: 1px solid blue;\n"
"    border-radius: 1px;\n"
"\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.spinBox_5.setMaximum(1000)
        self.spinBox_5.setProperty("value", 150)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout.addWidget(self.spinBox_5)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_2s1)
        self.pushButton_13.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_13.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_13.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ \n"
"    image: url(:/img/img42.ico);\n"
"    border:none;\n"
"    \n"
"    \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"\n"
"    \n"
"    image: url(:/img/img42s.ico);\n"
"    \n"
"    \n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.widget_2s2 = QtWidgets.QWidget(self.splitter_2)
        self.widget_2s2.setObjectName("widget_2s2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_2s2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.widget_2s2)
        self.label_13.setMinimumSize(QtCore.QSize(40, 0))
        self.label_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.spinBox_6 = QtWidgets.QSpinBox(self.widget_2s2)
        self.spinBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_6.setStyleSheet(" \n"
"QSpinBox {\n"
"    border: 1px solid blue;\n"
"    border-radius: 1px;\n"
"\n"
"    border-image: url(:/images/frame.png) 4;\n"
"    \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; /* position at the top right corner */\n"
"\n"
"    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"    \n"
"    border-image: url(:/img/img37.ico);\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; /* position at bottom right corner */\n"
"\n"
"    width: 16px;\n"
"    \n"
"    border-image: url(:/img/img9.ico);\n"
"   \n"
"    border-top-width: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.spinBox_6.setProperty("value", 3)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_2.addWidget(self.spinBox_6)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_2s2)
        self.comboBox_3.setMinimumSize(QtCore.QSize(40, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 1px;\n"
"    min-width: 3em;    \n"
"    \n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"image: url(:/img/img11.ico);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::item { /* shift the text when the popup opens */\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_2s2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_14.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ \n"
"    \n"
"    image: url(:/img/img60.png);\n"
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
"\n"
"    \n"
"    \n"
"    image: url(:/img/img60s.png);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.widget_4 = QtWidgets.QWidget(self.splitter_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_17.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_17.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ image: url(:/img/img45.ico);\n"
"    \n"
"    border:none;\n"
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
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_6.addWidget(self.pushButton_17, 0, 5, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_16.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_16.setStyleSheet("QPushButton\n"
"\n"
"\n"
"{ \n"
"    \n"
"    image: url(:/img/img36.ico);\n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"\n"
"    \n"
"    image: url(:/img/img47s.ico);\n"
"    \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_6.addWidget(self.pushButton_16, 0, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_15.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_15.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img29.ico);\n"
"    \n"
"    border:none;\n"
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
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_6.addWidget(self.pushButton_15, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 0, 4, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.horizontalLayout_3.addWidget(self.splitter)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(30, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.widget_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet("QWidget {\n"
"    \n"
"    border-left: 2px solid grey;\n"
"\n"
"   \n"
"  \n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_18 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QtCore.QSize(30, 150))
        self.pushButton_18.setMaximumSize(QtCore.QSize(30, 150))
        self.pushButton_18.setStyleSheet("\n"
"QPushButton\n"
"\n"
"\n"
"{ \n"
"    image: url(:/img/img61.png);\n"
"    \n"
"    \n"
"    border: 2px solid rgba(230, 126, 34,0); \n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"\n"
"    \n"
"    \n"
"    image: url(:/img/img61.png);\n"
"    \n"
"    border: none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(False)
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_10.addWidget(self.pushButton_18, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_19 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMinimumSize(QtCore.QSize(30, 150))
        self.pushButton_19.setMaximumSize(QtCore.QSize(30, 150))
        self.pushButton_19.setStyleSheet("QPushButton\n"
"\n"
"{ image: url(:/img/img62.png);\n"
"     \n"
"    border: 2px solid rgba(230, 126, 34,0);\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"\n"
"    \n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    image: url(:/img/img62.png);\n"
"     \n"
"    border:none;\n"
"    background-color: rgba(230, 126, 34,0);\n"
"    \n"
"}")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_10.addWidget(self.pushButton_19, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 440, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem7)
        self.pushButton_19.raise_()
        self.pushButton_18.raise_()
        self.horizontalLayout_3.addWidget(self.widget_3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "PyNano"))
        self.pushButton_6.setToolTip(_translate("mainWindow", "Next sweep"))
        self.label_2.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">end</span></p></body></html>"))
        self.comboBox.setToolTip(_translate("mainWindow", "Select analysis model"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Model 1 (vabration)"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Model 2 (Faraday)"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Model 3 (nanopore)"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Model 4 (mutl_peak)"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Model 5 (mutl_cluster)"))
        self.comboBox.setItemText(5, _translate("mainWindow", "Model 6 (pointSaltation)"))
        self.comboBox.setItemText(6, _translate("mainWindow", "Model 7 (adept2state)"))
        self.pushButton_3.setToolTip(_translate("mainWindow", "Start analysis"))
        self.pushButton_2.setToolTip(_translate("mainWindow", "Preview data"))
        self.pushButton_7.setToolTip(_translate("mainWindow", "Save result"))
        self.pushButton_8.setToolTip(_translate("mainWindow", "About"))
        self.pushButton.setToolTip(_translate("mainWindow", "Open Abf file"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">start</span></p></body></html>"))
        self.pushButton_4.setToolTip(_translate("mainWindow", "Preview result"))
        self.checkBox.setToolTip(_translate("mainWindow", "Set analysis range"))
        self.checkBox.setText(_translate("mainWindow", "Select Range"))
        self.pushButton_5.setToolTip(_translate("mainWindow", "Previous seep"))
        self.label_10.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_7.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Voltage</p></body></html>"))
        self.label_3.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Gap</p></body></html>"))
        self.label_5.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Sweep</p></body></html>"))
        self.label_4.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Origin</p></body></html>"))
        self.pushButton_11.setToolTip(_translate("mainWindow", "update view"))
        self.pushButton_12.setToolTip(_translate("mainWindow", "Plot all point hist"))
        self.label_8.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">0mv</p></body></html>"))
        self.pushButton_10.setToolTip(_translate("mainWindow", "Next part view"))
        self.pushButton_9.setToolTip(_translate("mainWindow", "Previous part view"))
        self.label_9.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Events</p></body></html>"))
        self.label_6.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.label_samp.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Sample Rate</p></body></html>"))
        self.label_sample_rate.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">100k</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Tool box"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "current"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "time"))
        self.comboBox_2.setItemText(2, _translate("mainWindow", "I/I0"))
        self.comboBox_2.setItemText(3, _translate("mainWindow", "△I"))
        self.comboBox_2.setItemText(4, _translate("mainWindow", "charge"))
        self.label_11.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Range</p></body></html>"))
        self.label_12.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Bins</p></body></html>"))
        self.pushButton_13.setToolTip(_translate("mainWindow", "Plot hist"))
        self.label_13.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\">Size</p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "current"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "I/I0"))
        self.comboBox_3.setItemText(2, _translate("mainWindow", "△I"))
        self.pushButton_14.setToolTip(_translate("mainWindow", "Plot scattering"))
        self.pushButton_17.setToolTip(_translate("mainWindow", "save markov result"))
        self.pushButton_16.setToolTip(_translate("mainWindow", "update markov stage"))
        self.pushButton_15.setToolTip(_translate("mainWindow", "Markov analysis"))
        self.pushButton_18.setToolTip(_translate("mainWindow", "Result panel"))
        self.pushButton_19.setToolTip(_translate("mainWindow", "Markov analysis panel"))

import ui.images