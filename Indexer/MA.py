# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase


class MA(IndexerBase):
    indexer_name = 'MA'
    indexer_name_list = []  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
    default_para_dic = {
        'N1': 5,
        'N2': 10,
        'N3': 15,
        'N4': 30,
        'N5': 50
    }

    def __init__(self, raw_data, plt):
        self.indexer_name_list = []
        for para_name, value in self.default_para_dic.items():
            print ('MA', value)
            self.indexer_name_list.append("MA%d"%value)
        super(MA,self).__init__(raw_data, plt)

    def calculate_indexer_value(self):
        del self.indexer_value_dic
        del self.indexer_name_list
        self.indexer_name_list = []
        self.indexer_value_dic = {}
        for para_name, para_value, in self.para_dic.items():
            indexer_name = "MA%d" % para_value
            self.indexer_name_list.append(indexer_name)
            self.indexer_value_dic[indexer_name] = self.raw_data['close'].rolling(para_value).mean().tolist()
            print ('self.indexer_value_dic.keys', self.indexer_value_dic.keys())

    def draw_indexer(self):
        i = 0
        for pname, values in self.para_dic.items():
            indexer_name = "MA%d" % values
            self.plt_dic[pname] = self.plt.plot(name=pname, pen=self.color_list[i])
            self.plt_dic[pname].setData(self.indexer_value_dic[indexer_name])
            i += 1

    def re_draw_indexer(self):
        for pname, values in self.para_dic.items():
            indexer_name = "MA%d" % values
            self.plt_dic[pname].setData(self.indexer_value_dic[indexer_name])

    def get_polar_value(self,start_pos, end_pos):
        max_v = 0
        min_v = 99999
        for value_list in self.indexer_value_dic.values():
            max_v = max(max_v, max(value_list[start_pos:end_pos]))
            min_v = min(min_v, min(value_list[start_pos:end_pos]))
        return max_v, min_v