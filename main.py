import sys
import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
import design.resources
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDialog
from PyQt6.QtSql import QSqlTableModel
from design.main_design import Ui_MainWindow
from design.dialog_new import Ui_Dialog_New
from design.dialog_edit import Ui_Dialog_Edit
from connection import Data

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect_db = Data()
        self.connect_db.create_connection()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view_data(self.connect_db.select_table_name()[0])
        #self.setFixedSize(QSize(400, 300))
        self.ui.btn_new_entry.clicked.connect(self.open_dialog_new_window)
        self.ui.btn_edit_entry.clicked.connect(self.open_dialog_edit_window)
        self.ui.btn_del_entry.clicked.connect(self.delete_current_record)
        self.ui.comboBox_name_tables.currentTextChanged.connect(self.view_data)
    
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
    window.show()
    app.exec()