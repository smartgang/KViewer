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
        self.setup_range_control_view()
        self.main_child_graph = ChildGraph(False)
        self.second_child_graph = ChildGraph(True)
        self.child_graph_layout.addWidget(self.main_child_graph,stretch=2)
        self.child_graph_layout.addWidget(self.second_child_graph, stretch=2)
        self.child_graph_layout.addWidget(self.range_control_plt, stretch=1)
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

    def setup_range_control_view(self):
        self.range_control_plt = pg.PlotWidget()
        # 下面第2个图的范围设置框
        self.region = pg.LinearRegionItem()
        self.region.setZValue(10)
        self.range_control_plt.addItem(self.region)
        #self.range_control_plt.plot(x=x,y=y, pen="w", name='close')

    def get_setting(self):
        self.setting_dic['contract'] = self.setting_symbol_edit.text()
        self.setting_dic['period'] = int(self.setting_bar_type_cb.currentText())
        self.setting_dic['start_date'] = self.setting_start_date.date().toString("yyyy-MM-dd")
        self.setting_dic['end_date'] = self.setting_end_date.date().toString("yyyy-MM-dd")
        self.raw_data = pd.read_csv('RB1810_2018-06-19_1m.csv')
        self.main_child_graph.set_raw_data(self.raw_data)
        self.second_child_graph.set_raw_data(self.raw_data)
        self.range_control_plt.plot(self.raw_data['close'], pen="w", name='close')
        self.main_child_graph.plt.setXLink(self.second_child_graph.plt)
        self.region.sigRegionChanged.connect(self.set_child_range)
        print ('update_region')
        self.main_child_graph.plt.sigRangeChanged.connect(self.update_region)
        print ('set region')
        self.region.setRegion([0, 100])
        #self.main_child_graph.plt.setYLink(self.second_child_graph.plt)
        pass

    def set_child_range(self):
        #self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.main_child_graph.update_visual_range(int(minX), int(maxX))

    def update_region(self,window, viewRange):
        rgn = viewRange[0]
        self.region.setRegion(rgn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = KViewer()
    demo.show()
    sys.exit(app.exec_())