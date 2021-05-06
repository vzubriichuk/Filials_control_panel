# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filial_cp.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 521, 101))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.btn_report_info = QtWidgets.QPushButton(self.groupBox)
        self.btn_report_info.setGeometry(QtCore.QRect(10, 60, 181, 31))
        self.btn_report_info.setStyleSheet("background-color:#525252;\n"
"font-weight:bold;\n"
"color:#FFFFFF;\n"
"")
        self.btn_report_info.setObjectName("btn_report_info")
        self.reports_dropdown = QtWidgets.QComboBox(self.groupBox)
        self.reports_dropdown.setGeometry(QtCore.QRect(10, 30, 391, 24))
        self.reports_dropdown.setObjectName("reports_dropdown")
        self.reports_dropdown.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 170, 521, 201))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.table_active_filials = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_active_filials.setGeometry(QtCore.QRect(10, 20, 501, 141))
        self.table_active_filials.setObjectName("table_active_filials")
        self.table_active_filials.setColumnCount(3)
        self.table_active_filials.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_active_filials.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_active_filials.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        self.table_active_filials.setHorizontalHeaderItem(2, item)
        self.btn_remove = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_remove.setGeometry(QtCore.QRect(10, 170, 151, 24))
        self.btn_remove.setStyleSheet("background-color:#a83e32;\n"
"font-weight:bold;\n"
"color:#FFFFFF;\n"
"")
        self.btn_remove.setObjectName("btn_remove")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 380, 521, 211))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.table_all_filials = QtWidgets.QTableWidget(self.groupBox_3)
        self.table_all_filials.setGeometry(QtCore.QRect(10, 20, 501, 151))
        self.table_all_filials.setObjectName("table_all_filials")
        self.table_all_filials.setColumnCount(3)
        self.table_all_filials.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_all_filials.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_all_filials.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_all_filials.setHorizontalHeaderItem(2, item)
        self.btn_add = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_add.setGeometry(QtCore.QRect(10, 180, 151, 24))
        self.btn_add.setStyleSheet("background-color:#6da832;\n"
"font-weight:bold;\n"
"color:#FFFFFF;\n"
"")
        self.btn_add.setObjectName("btn_add")
        self.lbl_version = QtWidgets.QLabel(self.centralwidget)
        self.lbl_version.setGeometry(QtCore.QRect(480, 10, 41, 16))
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_ver_num = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ver_num.setGeometry(QtCore.QRect(520, 10, 31, 16))
        self.lbl_ver_num.setObjectName("lbl_ver_num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панель управления филиалами в отчетах"))
        self.groupBox.setTitle(_translate("MainWindow", "Выберите отчёт"))
        self.btn_report_info.setText(_translate("MainWindow", "Просмотреть информацию"))
        self.reports_dropdown.setItemText(0, _translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Активные филиалы"))
        item = self.table_active_filials.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Выбрать"))
        item = self.table_active_filials.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Филиал"))
        item = self.table_active_filials.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Название филиала"))
        self.btn_remove.setText(_translate("MainWindow", "Исключить выбранное"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Доступные филиалы"))
        item = self.table_all_filials.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Выбрать"))
        item = self.table_all_filials.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Филиал"))
        item = self.table_all_filials.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Название филиала"))
        self.btn_add.setText(_translate("MainWindow", "Добавить выбранное"))
        self.lbl_version.setText(_translate("MainWindow", "Версия:"))
        self.lbl_ver_num.setText(_translate("MainWindow", "1.0"))
