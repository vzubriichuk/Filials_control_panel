#!/usr/bin/env python
# coding:utf-8
"""
Author : Vitaliy Zubriichuk
Contact : v@zubr.kiev.ua
Time    : 30.04.2021 9:14
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from gui.filial_cp import Ui_MainWindow
from gui.splash_screen import Ui_SplashScreen
# from pyodbc import Error as SQLError
from log_error import writelog
from singleinstance import Singleinstance
from db_connect import DBConnect
from _version import __version__
import access
import sys
import os
import getpass

# connection properties
db_info = access.conn_info
sql = DBConnect(server=db_info.get('Server'),
                 db=db_info.get('DB'),
                 uid=db_info.get('UID'),
                 pwd=db_info.get('PWD'))


LastStateRole = QtCore.Qt.UserRole


def _add_user_label(self):
    """ Adds user name in top right corner. """
    user_label = tk.Label(parent, text='Пользователь: ' +
                                       self.user_info.ShortUserName + '  Версия ' + __version__,
                          font=('Arial', 8))
    user_label.pack(side=tk.RIGHT, anchor=tk.NE)


class PopupInfoWindows(QWidget):
    def __init__(self):
        super().__init__()

    # def popup_add_user_succesfull(self):
    #     QMessageBox.information(self, 'Добавление пользователя',
    #                             'Пользователь успешно добавлен',
    #                             QMessageBox.Ok, QMessageBox.Ok)
    #
    def checked_error(self):
        QMessageBox.critical(self, 'Ошибка',
                             'Филиал не был выбран',
                             QMessageBox.Ok, QMessageBox.Ok)

    def remove_error(self):
        QMessageBox.critical(self, 'Ошибка',
                             'Ошибка при удалении филиала',
                             QMessageBox.Ok, QMessageBox.Ok)
    def add_error(self):
        QMessageBox.critical(self, 'Ошибка',
                             'Ошибка при добавлении филиала',
                             QMessageBox.Ok, QMessageBox.Ok)

    def popup_remove_filid_succesfull(self):
        QMessageBox.information(self, 'Удаление филиалов',
                                'Выбранные филиалы были успешно удалены.',
                                QMessageBox.Ok, QMessageBox.Ok)

    def popup_add_filid_succesfull(self):
        QMessageBox.information(self, 'Добавление филиалов',
                                'Выбранные филиалы были успешно добавлены.',
                                QMessageBox.Ok, QMessageBox.Ok)


class SplashScreen(QtWidgets.QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('resources/admin.png'))

# main app
class FilialApp(QtWidgets.QMainWindow, Ui_MainWindow, PopupInfoWindows):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('resources/admin.png'))
        _translate = QtCore.QCoreApplication.translate

        self.report_id = int
        self.filials = 0
        self.all_filials = dict
        self.user = getpass.getuser()
        # show user login in main window
        self.lbl_ver_num.setText(_translate("MainWindow", __version__))

        # loading list of reports
        try:
            with sql:
                self.report_list = dict(sql.get_reports())
                for key, values in self.report_list.items():
                    self.reports_dropdown.addItem(values)

        except Exception as error:
            writelog(error)

        self.btn_report_info.clicked.connect(self.data_load)
        self.btn_remove.clicked.connect(self.check_rows_remove)
        self.btn_add.clicked.connect(self.check_rows_add)

    # load info from choosing report
    def data_load(self):
        # print(len(self.filials))
        for k, v in self.report_list.items():
            if v == self.reports_dropdown.currentText():
                self.report_id = k
        try:
            # clear table if report not have info
            if self.filials != 0:
                self.remove_rows()
            with sql:
                self.filials = dict(sql.get_report_info(self.report_id))
                self.load_all_filial()  # Attempt to use a closed connection.
        except Exception as error:
            writelog(error)
            pass
            
        if len(self.filials) == 0:
            self.remove_rows()
            self.load_all_filial()
        else:
            # run loading filials
            self.load_all_filial()

    # load active filials from aid_FilialsAll
    def load_all_filial(self):
        try:
            with sql:
                self.all_filials = dict(sql.get_all_filials(self.report_id))
        except Exception as error:
            writelog(error)

        # insert rows into active filials window
        if len(self.filials.keys()) > 5:  # если больше 5 филиалов = горизонтальный скролл
            self.insert_into(self.table_active_filials, self.filials, 60, 50,
                             357)
        else:
            self.insert_into(self.table_active_filials, self.filials, 60, 50, 374)
        # insert rows into all filials window
        self.insert_into(self.table_all_filials, self.all_filials, 60, 50, 350)

    @staticmethod
    def insert_into(widget, lists, wCol1, wCol2, wCol3):
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
                widget.setColumnWidth(0, wCol1)
                widget.setColumnWidth(1, wCol2)
                widget.setColumnWidth(2, wCol3)
                widget.setItem(row, 0, item)

                # insert values into table
                rows = 0
                for tup in list(lists.items()):
                    col = 1
                    for i in tup:
                        cell = QTableWidgetItem(str(i))
                        widget.setItem(rows, col, cell)
                        widget.setRowHeight(rows, 10)
                        cell_align = widget.item(rows, 1)
                        cell_align.setTextAlignment(QtCore.Qt.AlignCenter)
                        col += 1
                    rows += 1
        except Exception as error:
            writelog(error)

    def remove_rows(self):
        for i in range(len(self.filials)):
            row = 0
            self.table_active_filials.removeRow(row)
        for i in range(len(self.all_filials)):
            row = 0
            self.table_all_filials.removeRow(row)

    # функция удаления филиалов из активного списка
    def check_rows_remove(self):
        try:
            FilID = []
            countRows = len(self.filials)
            for i in range(countRows):
                checkboxItem = self.table_active_filials.item(i, 0)
                currentState = checkboxItem.checkState()
                if currentState == QtCore.Qt.Checked:
                    # add checked FilID to list
                    FilID.append(self.table_active_filials.item(i, 1).text())
            ListFilID = ', '.join(FilID)
            if ListFilID is not None and len(ListFilID) != 0:
                try:
                    with sql:
                        status = sql.remove_filials(self.report_id, ListFilID, self.user)
                        if status[0] == 1:
                            self.popup_remove_filid_succesfull()
                        elif status == 0:
                            self.remove_error()
                    self.data_load()
                except Exception as error:
                    writelog(error)
            else:
                self.checked_error()
        except Exception as error:
            writelog(error)
            self.checked_error()

    # функция добавления филиалов в активный список
    def check_rows_add(self):
        try:
            FilID = []
            countRows = len(self.all_filials)
            for i in range(countRows):
                checkboxItem = self.table_all_filials.item(i, 0)
                currentState = checkboxItem.checkState()
                if currentState == QtCore.Qt.Checked:
                    # add checked FilID to list
                    FilID.append(self.table_all_filials.item(i, 1).text())
            ListFilID = ', '.join(FilID)
            if ListFilID is not None and len(ListFilID) != 0:
                try:
                    with sql:
                        status = sql.add_filials(self.report_id, ListFilID, self.user)
                        if status[0] == 1:
                            self.popup_add_filid_succesfull()
                        elif status == 0:
                            self.add_error()
                    self.data_load()
                except Exception as error:
                    writelog(error)
            else:
                self.checked_error()
        except Exception as error:
            writelog(error)
            self.checked_error()





def main():
    # splash screen
    splash = QtWidgets.QApplication(sys.argv)
    splash_window = SplashScreen()
    splash_window.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    splash_window.show()
    QTimer.singleShot(5000, splash.quit)
    splash.exec_()

    # main app
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = FilialApp()  # Создаём объект класса FilialApp
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