#!/usr/bin/env python
# coding:utf-8
"""
Author : Vitaliy Zubriichuk
Contact : v@zubr.kiev.ua
Time    : 30.04.2021 9:14
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from gui.filial_cp import Ui_MainWindow
from pyodbc import Error as SQLError
from log_error import writelog
from singleinstance import Singleinstance
from db_connect import DBConnect
import access
import sys
import os

# connection properties
db_info = access.conn_info
sql = DBConnect(server=db_info.get('Server'),
                 db=db_info.get('DB'),
                 uid=db_info.get('UID'),
                 pwd=db_info.get('PWD'))


LastStateRole = QtCore.Qt.UserRole


# main app
class FilialApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('resources/admin.png'))

        self.report_id = int
        self.filials = dict
        self.all_filials = dict

        # loading list of reports
        try:
            with sql:
                self.report_list = dict(sql.get_reports())
                for key, values in self.report_list.items():
                    self.reports_dropdown.addItem(values)

        except Exception as error:
            writelog(error)

        self.btn_report_info.clicked.connect(self.data_load)
        self.btn_remove.clicked.connect(self.remove)

    # load info from choosing report
    def data_load(self):
        for k, v in self.report_list.items():
            if v == self.reports_dropdown.currentText():
                self.report_id = k
        try:
            with sql:
                self.filials = dict(sql.get_report_info(self.report_id))
        except Exception as error:
            writelog(error)

        if len(self.filials) == 0:
            print('nema info')
        else:
            # run loading filials
            self.load_filial()

    # load active filials from aid_FilialsAll
    def load_filial(self):
        try:
            with sql:
                self.all_filials = dict(sql.get_all_filials(self.report_id))
        except Exception as error:
            writelog(error)

        # insert rows into active filials window
        self.insert_into(self.table_active_filials, self.filials)

        # insert rows into all filials window
        self.insert_into(self.table_all_filials, self.all_filials)


    @staticmethod
    def insert_into(widget, lists):
        try:
            # create basic table window
            # widget.removeRow(0)
            countRows = len(lists)
            widget.setRowCount(countRows)
            for row in range(countRows):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                item.setData(LastStateRole, item.checkState())
                widget.setColumnWidth(0, 60)
                widget.setColumnWidth(1, 50)
                widget.setColumnWidth(2, 374)
                widget.setItem(row, 0, item)

                # insert values into table
                rows = 0
                for tup in list(lists.items()):
                    col = 1
                    for i in tup:
                        cell = QTableWidgetItem(str(i))
                        widget.setItem(rows, col, cell)
                        widget.setRowHeight(rows, 5)
                        cell_align = widget.item(rows, 1)
                        cell_align.setTextAlignment(QtCore.Qt.AlignCenter)
                        col += 1
                    rows += 1
        except Exception as error:
            writelog(error)


    def remove(self):
        print(len(self.filials))
        for i in range(0, len(self.filials)):
            print(i)
            self.table_active_filials.removeRow(i)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = FilialApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    try:
        fname = os.path.basename(__file__)
        myapp = Singleinstance(fname)
        if myapp.alreadyrunning():
            sys.exit()
        main()
    except Exception as e:
        writelog(e)
    finally:
        sys.exit()