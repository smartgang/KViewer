# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase
import pyqtgraph as pg
import numpy as np
import talib


class HULL_MACD(IndexerBase):
    indexer_name = 'HULL_MACD'
    indexer_name_list = ['DIF', 'DEA', 'HIST']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
    default_para_dic = {
        'Short':12,
        'Mid':9,
        'Long':26
    }

    def __init__(self, raw_data, plt):
        super(HULL_MACD, self).__init__(raw_data, plt)
        self.indexer_name_list = ['DIF', 'DEA', 'HIST']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
        self.hist_item_up = None
        self.hist_item_down = None
        self.indexer_color_dic = {
            'DIF': 'blue',
            'DEA': 'magenta',
            'HIST': 'red'
        }

    def calculate_indexer_value(self):
        short = self.para_dic['Short']
        long_v = self.para_dic['Long']
        mid = self.para_dic['Mid']
        closedata = np.array(self.raw_data['close'].values, dtype=float)
        sema = self._hull_ma(closedata, short)
        lema = self._hull_ma(closedata, long_v)
        data_dif = sema - lema
        data_dea = talib.MA(data_dif, mid, matype=1)
        data_bar = 2 * (data_dif - data_dea)
        self.indexer_value_dic['DIF'] = data_dif.tolist()
        self.indexer_value_dic['DEA'] = data_dea.tolist()
        self.indexer_value_dic['HIST'] = data_bar.tolist()

    def _hull_ma(self, close_array, n):
        n = float(n)
        n_2 = round(n / 2)
        n_squr = round(np.sqrt(n))
        wma1 = talib.MA(close_array, n, matype=2)
        wma2 = talib.MA(close_array, n_2, matype=2)
        x = wma2 * 2 - wma1
        return talib.MA(x, n_squr, matype=2)

    def draw_indexer(self):
        i = 0
        for indexer_name, values in self.indexer_value_dic.items():
            if indexer_name == 'HIST':
                n = 0
                up_num = []
                up_value = []
                down_num = []
                down_value = []
                for v in values:
                    if v >= 0:
                        up_value.append(v)
                        up_num.append(n)
                    else:
                        down_value.append(v)
                        down_num.append(n)
                    n += 1
                self.hist_item_up = pg.BarGraphItem(x=up_num, height=up_value, width=0.3, brush='r')
                self.hist_item_down = pg.BarGraphItem(x=down_num, height=down_value, width=0.3, brush='g')
                self.plt.addItem(self.hist_item_up)
                self.plt.addItem(self.hist_item_down)
            else:
                c = self.indexer_color_dic[indexer_name][0]
                self.plt_dic[indexer_name] = self.plt.plot(name=indexer_name, pen=c)
                self.plt_dic[indexer_name].setData(values)
            i += 1

    def re_draw_indexer(self):
        for pname, values in self.indexer_value_dic.items():
            if pname == 'HIST':
                self.plt.removeItem(self.hist_item_up)
                self.plt.removeItem(self.hist_item_down)
                n = 0
                up_num = []
                up_value = []
                down_num = []
                down_value = []
                for v in values:
                    if v >= 0:
                        up_value.append(v)
                        up_num.append(n)
                    else:
                        down_value.append(v)
                        down_num.append(n)
                    n += 1
                self.hist_item_up = pg.BarGraphItem(x=up_num, height=up_value, width=0.3, brush='r')
                self.hist_item_down = pg.BarGraphItem(x=down_num, height=down_value, width=0.3, brush='g')
                self.plt.addItem(self.hist_item_up)
                self.plt.addItem(self.hist_item_down)
            else:
                self.plt_dic[pname].setData(values)

    def get_polar_value(self,start_pos, end_pos):
        max_v = max(max(self.indexer_value_dic['DIF'][start_pos:end_pos]),
                    max(self.indexer_value_dic['DEA'][start_pos:end_pos]),
                    max(self.indexer_value_dic['HIST'][start_pos:end_pos]))
        min_v = min(min(self.indexer_value_dic['DIF'][start_pos:end_pos]),
                    min(self.indexer_value_dic['DEA'][start_pos:end_pos]),
                    min(self.indexer_value_dic['HIST'][start_pos:end_pos]))
        return max_v, min_v