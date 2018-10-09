# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase


class MACD(IndexerBase):
    indexer_name = 'MACD'
    indexer_name_list = ['DIF', 'DEA', 'HIST']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
    default_para_dic = {
        'Short':5,
        'Mid':9,
        'Long':15
    }

    def __init__(self, raw_data, plt):
        super(MACD,self).__init__(raw_data, plt)

    def calculate_indexer_valuer(self):
        closedata = self.raw_data['close']
        short = self.para_dic['Short']
        long1 = self.para_dic['Long']
        mid = self.para_dic['Mid']
        sema = closedata.ewm(span=short, adjust=False).mean()
        lema = closedata.ewm(span=long1, adjust=False).mean()
        data_dif = sema - lema
        # data_dea = pd.ewma(data_dif, span=mid)
        data_dea = data_dif.ewm(span=mid, adjust=False).mean()
        data_bar = (data_dif - data_dea) * 2
        self.indexer_value_dic['DIF'] = data_dif.tolist()
        self.indexer_value_dic['DEA'] = data_dea.tolist()
        self.indexer_value_dic['HIST'] = data_bar.tolist()

    def draw_indexer(self):
        i = 0
        for indexer_name, values in self.indexer_value_dic.items():
            self.plt_dic[indexer_name] = self.plt.plot(name=indexer_name, pen=self.color_list[i])
            self.plt_dic[indexer_name].setData(values)
            print (indexer_name)
            i += 1

    def re_draw_indexer(self):
        for pname, values in self.indexer_value_dic.items():
            self.plt_dic[pname].setData(values)

    def get_polar_value(self,start_pos, end_pos):
        max_v = max(max(self.indexer_value_dic['DIF'][start_pos:end_pos]),
                    max(self.indexer_value_dic['DEA'][start_pos:end_pos]),
                    max(self.indexer_value_dic['HIST'][start_pos:end_pos]))
        min_v = min(min(self.indexer_value_dic['DIF'][start_pos:end_pos]),
                    min(self.indexer_value_dic['DEA'][start_pos:end_pos]),
                    min(self.indexer_value_dic['HIST'][start_pos:end_pos]))
        return max_v, min_v