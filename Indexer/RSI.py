# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase
import numpy as np
import talib


class RSI(IndexerBase):
    indexer_name = 'RSI'
    indexer_name_list = ['RSI']
    default_para_dic = {
        'N': 5,
    }

    def __init__(self, raw_data, plt):
        super(RSI, self).__init__(raw_data, plt)
        self.indexer_name_list = ['RSI']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
        self.indexer_color_dic = {
            'RSI': 'blue'
        }

    def calculate_indexer_value(self):
        n = self.para_dic['N']
        close_array = np.array(self.raw_data['close'].values, dtype='float')
        self.indexer_value_dic['RSI'] = talib.RSI(close_array, n)

    def draw_indexer(self):
        i = 0
        for indexer_name, values in self.indexer_value_dic.items():
            self.plt_dic[indexer_name] = self.plt.plot(name=indexer_name, pen=self.color_list[i])
            self.plt_dic[indexer_name].setData(values)
            i += 1

    def re_draw_indexer(self):
        for pname, values in self.indexer_value_dic.items():
            self.plt_dic[pname].setData(values)

    def get_polar_value(self,start_pos, end_pos):
        max_v = max(self.indexer_value_dic['RSI'][start_pos:end_pos])
        min_v = min(self.indexer_value_dic['RSI'][start_pos:end_pos])
        return max_v, min_v
