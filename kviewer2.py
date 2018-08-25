# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.checkBox_ma = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_ma.setGeometry(QtCore.QRect(40, 10, 71, 16))
        self.checkBox_ma.setObjectName("checkBox_ma")
        self.checkBox_dmi = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_dmi.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.checkBox_dmi.setObjectName("checkBox_dmi")
        self.checkBox_macd = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_macd.setGeometry(QtCore.QRect(140, 10, 71, 16))
        self.checkBox_macd.setObjectName("checkBox_macd")
        self.checkBox_kdj = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_kdj.setGeometry(QtCore.QRect(250, 10, 71, 16))
        self.checkBox_kdj.setObjectName("checkBox_kdj")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(140, 30, 71, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(250, 30, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.pushButton_draw = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.gridLayout.addWidget(self.pushButton_draw, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_plot = QtWidgets.QWidget()
        self.tab_plot.setObjectName("tab_plot")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_plot)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_plot_field = QtWidgets.QHBoxLayout()
        self.horizontalLayout_plot_field.setObjectName("horizontalLayout_plot_field")
        self.label_para = QtWidgets.QLabel(self.tab_plot)
        self.label_para.setFrameShape(QtWidgets.QFrame.Box)
        self.label_para.setObjectName("label_para")
        self.horizontalLayout_plot_field.addWidget(self.label_para)
        self.label_point = QtWidgets.QLabel(self.tab_plot)
        self.label_point.setFrameShape(QtWidgets.QFrame.Box)
        self.label_point.setObjectName("label_point")
        self.horizontalLayout_plot_field.addWidget(self.label_point)
        self.label_file = QtWidgets.QLabel(self.tab_plot)
        self.label_file.setFrameShape(QtWidgets.QFrame.Box)
        self.label_file.setObjectName("label_file")
        self.horizontalLayout_plot_field.addWidget(self.label_file)
        self.verticalLayout.addLayout(self.horizontalLayout_plot_field)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_plot, "")
        self.tab_para = QtWidgets.QWidget()
        self.tab_para.setObjectName("tab_para")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 110, 361, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(30, 40, 41, 16))
        self.label.setObjectName("label")
        self.lineEdit_macd_short = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_macd_short.setGeometry(QtCore.QRect(80, 40, 41, 20))
        self.lineEdit_macd_short.setObjectName("lineEdit_macd_short")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_macd_long = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_macd_long.setGeometry(QtCore.QRect(190, 40, 41, 20))
        self.lineEdit_macd_long.setObjectName("lineEdit_macd_long")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 21, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_macd_m = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_macd_m.setGeometry(QtCore.QRect(280, 40, 41, 20))
        self.lineEdit_macd_m.setObjectName("lineEdit_macd_m")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 371, 90))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 4, 1, 1)
        self.lineEdit_ma_n3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n3.setObjectName("lineEdit_ma_n3")
        self.gridLayout_2.addWidget(self.lineEdit_ma_n3, 0, 5, 1, 1)
        self.lineEdit_ma_n2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n2.setObjectName("lineEdit_ma_n2")
        self.gridLayout_2.addWidget(self.lineEdit_ma_n2, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.lineEdit_ma_n1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n1.setObjectName("lineEdit_ma_n1")
        self.gridLayout_2.addWidget(self.lineEdit_ma_n1, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_ma_n4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n4.setObjectName("lineEdit_ma_n4")
        self.gridLayout_2.addWidget(self.lineEdit_ma_n4, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_ma_n5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n5.setObjectName("lineEdit_ma_n5")
        self.gridLayout_2.addWidget(self.lineEdit_ma_n5, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 4, 1, 1)
        self.comboBox_ma = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_ma.setObjectName("comboBox_ma")
        self.comboBox_ma.addItem("")
        self.comboBox_ma.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_ma, 1, 5, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_5.setGeometry(QtCore.QRect(400, 10, 361, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_opr_file = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_opr_file.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.pushButton_opr_file.setObjectName("pushButton_opr_file")
        self.label_opr = QtWidgets.QLabel(self.groupBox_5)
        self.label_opr.setGeometry(QtCore.QRect(130, 40, 54, 12))
        self.label_opr.setObjectName("label_opr")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 10, 371, 90))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 351, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_contract = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_contract.setObjectName("lineEdit_contract")
        self.gridLayout_3.addWidget(self.lineEdit_contract, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.comboBox_bar = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_bar.setObjectName("comboBox_bar")
        self.comboBox_bar.addItem("")
        self.comboBox_bar.addItem("")
        self.comboBox_bar.addItem("")
        self.comboBox_bar.addItem("")
        self.comboBox_bar.addItem("")
        self.comboBox_bar.addItem("")
        self.comboBox_bar.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_bar, 0, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 3, 1, 1)
        self.dateEdit_end = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 30), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.gridLayout_3.addWidget(self.dateEdit_end, 1, 4, 1, 1)
        self.dateEdit_start = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.gridLayout_3.addWidget(self.dateEdit_start, 1, 2, 1, 1)
        self.pushButton_set_para = QtWidgets.QPushButton(self.tab_para)
        self.pushButton_set_para.setGeometry(QtCore.QRect(360, 330, 75, 23))
        self.pushButton_set_para.setObjectName("pushButton_set_para")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 210, 371, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_kdj_n = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_kdj_n.setGeometry(QtCore.QRect(40, 30, 51, 20))
        self.lineEdit_kdj_n.setObjectName("lineEdit_kdj_n")
        self.lineEdit_kdj_m1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_kdj_m1.setGeometry(QtCore.QRect(160, 30, 51, 20))
        self.lineEdit_kdj_m1.setObjectName("lineEdit_kdj_m1")
        self.lineEdit_kdj_m2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_kdj_m2.setGeometry(QtCore.QRect(270, 30, 51, 20))
        self.lineEdit_kdj_m2.setObjectName("lineEdit_kdj_m2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(140, 30, 21, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(250, 30, 21, 16))
        self.label_16.setObjectName("label_16")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_7.setGeometry(QtCore.QRect(400, 210, 361, 81))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_dmi_n = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_dmi_n.setGeometry(QtCore.QRect(70, 30, 41, 20))
        self.lineEdit_dmi_n.setObjectName("lineEdit_dmi_n")
        self.lineEdit_dmi_m = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_dmi_m.setGeometry(QtCore.QRect(190, 30, 41, 20))
        self.lineEdit_dmi_m.setObjectName("lineEdit_dmi_m")
        self.label_17 = QtWidgets.QLabel(self.groupBox_7)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 31, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_7)
        self.label_18.setGeometry(QtCore.QRect(170, 30, 21, 16))
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab_para, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "指标开关"))
        self.checkBox_ma.setText(QtWidgets.QApplication.translate("MainWindow", "MA"))
        self.checkBox_dmi.setText(QtWidgets.QApplication.translate("MainWindow", "DMI"))
        self.checkBox_macd.setText(QtWidgets.QApplication.translate("MainWindow", "MACD"))
        self.checkBox_kdj.setText(QtWidgets.QApplication.translate("MainWindow", "KDJ"))
        self.checkBox_5.setText(QtWidgets.QApplication.translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(QtWidgets.QApplication.translate("MainWindow", "CheckBox"))
        self.pushButton_draw.setText(QtWidgets.QApplication.translate("MainWindow", "绘图"))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "设置参数"))
        self.label_para.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel"))
        self.label_point.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel"))
        self.label_file.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plot), QtWidgets.QApplication.translate("MainWindow", "行情"))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "MACD参数"))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Short"))
        self.lineEdit_macd_short.setText(QtWidgets.QApplication.translate("MainWindow", "12"))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Long"))
        self.lineEdit_macd_long.setText(QtWidgets.QApplication.translate("MainWindow", "26"))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "M"))
        self.lineEdit_macd_m.setText(QtWidgets.QApplication.translate("MainWindow", "9"))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "MA参数"))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "N1"))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "N3"))
        self.lineEdit_ma_n3.setText(QtWidgets.QApplication.translate("MainWindow", "20"))
        self.lineEdit_ma_n2.setText(QtWidgets.QApplication.translate("MainWindow", "10"))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "N2"))
        self.lineEdit_ma_n1.setText(QtWidgets.QApplication.translate("MainWindow", "5"))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "N4"))
        self.lineEdit_ma_n4.setText(QtWidgets.QApplication.translate("MainWindow", "30"))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "N5"))
        self.lineEdit_ma_n5.setText(QtWidgets.QApplication.translate("MainWindow", "50"))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "算法"))
        self.comboBox_ma.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "MA"))
        self.comboBox_ma.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "EMA"))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "回测文件"))
        self.pushButton_opr_file.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton"))
        self.label_opr.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel"))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "公共参数"))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "周期"))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "合约"))
        self.comboBox_bar.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "0"))
        self.comboBox_bar.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "60"))
        self.comboBox_bar.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "300"))
        self.comboBox_bar.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "600"))
        self.comboBox_bar.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "900"))
        self.comboBox_bar.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "1800"))
        self.comboBox_bar.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "3600"))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "开始时间"))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "结束时间"))
        self.pushButton_set_para.setText(QtWidgets.QApplication.translate("MainWindow", "设置"))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("MainWindow", "KDJ参数"))
        self.lineEdit_kdj_n.setText(QtWidgets.QApplication.translate("MainWindow", "9"))
        self.lineEdit_kdj_m1.setText(QtWidgets.QApplication.translate("MainWindow", "3"))
        self.lineEdit_kdj_m2.setText(QtWidgets.QApplication.translate("MainWindow", "3"))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "N"))
        self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "M1"))
        self.label_16.setText(QtWidgets.QApplication.translate("MainWindow", "M2"))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("MainWindow", "DMI参数"))
        self.lineEdit_dmi_n.setText(QtWidgets.QApplication.translate("MainWindow", "14"))
        self.lineEdit_dmi_m.setText(QtWidgets.QApplication.translate("MainWindow", "6"))
        self.label_17.setText(QtWidgets.QApplication.translate("MainWindow", "N"))
        self.label_18.setText(QtWidgets.QApplication.translate("MainWindow", "M"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_para), QtWidgets.QApplication.translate("MainWindow", "参数设置"))

