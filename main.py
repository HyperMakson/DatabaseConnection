import sys
import pyodbc
import socket
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
import design.resources
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDialog
from PyQt6.QtSql import QSqlTableModel
from design.main_design import Ui_MainWindow
from design.dialog_new import Ui_Dialog_New
from design.dialog_edit import Ui_Dialog_Edit
from design.log_pass import Ui_Dialog_Auth
from connection import Data

class Authentication(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_auth_window = Ui_Dialog_Auth()
        self.ui_auth_window.setupUi(self)
        self.ui_auth_window.btn_auth.clicked.connect(self.check_auth)
        self.ui_auth_window.comboBox_type_connect.currentTextChanged.connect(self.change_type)
    
    def change_type(self):
        self.type_connection = self.ui_auth_window.comboBox_type_connect.currentText()
        if self.type_connection == "Windows Authentication":
            self.ui_auth_window.lineEdit.setDisabled(True)
            self.ui_auth_window.lineEdit_2.setDisabled(True)
            self.ui_auth_window.label.setStyleSheet("background-color: rgba(168, 216, 234, 50%);\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.label_2.setStyleSheet("background-color: rgba(168, 216, 234, 50%);\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.lineEdit.setStyleSheet("background-color: rgba(234, 255, 208, 50%);\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.lineEdit_2.setStyleSheet("background-color: rgba(234, 255, 208, 50%);\n"
                                     "border: 1px solid gray;")
        else:
            self.ui_auth_window.lineEdit.setEnabled(True)
            self.ui_auth_window.lineEdit_2.setEnabled(True)
            self.ui_auth_window.label.setStyleSheet("background-color: #A8D8EA;\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.label_2.setStyleSheet("background-color: #A8D8EA;\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.lineEdit.setStyleSheet("background-color: #EAFFD0;\n"
                                     "border: 1px solid state black;")
            self.ui_auth_window.lineEdit_2.setStyleSheet("background-color: #EAFFD0;\n"
                                     "border: 1px solid state black;")
    
    def check_auth(self):
        self.type_connection = self.ui_auth_window.comboBox_type_connect.currentText()
        self.auth_db = Data()
        if self.type_connection == "Windows Authentication":
            print(socket.gethostname())
            check = self.auth_db.create_connection()
        else:
            self.log = self.ui_auth_window.lineEdit.text()
            self.password = self.ui_auth_window.lineEdit_2.text()
            check = self.auth_db.create_connection_with_sql(self.log, self.password)
        if check == True:
            print("Connection succesfull")
            window.start_main()
        else:
            QtWidgets.QMessageBox.critical(None, "Failed connection", "Не удалось подключиться к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect_db = Data()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_new_entry.clicked.connect(self.open_dialog_new_window)
        self.ui.btn_edit_entry.clicked.connect(self.open_dialog_edit_window)
        self.ui.btn_del_entry.clicked.connect(self.delete_current_record)
        self.ui.comboBox_name_tables.currentTextChanged.connect(self.view_data)
    
    def start_main(self):
        self.ui.comboBox_name_tables.addItems(self.connect_db.select_table_name())
        self.view_data(self.connect_db.select_table_name()[0])
        window.show()
        auth_window.close()
    
    def open_dialog_new_window(self):
        self.table = self.ui.comboBox_name_tables.currentText()
        self.column = self.connect_db.select_column_name(self.table)
        self.new_window = QDialog()
        self.ui_new_window = Ui_Dialog_New()
        self.ui_new_window.setupUi(self.new_window, self.table)
        self.new_window.show()
        self.ui_new_window.btn_new_entry.clicked.connect(self.add_new_record)
    
    def add_new_record(self):
        dict_obj_text = self.ui_new_window.dict_obj_name
        arr_add_text = []
        for text_edit, type_data in dict_obj_text.items():
            text = getattr(self.ui_new_window, text_edit)
            if type_data == 'bigint' or type_data == 'bit' or type_data == 'smallint' or type_data == 'int' or type_data == 'tinyint':
                add_text = int(text.text())
                arr_add_text.append(add_text)
            elif type_data == 'float' or type_data == 'real'  or type_data == 'money' or type_data == 'smallmoney' or type_data == 'numeric' or type_data == 'decimal' :
                add_text = float(text.text())
                arr_add_text.append(add_text)
            else:
                add_text = text.text()
                arr_add_text.append(add_text)
        self.connect_db.new_record_query(self.table, self.column, arr_add_text)
        self.view_data(self.table)
        self.new_window.close()
    
    def open_dialog_edit_window(self):
        selection_model = self.ui.view_records.selectionModel()
        if selection_model.hasSelection() is False:
            QtWidgets.QMessageBox.information(None, "No id selected", "Сначала нужно выбрать id в таблице", QtWidgets.QMessageBox.StandardButton.Cancel)
        else:
            self.table = self.ui.comboBox_name_tables.currentText()
            self.column = self.connect_db.select_column_name(self.table)
            self.index = self.ui.view_records.selectedIndexes()[0]
            try:
                self.id = int(self.ui.view_records.model().data(self.index))
                self.edit_window = QDialog()
                self.ui_edit_window = Ui_Dialog_Edit()
                self.ui_edit_window.setupUi(self.edit_window, self.table, self.id)
                self.edit_window.show()
                self.ui_edit_window.btn_edit_entry.clicked.connect(self.edit_current_record)
            except:
                QtWidgets.QMessageBox.critical(None, "Incorrect id", "Неправильно выбрано id", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def edit_current_record(self):
        dict_obj_text = self.ui_edit_window.dict_obj_name
        arr_edit_text = []
        for text_edit, type_data in dict_obj_text.items():
            text = getattr(self.ui_edit_window, text_edit)
            if type_data == 'bigint' or type_data == 'bit' or type_data == 'smallint' or type_data == 'int' or type_data == 'tinyint':
                edit_text = int(text.text())
                arr_edit_text.append(edit_text)
            elif type_data == 'float' or type_data == 'real'  or type_data == 'money' or type_data == 'smallmoney' or type_data == 'numeric' or type_data == 'decimal' :
                edit_text = float(text.text())
                arr_edit_text.append(edit_text)
            else:
                edit_text = text.text()
                arr_edit_text.append(edit_text)
        arr_edit_text.append(self.id)
        self.connect_db.edit_record_query(self.table, self.column, arr_edit_text)
        self.view_data(self.table)
        self.edit_window.close()
    
    def delete_current_record(self):
        selection_model = self.ui.view_records.selectionModel()
        if selection_model.hasSelection() is False:
            QtWidgets.QMessageBox.information(None, "No id selected", "Сначала нужно выбрать id в таблице", QtWidgets.QMessageBox.StandardButton.Cancel)
        else:
            self.table = self.ui.comboBox_name_tables.currentText()
            self.column = self.connect_db.select_column_name(self.table)
            index = self.ui.view_records.selectedIndexes()[0]
            try:
                id = int(self.ui.view_records.model().data(index))
                self.connect_db.del_record_query(self.table, self.column, id)
                self.view_data(self.table)
            except:
                QtWidgets.QMessageBox.critical(None, "Incorrect id", "Неправильно выбрано id", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def view_data(self, s):
        print(s)
        self.model = QSqlTableModel(self)
        self.model.setTable(s)
        self.model.select()
        #self.ui.view_records.setColumnHidden(0, True)
        self.ui.view_records.setModel(self.model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    auth_window = Authentication()
    auth_window.show()
    app.exec()