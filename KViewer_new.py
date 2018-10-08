# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Indexer import *
import pyqtgraph as pg
import pandas as pd
from ChildGraph import ChildGraph
class KViewer(QWidget):

    def __init__(self,):
        super(KViewer, self).__init__()
        self.main_layout = QVBoxLayout(self)
        self.child_graph_layout = QVBoxLayout(self)
        self.setting_dic = {}
        self.setup_ui()
        self.main_child_graph = ChildGraph(False)
        self.child_graph_layout.addWidget(self.main_child_graph,stretch=2)
        self.main_layout.addLayout(self.setting_layout)
        self.main_layout.addLayout(self.child_graph_layout)
        self.setLayout(self.main_layout)

    def setup_ui(self):
        self.setup_ui_header()


    def setup_ui_header(self):
        self.setting_layout = QHBoxLayout(self)
        self.setting_layout.addWidget(QLabel('合约'))
        self.setting_symbol_edit = QLineEdit()
        self.setting_layout.addWidget(self.setting_symbol_edit)
        self.setting_layout.addWidget(QLabel('周期'))
        self.setting_bar_type_cb = QComboBox()
        self.setting_bar_type_cb.addItems(['0','60','300','600','900','1800','3600'])
        self.setting_layout.addWidget(self.setting_bar_type_cb)
        self.setting_start_date = QDateEdit()
        self.setting_start_date.setDisplayFormat("yyyy-MM-dd")
        self.setting_end_date = QDateEdit()
        self.setting_end_date.setDisplayFormat("yyyy-MM-dd")
        self.setting_layout.addWidget(QLabel('开始日期'))
        self.setting_layout.addWidget(self.setting_start_date)
        self.setting_layout.addWidget(QLabel('结束日期'))
        self.setting_layout.addWidget(self.setting_end_date)
        self.setting_view_btn = QPushButton('显示')
        self.setting_view_btn.clicked.connect(self.get_setting)
        self.setting_layout.addWidget(self.setting_view_btn)

    def get_setting(self):
        self.setting_dic['contract'] = self.setting_symbol_edit.text()
        self.setting_dic['period'] = int(self.setting_bar_type_cb.currentText())
        self.setting_dic['start_date'] = self.setting_start_date.date().toString("yyyy-MM-dd")
        self.setting_dic['end_date'] = self.setting_end_date.date().toString("yyyy-MM-dd")
        print (self.setting_dic)
        self.main_child_graph.set_raw_data(1)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = KViewer()
    demo.show()
    sys.exit(app.exec_())