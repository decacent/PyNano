# -*- coding: utf-8 -*-
"""


@author: Wnight
"""
from ui.tool_ui import *
from PyQt5.QtWidgets import QMainWindow
from tool.calPore import Cacl
from tool.tdms import Tdms_read


class Analy_tool(QMainWindow, Ui_toolbox):
    def __init__(self, parent=None):
        super(Analy_tool, self).__init__(parent)
        self.setupUi(self)
        self.statusBar().showMessage("Ready")

        self.window1 = Cacl()
        self.window2 = Tdms_read()
        self.caclpore_window()
        self.poresize.clicked.connect(self.caclpore_window)
        self.tdms.clicked.connect(self.tdms_window)

    def caclpore_window(self):
        self.window2.close()
        self.verticalLayout_tool.addWidget(self.window1)
        self.window1.show()
        self.statusBar().showMessage("计算孔径")

    def tdms_window(self):
        self.window1.close()
        self.verticalLayout_tool.addWidget(self.window2)
        self.window2.show()
        self.statusBar().showMessage("读取TDMS")
