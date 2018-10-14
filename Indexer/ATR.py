# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase
import numpy as np

class ATR(IndexerBase):
    indexer_name = 'ATR'
    indexer_name_list = ['ATR', 'TR']
    default_para_dic = {
        'N': 26,
    }

    def __init__(self, raw_data, plt):
        super(ATR, self).__init__(raw_data, plt)
        self.indexer_name_list = ['ATR', 'TR']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置

    def calculate_indexer_value(self):
        n = self.para_dic['N']
        closeshift1 = self.raw_data.close.shift(1).fillna(0)
        self.raw_data['c'] = self.raw_data.high - self.raw_data.low
        self.raw_data['d'] = np.abs(self.raw_data.high - closeshift1)
        self.raw_data['b'] = np.abs(self.raw_data.low - closeshift1)
        self.raw_data['TR'] = self.raw_data[['c', 'd', 'b']].max(axis=1)
        self.raw_data.loc[self.raw_data['open'] < self.raw_data['close'], 'TR'] = 0 - self.raw_data['TR']
        self.raw_data['ATR'] = np.abs(self.raw_data['TR'].rolling(window=n).mean())
        self.indexer_value_dic['TR'] = self.raw_data['TR'].tolist()
        self.indexer_value_dic['ATR'] = self.raw_data['ATR'].tolist()

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
        max_v = max(max(self.indexer_value_dic['ATR'][start_pos:end_pos]),
                    max(self.indexer_value_dic['TR'][start_pos:end_pos]))
        min_v = min(min(self.indexer_value_dic['ATR'][start_pos:end_pos]),
                    min(self.indexer_value_dic['TR'][start_pos:end_pos]))
        return max_v, min_v
