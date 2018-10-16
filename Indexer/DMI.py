# -*- coding: utf-8 -*-
from IndexerBase import IndexerBase
import numpy as np
import pandas as pd

class DMI(IndexerBase):
    indexer_name = 'DMI'
    indexer_name_list = ['PDI', 'MDI', 'ADX', 'ADXR']
    default_para_dic = {
        'N': 14,
        'M': 6,
    }

    def __init__(self, raw_data, plt):
        super(DMI, self).__init__(raw_data, plt)
        self.indexer_name_list = ['PDI', 'MDI', 'ADX', 'ADXR']  # MA的指标名和参数名都跟参数有关，所以要随参数进行设置
        self.indexer_color_dic = {
            'PDI': 'blue',
            'MDI': 'magenta',
            'ADX': 'cyan',
            'ADXR': 'green'
        }

    def calculate_indexer_value(self):
        n = self.para_dic['N']
        m = self.para_dic['M']
        high = self.raw_data.high
        print ('high')
        low = self.raw_data.low
        close = self.raw_data.close
        closeshift1 = close.shift(1).fillna(0)
        c = high - low
        d = high - closeshift1
        df1 = pd.DataFrame({'c': c, 'd': d})
        df1['A'] = df1.max(axis=1)
        df1.drop('c', axis=1, inplace=True)
        df1.drop('d', axis=1, inplace=True)
        df1['B'] = np.abs(low - closeshift1)
        df1['C'] = df1.max(axis=1)
        df1['TR'] = df1['C'].rolling(n).sum()
        HD = high - high.shift(1).fillna(0)
        LD = low.shift(1).fillna(0) - low
        df1['HD'] = HD
        df1['LD'] = LD
        df2 = pd.DataFrame({'HD': HD, 'LD': LD})
        df2['DMP_1'] = df2[(df2['HD'] > df2['LD']) & (df2['HD'] > 0)]['HD']
        df2['DMM_1'] = df2[(df2['LD'] > df2['HD']) & (df2['LD'] > 0)]['LD']
        df2 = df2.fillna(0)
        df1['DMP'] = df2['DMP_1'].rolling(n).sum()
        df1['DMM'] = df2['DMM_1'].rolling(n).sum()
        del df2
        df1['PDI'] = df1['DMP'] * 100 / df1['TR']
        df1['MDI'] = df1['DMM'] * 100 / df1['TR']
        adx = np.abs(df1['MDI'] - df1['PDI']) / (df1['MDI'] + df1['PDI']) * 100
        print ("pre adx")
        df1['ADX'] = adx.rolling(m).mean()
        df1['ADXR'] = (df1['ADX'] + df1['ADX'].shift(m).fillna(0)) / 2
        self.indexer_value_dic['PDI'] = df1['PDI'].tolist()
        self.indexer_value_dic['MDI'] = df1['MDI'].tolist()
        self.indexer_value_dic['ADX'] = df1['ADX'].tolist()
        self.indexer_value_dic['ADXR'] = df1['ADXR'].tolist()

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
        max_v = max(max(self.indexer_value_dic['PDI'][start_pos:end_pos]),
                    max(self.indexer_value_dic['MDI'][start_pos:end_pos]),
                    max(self.indexer_value_dic['ADX'][start_pos:end_pos]),
                    max(self.indexer_value_dic['ADXR'][start_pos:end_pos]))
        min_v = min(min(self.indexer_value_dic['PDI'][start_pos:end_pos]),
                    min(self.indexer_value_dic['MDI'][start_pos:end_pos]),
                    min(self.indexer_value_dic['ADX'][start_pos:end_pos]),
                    min(self.indexer_value_dic['ADXR'][start_pos:end_pos]))
        return max_v, min_v
