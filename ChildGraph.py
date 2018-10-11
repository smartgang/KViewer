# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Indexer import *
import pyqtgraph as pg
import pandas as pd

class ChildGraph(QWidget):

    def __init__(self, child=True):
        super(ChildGraph, self).__init__()
        self.child = child

        self.frame_layout = QVBoxLayout(self)
        self.frame_layout.addLayout(self.header_layout())
        self.raw_data = None
        self.plt = None
        self.indexer_dic = {}

    def set_raw_data(self, raw_data):
        self.raw_data = raw_data
        if not self.child:
            item = CandlestickItem(self.raw_data)
            date_list = self.raw_data['strtime'].tolist()
            axis = DateAxis(date_strings=date_list, orientation='bottom')
            self.plt = pg.PlotWidget(axisItems = {'bottom': axis})
            self.plt.addItem(item, )
            self.plt.showGrid(x=True, y=True)
            #self.plt.enableMouse()
            self.proxy = pg.SignalProxy(self.plt.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        else:
            self.plt = pg.PlotWidget()
            self.plt.showGrid(x=True, y=True)
        self.frame_layout.addWidget(self.plt)

    def header_layout(self):
        hbox = QHBoxLayout(self)
        self.indexer_label = QLabel(self)
        self.para_setting_btn = QPushButton("参数设置")
        self.para_setting_btn.clicked.connect(self.set_indexer_parameter)
        hbox.addWidget(self.indexer_label)
        hbox.addWidget(self.para_setting_btn)
        return hbox

    def set_indexer_label(self,value_str):
        self.indexer_label.setText(value_str)

    def set_indexer_parameter(self):
        all_indexer_para_dic = get_all_indexer_para_dic()
        if self.indexer_dic:
            for indexer_name, indexer_class in self.indexer_dic.items():
                all_indexer_para_dic[indexer_name] = indexer_class.get_para_dic()
        self.demo1 = IndexerWidget(all_indexer_para_dic)
        self.demo1.signal_para_changed.connect(self.indexer_parameter_changed)
        self.demo1.show()

    def indexer_parameter_changed(self, selected_indexer, para_dic):
        print ('indexer changed')
        if selected_indexer in self.indexer_dic.keys():
            indexer_class = self.indexer_dic[selected_indexer]
            indexer_class.update_parameter(para_dic[selected_indexer])
        else:
            indexer_class = indexer_mapping_dic[selected_indexer](self.raw_data,self.plt)
            indexer_class.set_para_dic(para_dic[selected_indexer])
            indexer_class.calculate_indexer_value()
            indexer_class.draw_indexer()
            self.indexer_dic[selected_indexer] = indexer_class
        print ('get_indexer_value_text')
        print ('indexer_class', indexer_class)
        value_str = indexer_class.get_indexer_value_text(200)
        print ('update_visual_range')
        self.update_visual_range(200, 400)
        print ('set_indexer_label')
        self.set_indexer_label(value_str)

    def update_visual_range(self,start_pos, end_pos):
        # Y轴自适应
        start_pos = max(0,start_pos)
        end_pos = max(1, end_pos)
        minY = 9999
        maxY = 0
        if self.indexer_dic:
            for indexer_class in self.indexer_dic.values():
                indexer_max_value, indexer_min_value = indexer_class.get_polar_value(start_pos,end_pos)
                minY = min(minY, indexer_min_value)
                maxY = max(maxY, indexer_max_value)
            self.plt.setYRange(minY, maxY)
        self.plt.setXRange(start_pos, end_pos, padding=0)

    def mouseMoved(self, pos):
        vb = self.plt.viewRange()
        print ('pos', pos)
        print ('view rect', vb)
        #print ('range', self.plt.range)
        #print ('scene bouding rect', self.plt.sceneBoundingRect())
        #print ('boudning rect', self.plt.boundingRect())

class DateAxis(pg.AxisItem):

    def __init__(self, date_strings, orientation):
        pg.AxisItem.__init__(self,orientation)
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

        self.data = zip(t,open, close, low, high)
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
    #demo.update_visual_range(200, 300)
    demo.set_raw_data(1)
    demo.show()
    sys.exit(app.exec_())