# -*- coding: utf-8 -*-

import nullWindow
from PyQt5 import QtCore, QtWidgets, QtGui

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = nullWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem(u'数据1'))
    ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(u'数据2'))
    ui.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(u'数据3'))

    MainWindow.show()
    sys.exit(app.exec_())