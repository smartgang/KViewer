# -*- coding: utf-8 -*-

import kviewer2
from indexer import Indexer_MA
import parameter2
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import time
import pyqtgraph as pg
import pandas as pd

import numpy as np
import tushare as ts
import datetime
from matplotlib.pylab import date2num
"""
    'b': QtGui.QColor(0,0,255,255),
    'g': QtGui.QColor(0,255,0,255),
    'r': QtGui.QColor(255,0,0,255),
    'c': QtGui.QColor(0,255,255,255),
    'm': QtGui.QColor(255,0,255,255),
    'y': QtGui.QColor(255,255,0,255),
    'k': QtGui.QColor(0,0,0,255),
    'w': QtGui.QColor(255,255,255,255),
    'd': QtGui.QColor(150,150,150,255),
    'l': QtGui.QColor(200,200,200,255),
    's': QtGui.QColor(100,100,150,255),"""
color_list = ['w', 'y', 'c','r','g']

class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = kviewer2.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.ma_para = []
        self.ma_data = []
        self.ma_plot_dic = {}
        # 准备数据

        hist_data = pd.read_csv('RB1810_2018-06-19_1m.csv')
        self.t = range(hist_data.shape[0])
        self.date_list = hist_data['Unnamed: 0'].tolist()
        self.open = hist_data.open.tolist()
        self.high = hist_data.high.tolist()
        self.low = hist_data.low.tolist()
        self.close = hist_data.close.tolist()
        self.prepare_indexer_para()

        packdate = zip(self.t,self.open, self.close, self.low, self.high)
        self.plt1 = self.chart(self.date_list,packdate)
        self.plt2 = self.chart2(self.t, self.close)
        self.plt1.addLegend()
        """
        i=0
        for d in self.ma_para:
            pname='ma%d'%d
            self.ma_plot_dic[pname]=self.plt1.plot(name=pname,pen=color_list[i])
            i+=1
        self.prepare_indexer_data()
        """
        self.ma_indexer = Indexer_MA(self.plt1, hist_data, [self.ui.lineEdit_ma_n1, self.ui.lineEdit_ma_n2,
                                                            self.ui.lineEdit_ma_n3, self.ui.lineEdit_ma_n4,
                                                            self.ui.lineEdit_ma_n5])
        self.ma_indexer.draw()
        #self.label = QtWidgets.QLabel()
        # 加入竖线
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.plt1.addItem(self.vLine, ignoreBounds=True)
        self.vb = self.plt1.viewRect()

        # 下面第2个图的范围设置框
        self.region = pg.LinearRegionItem()
        self.region.setZValue(10)
        self.region.sigRegionChanged.connect(self.update_plt1)

        self.plt1.sigRangeChanged.connect(self.updateRegion)

        self.region.setRegion([0, 100])
        self.plt2.addItem(self.region, ignoreBounds=True)

        #self.ui.verticalLayout.addWidget(self.label)
        self.ui.verticalLayout.addWidget(self.plt1)
        self.ui.verticalLayout.addWidget(self.plt2)
        proxy = pg.SignalProxy(self.plt1.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        MainWindow.show()
        sys.exit(app.exec_())

    def prepare_indexer_para(self):
        # 准备指标参数
        """
        self.ma_para = {
            'N1': 5,
            'N2': 10,
            'N3': 15,
            'N4': 30,
            'N5': 50
        }
        """
        self.ma_para = [5,10,20,30,50]
        self.macd_para = {
            'short': 5,
            'long': 10,
            'M': 9
        }
        self.kdj_para = {
            'N': 9,
            'M1': 3,
            'M2': 3
        }
        self.dmi_para = {
            'N': 14,
            'M': 6
        }

    def prepare_indexer_data(self):
        # ma数据
        for d in self.ma_para:
            data_name = 'ma%d' % d
            data = pd.Series(self.close).rolling(d).mean()
            self.ma_plot_dic[data_name].setData(data)

    def set_ma_para(self):
        self.ma_para[0]+=3
        data = pd.Series(self.close).rolling(self.ma_para[0]).mean()
        self.ma_plot_dic['ma5'].setData(data)

    def chart(self,date_list, data_list):
        item = CandlestickItem(data_list)
        axis = DateAxis(date_strings=date_list, orientation='bottom')
        plt = pg.PlotWidget(axisItems={'bottom': axis})
        plt.addItem(item, )
        plt.showGrid(x=True, y=True)
        return plt

    def chart2(self,x,y):
        plt = pg.PlotWidget()
        plt.addLegend() # 加上图标
        plt.plot(x=x,y=y, pen="w", name='close')
        return plt

    def update_plt1(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()

        #Y轴自适应
        int_minY = max(0,int(minX))
        int_maxY = max(1, int(maxX))
        minY = min(self.low[int_minY:int_maxY]) - 5
        maxY = max(self.high[int_minY:int_maxY]) +5
        self.plt1.setYRange(minY, maxY)

        self.plt1.setXRange(minX, maxX, padding=0)


    def updateRegion(self,window, viewRange):
        rgn = viewRange[0]
        self.region.setRegion(rgn)

    def mouseMoved(self,event):
        pos = event[0]  ## using signal proxy turns original arguments into a tuple
        if self.plt1.sceneBoundingRect().contains(pos):
            a =  self.plt1.boundingRect().getRect()
            minx, maxx = self.region.getRegion()
            knum = maxx-minx
            # (pos.x()-35）表示鼠标点距离左边框的位置
            # (a[2]-35)/knum表示每一根K线占用的像素点数量
            # 上面两者两除即为鼠标位置点的K线序号，+minx就是在整个数据列表中的位置
            rx = int((pos.x()-35)/((a[2]-35)/knum)+minx)
            index = rx
            if index > 0 and index < len(self.t):
                open = self.open[index]
                close = self.close[index]
                if open > close:
                    c = 'green'
                elif open < close:
                    c = 'red'
                else:
                    c = 'black'
                self.ui.label_point.setText(
                    """
                    <span style='color: %s'>open=%0.1f,high=%0.1f,low=%0.1f,close=%0.1f</span>,%s
                    """ % (
                    c,self.open[index], self.high[index], self.low[index],self.close[index],self.date_list[index]))
                self.ui.label_para.setText(
                    self.ma_indexer.get_indexer_value_text(index)
                )
            self.vLine.setPos(index)

    def set_parameter(self):
        # 从参数页获取参数

        pass



class DateAxis(pg.AxisItem):

    def __init__(self, date_strings, orientation):
        pg.AxisItem.__init__(self,orientation)
        self.date_strings = date_strings
        self.len = len(self.date_strings)
    def tickStrings(self, values, scale, spacing):
        """
        strns = []
        rng = max(values) - min(values)
        # if rng < 120:
        #    return pg.AxisItem.tickStrings(self, values, scale, spacing)
        if rng < 3600 * 24:
            string = '%H:%M:%S'
            label1 = '%b %d -'
            label2 = ' %b %d, %Y'
        elif rng >= 3600 * 24 and rng < 3600 * 24 * 30:
            string = '%d'
            label1 = '%b - '
            label2 = '%b, %Y'
        elif rng >= 3600 * 24 * 30 and rng < 3600 * 24 * 30 * 24:
            string = '%b'
            label1 = '%Y -'
            label2 = ' %Y'
        elif rng >= 3600 * 24 * 30 * 24:
            string = '%Y'
            label1 = ''
            label2 = ''
        for x in values:
            try:
                strns.append(time.strftime(string, time.localtime(x)))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')
        try:
            label = time.strftime(label1, time.localtime(min(values))) + time.strftime(label2,
                                                                                       time.localtime(max(values)))
        except ValueError:
            label = ''
        # self.setLabel(text=label)
        return strns
        """
        #print values
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
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly,
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setBrush(pg.mkBrush('r'))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())

if __name__=='__main__':
    MainWindow()