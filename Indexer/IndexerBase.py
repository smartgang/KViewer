# -*- coding: utf-8 -*-
"""
指标类，用于管理指标相内容：
"""

class IndexerBase(object):
    color_list = ['blue', 'magenta', 'cyan', 'red', 'green']
    indexer_name = ''
    indexer_name_list = []
    default_para_dic = {}
    para_dic = {}
    indexer_color_dic = {}  # 各指标对应的显示颜色

    def __init__(self, raw_data, plt):
        self.raw_data = raw_data
        self.para_dic = {}
        for para_name, value in self.default_para_dic.items():
            self.para_dic[para_name] = value
        self.indexer_value_dic = {}
        self.plt = plt
        self.plt_dic = {}
        self.value_num = self.raw_data.shape[0]
        #self.calculate_indexer_value()
        #self.draw_indexer()
        pass

    def calculate_indexer_value(self):
        pass

    def draw_indexer(self):
        pass

    def re_draw_indexer(self):
        pass

    def get_polar_value(self, start_pos, end_pos):
        pass

    def close_sub_plt(self):
        for plt in self.plt_dic.values():
            plt.close()

    def set_para_dic(self,para_dic):
        for para_name in self.para_dic.keys():
            self.para_dic[para_name] = para_dic[para_name]

    def get_para_dic(self):
        return self.para_dic

    def update_raw_data(self,raw_data):
        self.raw_data = raw_data
        self.calculate_indexer_value()
        self.re_draw_indexer()

    def update_parameter(self, para_dic):
        changed = False
        for para_name in self.default_para_dic.keys():
            if self.para_dic[para_name] != para_dic[para_name]:
                self.para_dic[para_name] = para_dic[para_name]
                changed = True
        if changed:
            self.calculate_indexer_value()
            self.re_draw_indexer()

    def get_indexer_value_text(self, pos):
        # 根据传入的位置返回一个指标值的字符串
        t = self.indexer_name + '('
        for para_name, para_value in self.para_dic.items():
            t += '%s_%d ' % (para_name, para_value)
        t += ')'
        i = 0
        for para_name, c in self.indexer_color_dic.items():
            t += "<span style='color: %s'>%s=%0.2f </span>" % (c, para_name, self.indexer_value_dic[para_name][pos])
            i += 1
        return t
