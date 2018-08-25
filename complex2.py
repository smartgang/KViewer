# -*- coding: utf-8 -*-
#from PySide import QtCore, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 531))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 73, 92))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 30, 321, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(60, 30, 172, 102))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dial = QtWidgets.QDial(self.widget)
        self.dial.setObjectName("dial")
        self.horizontalLayout.addWidget(self.dial)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_2)
        self.fontComboBox.setGeometry(QtCore.QRect(60, 230, 381, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(60, 290, 381, 71))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(60, 480, 661, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 791, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", u"第一列"))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "New Column"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", u"子条目一"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", u"子条目一一"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", u"树"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", u"日历"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Tab 1"))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", u"功能选择"))
        self.radioButton.setText(QtWidgets.QApplication.translate("MainWindow", u"默认"))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("MainWindow", u"重置"))
        self.radioButton_3.setText(QtWidgets.QApplication.translate("MainWindow", u"选项3"))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", u"移动刻度盘"))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtWidgets.QApplication.translate("MainWindow", "绘图"))

