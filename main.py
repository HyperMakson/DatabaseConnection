import sys
import pyodbc
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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_db = Data()
        self.view_data()
        #self.setFixedSize(QSize(400, 300))
        self.ui.btn_new_entry.clicked.connect(self.open_dialog_new_window)
        self.ui.btn_edit_entry.clicked.connect(self.open_dialog_edit_window)
        self.ui.btn_del_entry.clicked.connect(self.delete_current_record)
    
    def open_dialog_new_window(self):
        self.new_window = QDialog()
        self.ui_new_window = Ui_Dialog_New()
        self.ui_new_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_new_window.btn_new_entry.clicked.connect(self.add_new_record)
    
    def add_new_record(self):
        text1 = self.ui_new_window.lineEdit.text()
        text2 = self.ui_new_window.lineEdit_2.text()
        text3 = int(self.ui_new_window.lineEdit_3.text())
        text4 = int(self.ui_new_window.lineEdit_4.text())
        self.connect_db.new_record_query(text1, text2, text3, text4)
        self.view_data()
        self.new_window.close()
    
    def open_dialog_edit_window(self):
        self.edit_window = QDialog()
        self.ui_edit_window = Ui_Dialog_Edit()
        self.ui_edit_window.setupUi(self.edit_window)
        self.edit_window.show()
        self.ui_edit_window.btn_edit_entry.clicked.connect(self.edit_current_record)
    
    def edit_current_record(self):
        index = self.ui.view_records.selectedIndexes()[0]
        id = int(self.ui.view_records.model().data(index))
        text1 = self.ui_edit_window.lineEdit.text()
        text2 = self.ui_edit_window.lineEdit_2.text()
        text3 = int(self.ui_edit_window.lineEdit_3.text())
        text4 = int(self.ui_edit_window.lineEdit_4.text())
        self.connect_db.edit_record_query(text1, text2, text3, text4, id)
        self.view_data()
        self.edit_window.close()
    
    def delete_current_record(self):
        index = self.ui.view_records.selectedIndexes()[0]
        id = int(self.ui.view_records.model().data(index))
        self.connect_db.del_record_query(id)
        self.view_data()
    
    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Products')
        self.model.select()
        self.ui.view_records.setModel(self.model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()