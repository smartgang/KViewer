# -*- coding: utf-8 -*-

import complex2
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import time
import pyqtgraph as pg
import pandas as pd
import tushare as ts
import datetime
from matplotlib.pylab import date2num


class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = complex2.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.update_date()
        self.update_calendar()
        self.set_lcd()
        self.set_dial()

        #self.zero_progress()
        #self.click_radio3()
        self.update_progressbar()

        self.set_font()

        # 数据要解好，供多个用，这样才省事
        #hist_data = ts.get_hist_data('600519', start='2010-05-01', end='2017-11-04')
        #hist_data.to_csv('hist_data.csv')
        hist_data = pd.read_csv('hist_data.csv')
        self.t = range(hist_data.shape[0])
        self.open = hist_data.open.tolist()
        self.high = hist_data.high.tolist()
        self.low = hist_data.low.tolist()
        self.close = hist_data.close.tolist()
        packdate = zip(self.t,self.open, self.close, self.low, self.high)
        ma5 = hist_data.close.rolling(5).mean().tolist()
        self.plt1 = self.chart(hist_data['date'].tolist(),packdate)
        self.plt2 = self.chart2(self.t, self.close)
        self.plt1.plot(ma5)

        # 下面第2个图的范围设置框
        self.region = pg.LinearRegionItem()
        self.region.setZValue(10)
        self.region.sigRegionChanged.connect(self.update_plt1)

        self.plt1.sigRangeChanged.connect(self.updateRegion)

        self.region.setRegion([0, 100])
        # Add the LinearRegionItem to the ViewBox, but tell the ViewBox to exclude this
        # item when doing auto-range calculations.
        self.plt2.addItem(self.region, ignoreBounds=True)

        self.ui.verticalLayout_3.addWidget(self.plt1)
        self.ui.verticalLayout_3.addWidget(self.plt2)
        MainWindow.show()
        sys.exit(app.exec_())

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def set_lcd(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    def set_dial(self):
        self.ui.dial.valueChanged['int'].connect(self.set_lcd)

    #按钮2重置进度栏
    def zero_progress(self):
        self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)

    def update_progress(self):
        value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(value)

    def click_radio3(self):
        self.ui.radioButton_3.clicked.connect(self.update_progress)

    def set_font(self):
        self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)

    def progressBar_counter(self, start_value=0):
        self.run_thread =  RunThread(parent=None, counter_start=start_value)
        self.run_thread.start()
        self.run_thread.counter_value.connect(self.set_progressbar)

    def set_progressbar(self, counter):
        if not self.stop_progress:
            self.ui.progressBar.setValue(counter)

    # 多进程的方式控制progressBar
    # RunThread会一直计时，并发出int类型的信号
    # start_progressbar开始时，会先取得progressbar的值，然后再往下数，这样ui上看起来progressbar是连着上一次中断的位置往下的
    # 实际上点stop的时候，RunThread进程已经结束，重新开始时是新的线程了
    def update_progressbar(self):
        self.ui.radioButton.clicked.connect(self.start_progressbar)
        self.ui.radioButton_2.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_3.clicked.connect(self.reset_progressbar)
        self.progress_value = 0
        self.stop_progress = False

    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.ui.progressBar.value()
        self.progressBar_counter(self.progress_value)

    def stop_progressbar(self):
        self.stop_progress = True
        try:
            self.run_thread.stop()
        except:
            pass

    def reset_progressbar(self):
        self.progress_value = 0
        self.ui.progressBar.reset()
        #self.stop_progress = False
        self.stop_progressbar()

    def chart(self,date_list, data_list):
        """
        data_list = []
        i = 0
        for dates, row in hist_data.iterrows():
            #date_time = datetime.datetime.strptime(dates, "%Y-%m-%d")
            #t = date2num(date_time)
            open, high, close, low = row[:4]
            datas = (i, open, close, low, high)
            i+=1
            data_list.append(datas)
        # axis_dic = dict(enumerate(axis))
        #print (data_list)
        """
        item = CandlestickItem(data_list)
        axis = DateAxis(date_strings=date_list, orientation='bottom')
        plt = pg.PlotWidget(axisItems={'bottom': axis})
        #plt = pg.PlotWidget()
        plt.addItem(item, )
        # plt.setXRange()
        plt.showGrid(x=True, y=True)
        return plt

    def chart2(self,x,y):
        #y = hist_data['close'].tolist()
        #x_datas =hist_data.index.tolist()
        #x=range(len(y))
        #for x1 in x_datas:
        #    date_time = datetime.datetime.strptime(x1, "%Y-%m-%d")
        #    x.append(date2num(date_time))
        # axis_dic = dict(enumerate(axis))
        #print (close_list)
        plt = pg.PlotWidget()
        plt.addLegend() # 加上图标
        plt.plot(x=x,y=y, pen="w", name='close')
        #plt.addItem(item, )
        # plt.setXRange()
        #plt.showGrid(x=True, y=True)
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

class RunThread(QtCore.QThread):
    # 定义一个信号，内容为int
    counter_value = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True

    def run(self):
        while self.counter < 100 and self.is_running == True:
            time.sleep(0.1)
            self.counter += 1
            print (self.counter)
            self.counter_value.emit(self.counter)   # 发出信号

    def stop(self):
        self.is_running = False
        print ("线程停止中...")
        self.terminate()

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
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
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