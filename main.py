import sys
import socket
from PyQt6 import QtWidgets
import design.resources
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
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
            self.ui_auth_window.lineEdit_3.setEnabled(True)
            self.ui_auth_window.lineEdit.setDisabled(True)
            self.ui_auth_window.lineEdit_2.setDisabled(True)
            self.ui_auth_window.label_3.setStyleSheet("background-color: #A8D8EA;\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.label.setStyleSheet("background-color: rgba(168, 216, 234, 50%);\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.label_2.setStyleSheet("background-color: rgba(168, 216, 234, 50%);\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.lineEdit_3.setStyleSheet("background-color: #EAFFD0;\n"
                                     "border: 1px solid state black;")
            self.ui_auth_window.lineEdit.setStyleSheet("background-color: rgba(234, 255, 208, 50%);\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.lineEdit_2.setStyleSheet("background-color: rgba(234, 255, 208, 50%);\n"
                                     "border: 1px solid gray;")
        else:
            self.ui_auth_window.lineEdit_3.setEnabled(True)
            self.ui_auth_window.lineEdit.setEnabled(True)
            self.ui_auth_window.lineEdit_2.setEnabled(True)
            self.ui_auth_window.label_3.setStyleSheet("background-color: #A8D8EA;\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.label.setStyleSheet("background-color: #A8D8EA;\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.label_2.setStyleSheet("background-color: #A8D8EA;\n"
                                     "border: 1px solid gray;")
            self.ui_auth_window.lineEdit_3.setStyleSheet("background-color: #EAFFD0;\n"
                                     "border: 1px solid state black;")
            self.ui_auth_window.lineEdit.setStyleSheet("background-color: #EAFFD0;\n"
                                     "border: 1px solid state black;")
            self.ui_auth_window.lineEdit_2.setStyleSheet("background-color: #EAFFD0;\n"
                                     "border: 1px solid state black;")
    
    def check_auth(self):
        self.type_connection = self.ui_auth_window.comboBox_type_connect.currentText()
        self.server = self.ui_auth_window.lineEdit_3.text() + ",1433"
        self.auth_db = Data()
        if self.type_connection == "Windows Authentication":
            self.user = socket.gethostname()
            check = self.auth_db.create_connection(self.server)
        else:
            self.log = self.ui_auth_window.lineEdit.text()
            self.password = self.ui_auth_window.lineEdit_2.text()
            self.user = self.log
            check = self.auth_db.create_connection_with_sql(self.server, self.log, self.password)
        if check == True:
            print("Connection succesfull")
            window.start_main(self.user)
        else:
            QtWidgets.QMessageBox.critical(None, "Failed connection", "Не удалось подключиться к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect_db = Data()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def start_main(self, user):
        self.ui.label_user.setText(f"Пользователь: {user}")
        self.ui.comboBox_name_tables.addItems(self.connect_db.select_table_name())
        self.view_data(self.connect_db.select_table_name()[0])
        self.ui.btn_new_entry.clicked.connect(self.open_dialog_new_window)
        self.ui.btn_edit_entry.clicked.connect(self.open_dialog_edit_window)
        self.ui.btn_del_entry.clicked.connect(self.delete_current_record)
        self.ui.comboBox_name_tables.currentTextChanged.connect(self.view_data)
        check_role = self.connect_db.check_server_role()
        if check_role[0] == "yes":
            self.ui.btn_new_entry.setEnabled(True)
            self.ui.btn_edit_entry.setEnabled(True)
            self.ui.btn_del_entry.setEnabled(True)
        else:
            self.ui.btn_new_entry.setDisabled(True)
            self.ui.btn_edit_entry.setDisabled(True)
            self.ui.btn_del_entry.setDisabled(True)
            self.ui.btn_new_entry.setStyleSheet("background-color: rgba(170, 150, 218, 50%);\n"
                                                "border-radius: 10px;\n"
                                                "color: #FCE38A;\n"
                                                "font-size: 14px;\n"
                                                "border: 1px solid white;")
            self.ui.btn_edit_entry.setStyleSheet("background-color: rgba(170, 150, 218, 50%);\n"
                                                "border-radius: 10px;\n"
                                                "color: #FCE38A;\n"
                                                "font-size: 14px;\n"
                                                "border: 1px solid white;")
            self.ui.btn_del_entry.setStyleSheet("background-color: rgba(170, 150, 218, 50%);\n"
                                                "border-radius: 10px;\n"
                                                "color: #FCE38A;\n"
                                                "font-size: 14px;\n"
                                                "border: 1px solid white;")
        window.show()
        auth_window.close()
    
    def open_dialog_new_window(self):
        self.table = self.ui.comboBox_name_tables.currentText()
        self.column = self.connect_db.select_column_name(self.table)
        self.new_window = QDialog()
        self.ui_new_window = Ui_Dialog_New()
        self.ui_new_window.setupUi(self.new_window, self.table)
        self.new_window.setModal(True)
        self.new_window.show()
        self.ui_new_window.btn_new_entry.clicked.connect(self.add_new_record)
    
    def add_new_record(self):
        dict_obj_text = self.ui_new_window.dict_obj_name
        arr_add_text = []
        for text_edit, type_data in dict_obj_text.items():
            text = getattr(self.ui_new_window, text_edit)
            if type_data == 'bigint' or type_data == 'smallint' or type_data == 'int' or type_data == 'tinyint':
                if text_edit[:-2] == "comboBox_keys":
                    add_text = int(text.currentText())
                else:
                    try:
                        add_text = int(text.text())
                    except ValueError:
                        add_text = text.text()
                arr_add_text.append(add_text)
            elif type_data == 'bit':
                if text_edit[:-2] == "comboBox_keys":
                    add_text = text.currentText()
                else:
                    add_text = text.currentText()
                arr_add_text.append(add_text)
            elif type_data == 'float' or type_data == 'real'  or type_data == 'money' or type_data == 'smallmoney' or type_data == 'numeric' or type_data == 'decimal':
                if text_edit[:-2] == "comboBox_keys":
                    add_text = float(text.currentText())
                else:
                    add_text = float(text.text())
                arr_add_text.append(add_text)
            elif type_data == 'datetime' or type_data == 'datetime2'  or type_data == 'datetimeoffset' or type_data == 'smalldatetime':
                if text_edit[:-2] == "comboBox_keys":
                    add_text = text.currentText()
                else:
                    add_text = text.dateTime()
                    #add_text = text.dateTime().toString('dd-MM-yyyy')
                arr_add_text.append(add_text)
            elif type_data == 'date':
                if text_edit[:-2] == "comboBox_keys":
                    add_text = text.currentText()
                else:
                    add_text = text.date()
                arr_add_text.append(add_text)
            elif type_data == 'time':
                if text_edit[:-2] == "comboBox_keys":
                    add_text = text.currentText()
                else:
                    add_text = text.time()
                arr_add_text.append(add_text)
            else:
                if text_edit[:-2] == "comboBox_keys":
                    add_text = text.currentText()
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
                self.edit_window.setModal(True)
                self.edit_window.show()
                self.ui_edit_window.btn_edit_entry.clicked.connect(self.edit_current_record)
            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.critical(None, "Incorrect id", "Неправильно выбрано id", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def edit_current_record(self):
        dict_obj_text = self.ui_edit_window.dict_obj_name
        arr_edit_text = []
        for text_edit, type_data in dict_obj_text.items():
            text = getattr(self.ui_edit_window, text_edit)
            if type_data == 'bigint' or type_data == 'smallint' or type_data == 'int' or type_data == 'tinyint':
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = int(text.currentText())
                else:
                    try:
                        edit_text = int(text.text())
                    except ValueError:
                        edit_text = text.text()
                arr_edit_text.append(edit_text)
            elif type_data == 'bit':
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = text.currentText()
                else:
                    edit_text = text.currentText()
                arr_edit_text.append(edit_text)
            elif type_data == 'float' or type_data == 'real'  or type_data == 'money' or type_data == 'smallmoney' or type_data == 'numeric' or type_data == 'decimal':
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = float(text.currentText())
                else:
                    edit_text = float(text.text())
                arr_edit_text.append(edit_text)
            elif type_data == 'datetime' or type_data == 'datetime2'  or type_data == 'datetimeoffset' or type_data == 'smalldatetime':
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = text.currentText()
                else:
                    edit_text = text.dateTime()
                    #edit_text = text.dateTime().toString('dd-MM-yyyy')
                arr_edit_text.append(edit_text)
            elif type_data == 'date':
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = text.currentText()
                else:
                    edit_text = text.date()
                arr_edit_text.append(edit_text)
            elif type_data == 'time':
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = text.currentText()
                else:
                    edit_text = text.time()
                arr_edit_text.append(edit_text)
            else:
                if text_edit[:-2] == "comboBox_keys":
                    edit_text = text.currentText()
                else:
                    edit_text = text.text()
                arr_edit_text.append(edit_text)
        first_type = next(iter(dict_obj_text.values()))
        if first_type == 'bigint' or first_type == 'bit' or first_type == 'smallint' or first_type == 'int' or first_type == 'tinyint':
            arr_edit_text.append(self.id)
        elif first_type == 'float' or first_type == 'real'  or first_type == 'money' or first_type == 'smallmoney' or first_type == 'numeric' or first_type == 'decimal':
            arr_edit_text.append(float(self.id))
        else:
            arr_edit_text.append(str(self.id))
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
            self.type = self.connect_db.select_data_type(self.table)
            index = self.ui.view_records.selectedIndexes()[0]
            try:
                id = int(self.ui.view_records.model().data(index))
                first_type = self.type[0]
                if first_type == 'bigint' or first_type == 'bit' or first_type == 'smallint' or first_type == 'int' or first_type == 'tinyint':
                    id = int(id)
                elif first_type == 'float' or first_type == 'real'  or first_type == 'money' or first_type == 'smallmoney' or first_type == 'numeric' or first_type == 'decimal':
                    id = float(id)
                else:
                    id = str(id)
                self.connect_db.del_record_query(self.table, self.column, id)
                self.view_data(self.table)
            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.critical(None, "Incorrect id", "Неправильно выбрано id", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def view_data(self, s):
        self.model = QSqlTableModel(self)
        self.model.setTable(s)
        self.model.select()
        #self.ui.view_records.setColumnHidden(0, True)
        self.ui.view_records.setModel(self.model)
        self.ui.view_records.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    auth_window = Authentication()
    auth_window.show()
    app.exec()