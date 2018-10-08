# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *

class KViewerMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(KViewerMainWindow, self).__init__(parent)
        self.resize(800,600)
        self.setWindowTitle('KViewer')

        self.tab_widget = QTabWidget()
        self.tab_num = 0
        tab1 = self.new_tab()
        self.tab_widget.addTab(tab1, 'tab%d'% self.tab_num)
        self.tab_widget.setTabText(0, 'contract 0')

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)
        self.setCentralWidget(self.tab_widget)

        tb = self.addToolBar("增删")
        add = QAction("增加",self)
        add.triggered.connect(self.add_tab)
        tb.addAction(add)
        rem = QAction("删除",self)
        rem.triggered.connect(self.remove_tab)
        tb.addAction(rem)
        #tb.actionTriggered[QAction].connect(self.add_tab)

    def new_tab(self):
        tab1 = QWidget()
        layout = QFormLayout()
        layout.addRow("name",QLineEdit())
        layout.addRow("address",QLineEdit())
        tab1.setLayout(layout)
        return tab1

    def add_tab(self,):
        print ('1')
        tab1 = self.new_tab()
        self.tab_num += 1
        self.tab_widget.addTab(tab1, 'tab %d'% self.tab_num)
        self.tab_widget.setTabText(self.tab_num, 'contract%d'% self.tab_num)

    def remove_tab(self):
        i = self.tab_widget.currentIndex()
        print ("current index:%d" % i)
        print ("tab_num:%d" % self.tab_num)
        self.tab_widget.removeTab(i)
        self.tab_num -=1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = KViewerMainWindow()
    win.show()
    sys.exit(app.exec_())