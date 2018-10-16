# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase
import numpy as np
import talib


class KDJ(IndexerBase):
    indexer_name = 'KDJ'
    indexer_name_list = ['K', 'D', 'J']
    default_para_dic = {
        'N': 9,
        'M1': 3,
        'M2': 3
    }

    def __init__(self, raw_data, plt):
        super(KDJ, self).__init__(raw_data, plt)
        self.indexer_name_list = ['K', 'D', 'J']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
        self.indexer_color_dic = {
            'K': 'blue',
            'D': 'magenta',
            'J': 'cyan'
        }

    def calculate_indexer_value(self):
        n = self.para_dic['N']
        m1 = self.para_dic['M1']
        m2 = self.para_dic['M2']
        low_list = self.raw_data['low'].rolling(n).min().fillna(self.raw_data['low'])  # 使用low的值来填充前面的空白
        high_list = self.raw_data['high'].rolling(n).max().fillna(self.raw_data['high'])  # 使用high来填充
        rsv = (self.raw_data['close'] - low_list) / (high_list - low_list) * 100
        a = 1.0/m1
        a2 = 1.0/m2
        kdj_k = rsv.ewm(alpha=a, adjust=False).mean()
        kdj_d = kdj_k.ewm(alpha=a2, adjust=False).mean()
        kdj_j = 3 * kdj_k - 2 * kdj_d
        self.indexer_value_dic['K'] = kdj_k
        self.indexer_value_dic['D'] = kdj_d
        self.indexer_value_dic['J'] = kdj_j

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
        max_v = max(max(self.indexer_value_dic['K'][start_pos:end_pos]),
                    max(self.indexer_value_dic['D'][start_pos:end_pos]),
                    max(self.indexer_value_dic['J'][start_pos:end_pos]))
        min_v = min(min(self.indexer_value_dic['K'][start_pos:end_pos]),
                    min(self.indexer_value_dic['D'][start_pos:end_pos]),
                    min(self.indexer_value_dic['J'][start_pos:end_pos]))
        return max_v, min_v
