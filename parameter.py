# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created: Sat Jul 21 16:49:46 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(398, 494)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 351, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout_2.addWidget(self.dateEdit_2, 1, 4, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(110, 30, 54, 12))
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)
        self.lineEdit_ma_n3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n3.setObjectName("lineEdit_ma_n3")
        self.gridLayout.addWidget(self.lineEdit_ma_n3, 0, 5, 1, 1)
        self.lineEdit_ma_n2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n2.setObjectName("lineEdit_ma_n2")
        self.gridLayout.addWidget(self.lineEdit_ma_n2, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.lineEdit_ma_n1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n1.setObjectName("lineEdit_ma_n1")
        self.gridLayout.addWidget(self.lineEdit_ma_n1, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_ma_n4 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n4.setObjectName("lineEdit_ma_n4")
        self.gridLayout.addWidget(self.lineEdit_ma_n4, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_ma_n5 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_ma_n5.setObjectName("lineEdit_ma_n5")
        self.gridLayout.addWidget(self.lineEdit_ma_n5, 1, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 4, 1, 1)
        self.comboBox_ma = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_ma.setObjectName("comboBox_ma")
        self.comboBox_ma.addItem("")
        self.comboBox_ma.addItem("")
        self.gridLayout.addWidget(self.comboBox_ma, 1, 5, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "公共参数", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "周期", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "合约", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "300", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form", "900", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Form", "1800", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Form", "3600", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "开始时间", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "结束时间", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "回测文件", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "MA参数", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "N1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "N3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "N2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "N4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "N5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "算法", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ma.setItemText(0, QtGui.QApplication.translate("Form", "MA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ma.setItemText(1, QtGui.QApplication.translate("Form", "EMA", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "MACD参数", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "取消", None, QtGui.QApplication.UnicodeUTF8))

