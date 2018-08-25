# -*- coding: utf-8 -*-
"""
指标类，用于管理指标相内容：
1.参数，包括参数控件的内容
    para_name:参数名列表
    para_dic: 参数字典，键为参数名，值为参数值
    para_widgets_dic: 参数按键字典， 键为参数名，值为控件名
2.数据
    data_dic:数据字典，键为参数名，值为数据
3.画图
    plt:主图控件
    plt_dic:子图控件字典，键为参数名，值为子图控件

"""
class IndexerBase(object):

    color_list = ['w', 'y', 'c', 'r', 'g']

    def __init__(self, plt, ):
        self.is_avtived = True
        self.plt = plt
        self.para_name = []
        self.para_dic = {}
        self.para_widgets_dic = {}

        self.data_dic = {}

        self.plt_dic = {}

        pass

    def draw(self):
        pass

    def reflesh(self):
        pass

    def set_data(self):
        pass

    def set_all_para(self):
        for k, v in self.para_widgets_dic.items():
            p = self.set_para(v)
            if p:
                self.para_dic[k] = p
            else:
                self.para_dic[k] = 0
        self.set_data()

    def set_para(self, lindEdit_widgets):
        t = lindEdit_widgets.text()
        if t:
            try:
                p=int(t)
                return p
            except:
                print (u"请检查输入内容，只接受数字")
                return None

    def get_indexer_value_text(self, pos):
        # 根据传入的位置返回一个指标值的字符串
        t = ""
        i = 0
        for pname in self.para_name:
            c = self.color_list[i]
            t += "<span style='color: %s'>%s=%0.3f </span>" % (c, pname, self.data_dic[pname][pos])
            i += 1
        return t

class Indexer_MA(IndexerBase):

    def __init__(self, plt, rawdata, para_widgets_list):
        super(IndexerBase, self).__init__()
        self.plt = plt
        self.is_avtived = True
        self.plt = plt
        self.para_name = []
        self.para_dic = {}
        self.para_widgets_dic = {}

        self.data_dic = {}

        self.plt_dic = {}

        self.para_name = ['N1', 'N2', 'N3', 'N4', 'N5']

        # 获取原始数据
        self.series_close = rawdata['close']

        # 获取参数
        for i in range(len(para_widgets_list)):
            para_name = self.para_name[i]
            pwidget = para_widgets_list[i]
            self.para_widgets_dic[para_name] = pwidget
        self.set_all_para()

        # 准备数据
        self.set_data()

        pass

    def draw(self):
        if self.is_avtived:
            for i in range(len(self.para_name)):
                pname = self.para_name[i]
                if pname in self.para_dic.keys():
                    self.plt_dic[pname]=self.plt.plot(name=pname,pen=self.color_list[i])
                    self.plt_dic[pname].setData(self.data_dic[pname])

    def reflesh(self):
        for k, d in self.data_dic.items():
            self.plt_dic[k].setData(d)

    def set_data(self,):
        for k, d in self.para_dic.items():
            self.data_dic[k] = self.series_close.rolling(d).mean()
