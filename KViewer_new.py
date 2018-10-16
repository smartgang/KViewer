# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Indexer import *
import pyqtgraph as pg
import pandas as pd
from ChildGraph import ChildGraph
import DataInterface.DataInterface as DI


class KViewer(QWidget):

    def __init__(self,):
        super(KViewer, self).__init__()
        self.raw_data = None
        self.main_layout = QVBoxLayout(self)
        self.setting_layout = QHBoxLayout(self)
        self.child_graph_layout = QVBoxLayout(self)
        self.region = pg.LinearRegionItem()
        self.region_minx = 0  # region控制框的宽度
        self.region_maxx = 0
        self.range_control_plt = pg.PlotWidget()
        self.setting_view_btn = QPushButton('显示')
        self.setting_add_child_btn = QPushButton('增加子图')
        self.setting_remove_child_btn = QPushButton('删除子图')
        self.setting_end_date = QDateEdit()
        self.setting_start_date = QDateEdit()
        self.setting_bar_type_cb = QComboBox()
        self.setting_symbol_edit = QLineEdit()  # 品种
        self.setting_exchange_cb = QComboBox()
        #self.setting_exchange_edit = QLineEdit()    # 交易所
        self.setting_contract_edit = QLineEdit()    # 合约
        self.setting_dic = {}
        self.setup_ui()
        self.setup_range_control_view()
        self.main_child_graph = ChildGraph(False)
        self.main_child_graph.main_child_plt_changed.connect(self.main_child_plt_changed)
        self.child_graph_list = []
        second_child_graph = ChildGraph(True)
        self.child_graph_list.append(second_child_graph)
        self.child_graph_layout.addWidget(self.main_child_graph,stretch=2)
        self.child_graph_layout.addWidget(second_child_graph, stretch=2)
        self.child_graph_layout.addWidget(self.range_control_plt, stretch=1)
        self.main_layout.addLayout(self.setting_layout)
        self.main_layout.addLayout(self.child_graph_layout)
        self.setLayout(self.main_layout)

    def setup_ui(self):
        self.setup_ui_header()

    def setup_ui_header(self):
        self.setting_layout.addWidget(QLabel('交易所'))
        self.setting_exchange_cb.addItems(['SHFE', 'DCE', 'CZCE', 'CFFEX'])
        self.setting_layout.addWidget(self.setting_exchange_cb)
        #self.setting_layout.addWidget(self.setting_exchange_edit)
        self.setting_layout.addWidget(QLabel('品种'))
        self.setting_layout.addWidget(self.setting_symbol_edit)
        self.setting_layout.addWidget(QLabel('合约'))
        self.setting_layout.addWidget(self.setting_contract_edit)
        self.setting_layout.addWidget(QLabel('周期'))
        self.setting_bar_type_cb.addItems(['0','60','300','600','900','1800','3600'])
        self.setting_layout.addWidget(self.setting_bar_type_cb)
        self.setting_start_date.setDisplayFormat("yyyy-MM-dd")
        self.setting_end_date.setDisplayFormat("yyyy-MM-dd")
        self.setting_layout.addWidget(QLabel('开始日期'))
        self.setting_layout.addWidget(self.setting_start_date)
        self.setting_layout.addWidget(QLabel('结束日期'))
        self.setting_layout.addWidget(self.setting_end_date)
        self.setting_view_btn.clicked.connect(self.get_setting)
        self.setting_layout.addWidget(self.setting_view_btn)
        self.setting_layout.addWidget(self.setting_add_child_btn)
        self.setting_layout.addWidget(self.setting_remove_child_btn)
        self.setting_add_child_btn.clicked.connect(self.add_child_graph)
        self.setting_remove_child_btn.clicked.connect(self.remove_child_graph)

    def setup_range_control_view(self):
        # 下面第2个图的范围设置框
        self.region.setZValue(10)
        self.range_control_plt.addItem(self.region)
        #self.range_control_plt.plot(x=x,y=y, pen="w", name='close')

    def get_setting(self):
        exchange = self.setting_exchange_cb.currentText()
        symbol = self.setting_symbol_edit.text()
        contract = self.setting_contract_edit.text()
        bar_type = int(self.setting_bar_type_cb.currentText())
        start_date = self.setting_start_date.date().toString("yyyy-MM-dd")
        end_date = self.setting_end_date.date().toString("yyyy-MM-dd")
        self.setting_dic['exchange'] = exchange
        self.setting_dic['symbol'] = symbol
        self.setting_dic['contract'] = contract
        self.setting_dic['period'] = bar_type
        self.setting_dic['start_date'] = start_date
        self.setting_dic['end_date'] = end_date
        self.setup_child_graph()

    def setup_child_graph(self):
        domain_symbol = '.'.join([self.setting_dic['exchange'], self.setting_dic['symbol']])
        contract = self.setting_dic['contract']
        bar_type = self.setting_dic['period']
        start_date = self.setting_dic['start_date']
        end_date = self.setting_dic['end_date']
        self.raw_data = DI.getBarBySymbol(domain_symbol, contract, bar_type, start_date + ' 09:00:00', end_date + ' 15:00:00')
        #self.raw_data = pd.read_excel('RB1810_2018-06-19_1m.xlsx')
        self.main_child_graph.set_raw_data(self.raw_data)
        for second_child_graph in self.child_graph_list:
            second_child_graph.set_raw_data(self.raw_data)
        self.range_control_plt.plot(self.raw_data['close'], pen="w", name='close')
        self.region.sigRegionChanged.connect(self.set_child_range)
        self.region.setRegion([0, 100])
        pass

    def set_child_range(self):
        #self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.main_child_graph.update_visual_range(int(minX), int(maxX))
        for second_child_graph in self.child_graph_list:
            second_child_graph.update_visual_range(int(minX), int(maxX))

    def update_region(self,window, viewRange):
        rgn = viewRange[0]
        self.region.setRegion(rgn)
        self.region_minx, self.region_maxx = self.region.getRegion()

    def main_child_plt_changed(self):
        self.main_child_graph.plt.sigRangeChanged.connect(self.update_region)
        self.proxy = pg.SignalProxy(self.main_child_graph.plt.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)

    def mouseMoved(self, event):
        pos = event[0]  ## using signal proxy turns original arguments into a tuple
        if self.main_child_graph.plt.sceneBoundingRect().contains(pos):
            a = self.main_child_graph.plt.boundingRect().getRect()
            knum = self.region_maxx - self.region_minx
            # (pos.x()-35）表示鼠标点距离左边框的位置
            # (a[2]-35)/knum表示每一根K线占用的像素点数量
            # 上面两者两除即为鼠标位置点的K线序号，+minx就是在整个数据列表中的位置
            rx = int((pos.x()-35)/((a[2]-35)/knum)+ self.region_minx)
            index = rx
            #if index > 0 and index < len(self.t):
            self.main_child_graph.set_indexer_label(index)
            for second_child_graph in self.child_graph_list:
                second_child_graph.set_indexer_label(index)

    def add_child_graph(self):
        second_child_graph = ChildGraph(True)
        self.child_graph_list.append(second_child_graph)
        if self.raw_data is not None:
            second_child_graph.set_raw_data(self.raw_data)
        self.child_graph_layout.insertWidget(len(self.child_graph_list), second_child_graph, stretch=2)

    def remove_child_graph(self):
        if self.child_graph_list:
            self.child_graph_layout.removeWidget(self.child_graph_list[-1])
            self.child_graph_list[-1].deleteLater()
            del self.child_graph_list[-1]
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = KViewer()
    demo.show()
    sys.exit(app.exec_())