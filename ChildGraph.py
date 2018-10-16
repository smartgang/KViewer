# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Indexer import *
import pyqtgraph as pg
import pandas as pd


class ChildGraph(QWidget):

    main_child_plt_changed = pyqtSignal(name='main_child_plt_changed')

    def __init__(self, child=True):
        super(ChildGraph, self).__init__()
        self.child = child
        self.frame_layout = QVBoxLayout(self)
        self.para_setting_btn = QPushButton("参数设置")
        self.para_setting_btn.setFixedWidth(100)
        self.indexer_label = QLabel(self)
        self.vLine = None
        self.frame_layout.addLayout(self.header_layout())
        self.raw_data = None
        self.open_list = []
        self.high_list = []  # 当子图为主图是(child=Fasle)， 用来保留raw_data的high和low信息，用于计算Y轴范围
        self.low_list = []
        self.close_list = []
        self.time_list = []
        self.plt = None
        self.indexer_class = None
        self.indexer_name = ''
        self.indexer_widget = None

    def set_raw_data(self, raw_data):
        # 外部调用，在主图获取到数据后传入数据
        # 获取到数据同时加载plt,如果是主图则加载K线ohlc
        self.raw_data = raw_data
        if not self.child:
            self.open_list = self.raw_data['open'].tolist()
            self.high_list = self.raw_data['high'].tolist()
            self.low_list = self.raw_data['low'].tolist()
            self.close_list = self.raw_data['close'].tolist()
            self.time_list = self.raw_data['strtime'].tolist()
        self._setup_plt()

    def _setup_candlestick(self):
        # 为主图加载K线
        csitem = CandlestickItem(self.raw_data)
        axis = DateAxis(date_strings=self.time_list, orientation='bottom')
        return csitem, axis

    def _setup_plt(self):
        if self.plt:
            self.plt.close()
        if not self.child:
            # 为主图加载K线
            item, axis = self._setup_candlestick()
            self.plt = pg.PlotWidget(axisItems={'bottom': axis})
            self.plt.addItem(item, )
            self.plt.showGrid(x=True, y=True)
            self.main_child_plt_changed.emit()
        else:
            self.plt = pg.PlotWidget()
            self.plt.showGrid(x=True, y=True)
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.plt.addItem(self.vLine)
        self.frame_layout.addWidget(self.plt)

    def header_layout(self):
        hbox = QHBoxLayout(self)
        self.para_setting_btn.clicked.connect(self.set_indexer_parameter)
        hbox.addWidget(self.indexer_label)
        hbox.addWidget(self.para_setting_btn)
        return hbox

    def set_indexer_label(self, xpos):
        # 设置指标标签的值，同时更新竖线位置
        if self.indexer_class:
            if xpos >= self.indexer_class.value_num:
                return
            value_str = self.indexer_class.get_indexer_value_text(xpos)
            if not self.child:
                # 主图要加上ohlc数据
                open = self.open_list[xpos]
                close = self.close_list[xpos]
                if open > close:
                    c = 'green'
                elif open < close:
                    c = 'red'
                else:
                    c = 'black'
                value_str += \
                    "     <span style='color: %s'>open=%0.1f,high=%0.1f,low=%0.1f,close=%0.1f</span>,%s" % (
                    c, open, self.high_list[xpos], self.low_list[xpos], close, self.time_list[xpos])
            self.indexer_label.setText(value_str)
            self.vLine.setPos(xpos)

    def set_indexer_parameter(self):
        # 用户设置指标参数接口，弹出指标设置对话框供用户设置
        # 已设置的指标加载已有参数，其余指标均加载默认参数
        all_indexer_para_dic = get_all_indexer_para_dic()
        if self.indexer_class:
            all_indexer_para_dic[self.indexer_name] = self.indexer_class.get_para_dic()
        self.indexer_widget = IndexerWidget(all_indexer_para_dic)
        self.indexer_widget.signal_para_changed.connect(self.indexer_parameter_changed)
        self.indexer_widget.show()

    def indexer_parameter_changed(self, selected_indexer, para_dic):
        # 接收用户设置的新参数，并更新显示
        if selected_indexer == self.indexer_name:
            # 所选指标与已有指标相同，则更新参数
            self.indexer_class.update_parameter(para_dic[selected_indexer])
        else:
            # 所选指标与已有指标不同，则加载新指标
            if self.indexer_class:
                #self.plt.clear()
                self._setup_plt()
            indexer_class = indexer_mapping_dic[selected_indexer](self.raw_data, self.plt)
            indexer_class.set_para_dic(para_dic[selected_indexer])
            indexer_class.calculate_indexer_value()
            indexer_class.draw_indexer()
            self.indexer_class = indexer_class
            self.indexer_name = selected_indexer
        self.update_visual_range(200, 400)
        self.set_indexer_label(200)

    def update_visual_range(self, start_pos, end_pos):
        if self.plt and self.indexer_class:
            # Y轴自适应
            value_n = self.indexer_class.value_num
            start_pos = max(0, start_pos)
            start_pos = min(start_pos, value_n)
            end_pos = max(1, end_pos)
            end_pos = min(end_pos, value_n)
            if not self.child:
                minY = min(self.low_list[start_pos:end_pos])
                maxY = max(self.high_list[start_pos:end_pos])
            else:
                minY = 999999
                maxY = 0
            indexer_max_value, indexer_min_value = self.indexer_class.get_polar_value(start_pos, end_pos)
            minY = min(minY, indexer_min_value)
            maxY = max(maxY, indexer_max_value)
            self.plt.setYRange(minY, maxY)
            self.plt.setXRange(start_pos, end_pos, padding=0)


class DateAxis(pg.AxisItem):
    def __init__(self, date_strings, orientation):
        pg.AxisItem.__init__(self, orientation)
        self.date_strings = date_strings
        self.len = len(self.date_strings)

    def tickStrings(self, values, scale, spacing):
        strns = []
        for x in values:
            x1 = int(x)
            if 0 <= x1 < self.len:
                strns.append(self.date_strings[x1])
            else:
                strns.append('')
        return strns


## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect()
## (see QGraphicsItem documentation)
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        t = range(data.shape[0])
        open = data.open.tolist()
        high = data.high.tolist()
        low = data.low.tolist()
        close = data.close.tolist()

        self.data = zip(t, open, close, low, high)
        ## data must have fields: time, open, close, min, max
        self.generatePicture()

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly,
        ## rather than re-drawing the shapes every time.
        self.picture = QPicture()
        p = QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QPointF(t, min), QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setBrush(pg.mkBrush('r'))
            p.drawRect(QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QRectF(self.picture.boundingRect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ChildGraph(False)
    # demo.update_visual_range(200, 300)
    demo.set_raw_data(1)
    demo.show()
    sys.exit(app.exec_())
