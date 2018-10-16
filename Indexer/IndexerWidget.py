# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Indexer import *

class IndexerWidget(QWidget):

    signal_para_changed = pyqtSignal(str,dict, name='para_changed')

    def __init__(self, all_indexer_para_dic, current_indexer_name):
        super(IndexerWidget,self).__init__()
        #self.setGeometry(300,50,10,10)
        self.setWindowTitle('设置指标参数')
        self.indexer_para_dic = all_indexer_para_dic
        self.leftlist = QListWidget()
        self.para_line_edit_dic = {}
        self.stack_dic = {}
        self.indexer_pos_dic = {}   #  记录各个指标在leftlist中的位置
        i = 0
        current_indexer_pos = 0
        self.stack = QStackedWidget(self)
        for indexer_name in self.indexer_para_dic.keys():
            self.leftlist.insertItem(i, indexer_name)
            stack_widget= QWidget()
            layout = QFormLayout()
            indexer_para_dic = self.indexer_para_dic[indexer_name]
            line_edit_dic = {}
            for name, value in indexer_para_dic.items():
                le = QLineEdit()
                le.setValidator(QIntValidator())
                le.setMaxLength(2)
                le.setText(str(value))
                line_edit_dic[name] = le
                layout.addRow(name, le)
            self.para_line_edit_dic[indexer_name] = line_edit_dic
            stack_widget.setLayout(layout)
            self.stack_dic[indexer_name] = stack_widget
            self.stack.addWidget(stack_widget)
            if indexer_name == current_indexer_name:
                current_indexer_pos = i
            i += 1
        main_box = QVBoxLayout(self)
        hbox  = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.stack)
        
        main_box.addLayout(hbox)
        btn_layout = self.setup_button()
        main_box.addLayout(btn_layout)
        self.setLayout(btn_layout)
        self.leftlist.currentRowChanged.connect(self.display)
        self.leftlist.setCurrentRow(current_indexer_pos)

    def setup_button(self):
        vbox = QHBoxLayout(self)
        btn_ok = QPushButton('OK')
        btn_cancel = QPushButton('Cancle')
        btn_ok.clicked.connect(self.get_user_para)
        btn_cancel.clicked.connect(self.close)
        vbox.addWidget(btn_ok)
        vbox.addWidget(btn_cancel)
        return vbox

    def get_user_para(self):
        all_para_dic = {}
        for indexer_name, line_edit_dic in self.para_line_edit_dic.items():
            para_dic = {}
            for para_name, line_edit in line_edit_dic.items():
                para_dic[para_name] = int(line_edit.text())
            all_para_dic[indexer_name] = para_dic
        selected_indexer = self.leftlist.currentItem().text()
        self.signal_para_changed.emit(selected_indexer,all_para_dic)
        self.close()

    def display(self,i):
        self.stack.setCurrentIndex(i)

class test1():

    def __init__(self, name):
        self.name = name

    def receive_para_changed(self,selected,dict):
        print (self.name, selected, dict)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    all_indexer_para_dic = get_all_indexer_para_dic()
    demo = IndexerWidget(all_indexer_para_dic)
    #demo2 = IndexerWidget(all_indexer_para_dic)
    c1 = test1('test1')
    #c2 = test1('test2')
    demo.signal_para_changed.connect(c1.receive_para_changed)
    #demo2.signal_para_changed.connect(c2.receive_para_changed)
    demo.show()
    #demo2.show()
    sys.exit(app.exec_())