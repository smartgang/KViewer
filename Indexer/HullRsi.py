# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase
import numpy as np
import talib


class HULL_RSI(IndexerBase):
    indexer_name = 'HULL_RSI'
    indexer_name_list = ['RSI']
    default_para_dic = {
        'N1': 5,
        'M1': 5,
        'M2': 9,
        'N': 8
    }

    def __init__(self, raw_data, plt):
        super(HULL_RSI, self).__init__(raw_data, plt)
        self.indexer_name_list = ['RSI']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
        self.indexer_color_dic = {
            'RSI': 'blue'
        }

    def calculate_indexer_value(self):
        n1 = self.para_dic['N1']
        m1 = self.para_dic['M1']
        m2 = self.para_dic['M2']
        n = self.para_dic['N']
        close_array = np.array(self.raw_data['close'].values, dtype='float')
        n = float(n)
        rsi_data = talib.RSI(close_array, n1)
        rsi_ema1 = talib.EMA(rsi_data, m1)
        rsi_ema2 = talib.EMA(rsi_ema1, m2)
        rsi_new = rsi_ema1 - rsi_ema2
        n_2 = round(n / 2, 0)
        n_squr = round(np.sqrt(n), 0)
        wma1 = talib.MA(rsi_new, n, matype=2)
        wma2 = talib.MA(rsi_new, n_2, matype=2)
        x = wma2 * 2 - wma1
        hull_ma = talib.MA(x, n_squr, matype=2)
        self.indexer_value_dic['RSI'] = hull_ma

    def draw_indexer(self):
        i = 0
        for indexer_name, values in self.indexer_value_dic.items():
            c = self.indexer_color_dic[indexer_name][0]
            self.plt_dic[indexer_name] = self.plt.plot(name=indexer_name, pen=c)
            self.plt_dic[indexer_name].setData(values)
            i += 1

    def re_draw_indexer(self):
        for pname, values in self.indexer_value_dic.items():
            self.plt_dic[pname].setData(values)

    def get_polar_value(self,start_pos, end_pos):
        max_v = max(self.indexer_value_dic['RSI'][start_pos:end_pos])
        min_v = min(self.indexer_value_dic['RSI'][start_pos:end_pos])
        return max_v, min_v
