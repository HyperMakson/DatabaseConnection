from PyQt6 import QtCore, QtGui, QtWidgets
import design.resources
from connection import Data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #A8D8EA;\n"
"font-family: arial rounded mt bold;")
        MainWindow.setWindowIcon(QtGui.QIcon(":/icon/icons/database_FILL0_wght400_GRAD0_opsz24.svg"))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_icon = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_icon.setMaximumSize(QtCore.QSize(26, 50))
        self.label_icon.setStyleSheet("background-color: #FCE38A;\n"
"border-radius: 10px;\n"
"border: 1px solid black;")
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(":/icon/icons/database_FILL0_wght400_GRAD0_opsz24.svg"))
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_2.addWidget(self.label_icon)
        self.label_main_name = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("arial rounded mt 13")
        font.setPointSize(20)
        font.setBold(True)
        self.label_main_name.setFont(font)
        self.label_main_name.setStyleSheet("background-color: #AA96DA;\n"
"border-radius: 10px;\n"
"color: #FCE38A;\n"
"border: 1px solid white;")
        self.label_main_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_main_name.setObjectName("label_main_name")
        self.horizontalLayout_2.addWidget(self.label_main_name)
        self.label_user = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_user.setMinimumSize(QtCore.QSize(0, 0))
        self.label_user.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("arial rounded mt 13")
        font.setBold(True)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("background-color: #F08A5D;\n"
"border-radius: 10px;\n"
"color: #112D4E;\n"
"border: 1px solid white;")
        self.label_user.setObjectName("label_user")
        self.horizontalLayout_2.addWidget(self.label_user)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_new_entry = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_new_entry.setEnabled(True)
        self.btn_new_entry.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("arial rounded mt 13")
        font.setBold(True)
        self.btn_new_entry.setFont(font)
        self.btn_new_entry.setStyleSheet("QPushButton {\n"
"background-color: #AA96DA;\n"
"border-radius: 10px;\n"
"color: #FCE38A;\n"
"font-size: 14px;\n"
"border: 1px solid white\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #F38181;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #EAFFD0;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/add_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_new_entry.setIcon(icon)
        self.btn_new_entry.setIconSize(QtCore.QSize(24, 24))
        self.btn_new_entry.setObjectName("btn_new_entry")
        self.horizontalLayout.addWidget(self.btn_new_entry)
        self.btn_edit_entry = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_edit_entry.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("arial rounded mt 13")
        font.setBold(True)
        self.btn_edit_entry.setFont(font)
        self.btn_edit_entry.setStyleSheet("QPushButton {\n"
"background-color: #AA96DA;\n"
"border-radius: 10px;\n"
"color: #FCE38A;\n"
"font-size: 14px;\n"
"border: 1px solid white\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #F38181;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #EAFFD0;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/edit_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_edit_entry.setIcon(icon1)
        self.btn_edit_entry.setIconSize(QtCore.QSize(24, 24))
        self.btn_edit_entry.setObjectName("btn_edit_entry")
        self.horizontalLayout.addWidget(self.btn_edit_entry)
        self.btn_del_entry = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_del_entry.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("arial rounded mt 13")
        font.setBold(True)
        self.btn_del_entry.setFont(font)
        self.btn_del_entry.setStyleSheet("QPushButton {\n"
"background-color: #AA96DA;\n"
"border-radius: 10px;\n"
"color: #FCE38A;\n"
"font-size: 14px;\n"
"border: 1px solid white\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #F38181;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #EAFFD0;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/delete_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_del_entry.setIcon(icon2)
        self.btn_del_entry.setIconSize(QtCore.QSize(24, 24))
        self.btn_del_entry.setObjectName("btn_del_entry")
        self.horizontalLayout.addWidget(self.btn_del_entry)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboBox_name_tables = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_name_tables.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_name_tables.setStyleSheet("QComboBox {\n"
"background-color: #AA96DA;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"color: #FCE38A;\n"
"font-size: 14px;\n"
"border: 1px solid white\n"
"}")
        self.comboBox_name_tables.setObjectName("comboBox_name_tables")
        self.verticalLayout.addWidget(self.comboBox_name_tables)
        self.view_records = QtWidgets.QTableView(parent=self.centralwidget)
        self.view_records.setStyleSheet("QTableView {\n"
"background-color: #EAFFD0;\n"
"border-bottom-right-radius: 10px;\n"
"border: 1px solid gray;\n"
"}\n"
"QTableView::section {\n"
"background-color: #AA96DA;\n"
"color: #FCE38A;\n"
"border: none;\n"
"}\n"
"QHeaderView {\n"
"background-color: #EAFFD0;\n"
"}\n"
"QHeaderView::section {\n"
"background-color: #AA96DA;\n"
"color: #FCE38A;\n"
"border: none;\n"
"font-weight: bold;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: black;\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: #FCE38A;\n"
"background-color: #AA96DA;\n"
"}")
        self.view_records.setObjectName("view_records")
        self.verticalLayout.addWidget(self.view_records)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database"))
        self.label_main_name.setText(_translate("MainWindow", "База данных"))
        self.label_user.setText(_translate("MainWindow", "Пользователь:"))
        self.btn_new_entry.setText(_translate("MainWindow", "Добавить запись"))
        self.btn_edit_entry.setText(_translate("MainWindow", "Редактировать запись"))
        self.btn_del_entry.setText(_translate("MainWindow", "Удалить запись"))
