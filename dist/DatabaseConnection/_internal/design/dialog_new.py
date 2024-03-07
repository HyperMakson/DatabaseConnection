from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
import design.resources
from connection import Data


class Ui_Dialog_New(object):
    def setupUi(self, Dialog, table):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 487)
        Dialog.setStyleSheet("background-color: #A8D8EA;\n"
"font-family: arial rounded mt bold;")
        Dialog.setWindowIcon(QtGui.QIcon(":/icon/icons/database_FILL0_wght400_GRAD0_opsz24.svg"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setStyleSheet("background-color: #EAFFD0;\n"
"border-radius: 10px;\n"
"border: 1px solid #AA96DA;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_main_name = QtWidgets.QLabel(parent=self.frame)
        self.label_main_name.setMinimumSize(QtCore.QSize(300, 100))
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
        self.verticalLayout.addWidget(self.label_main_name)

        self.edit_ui = Data()
        self.data_type = self.edit_ui.select_data_type(table)
        self.column = self.edit_ui.select_column_name(table)
        self.constraint_keys = self.edit_ui.select_relation(table)
        self.arr_identity = self.edit_ui.check_identity(table, self.column[0])
        j = 0
        self.dict_obj_name = {}
        
        if self.arr_identity[0] == 0:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout_0")
            self.label = QtWidgets.QLabel(parent=self.frame)
            self.label.setMinimumSize(QtCore.QSize(150, 0))
            self.label.setMaximumSize(QtCore.QSize(150, 300))
            self.label.setWordWrap(True)
            self.label.setStyleSheet("background-color: #A8D8EA;\n"
                                        "border: 1px solid gray;")
            self.label.setObjectName("label_0")
            self.horizontalLayout.addWidget(self.label)
            self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
            self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
            self.lineEdit.setObjectName("lineEdit_0")
            self.dict_obj_name["lineEdit_0"] = self.data_type[0]
            setattr(self, "lineEdit_0", self.lineEdit)
            self.horizontalLayout.addWidget(self.lineEdit)
            _translate = QtCore.QCoreApplication.translate
            self.verticalLayout.addLayout(self.horizontalLayout)
            self.label.setText(_translate("Dialog", self.column[0]))
            self.lineEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[0]}"))
        else:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout_0")
            self.label = QtWidgets.QLabel(parent=self.frame)
            self.label.setMinimumSize(QtCore.QSize(150, 0))
            self.label.setMaximumSize(QtCore.QSize(150, 300))
            self.label.setWordWrap(True)
            self.label.setStyleSheet("background-color: rgba(168, 216, 234, 50%);\n"
                                     "border: 1px solid gray;")
            self.label.setObjectName("label_0")
            self.horizontalLayout.addWidget(self.label)
            self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
            self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
            self.lineEdit.setStyleSheet("background-color: rgba(168, 216, 234, 50%);\n"
                                     "border: 1px solid gray;")
            self.lineEdit.setDisabled(True)
            self.lineEdit.setObjectName("lineEdit_0")
            self.dict_obj_name["lineEdit_0"] = self.data_type[0]
            setattr(self, "lineEdit_0", self.lineEdit)
            self.horizontalLayout.addWidget(self.lineEdit)
            _translate = QtCore.QCoreApplication.translate
            self.verticalLayout.addLayout(self.horizontalLayout)
            self.label.setText(_translate("Dialog", self.column[0]))
            self.lineEdit.setPlaceholderText(_translate("Dialog", "Автоинкремент"))

        for i in range(1, len(self.data_type)):
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName(f"horizontalLayout_{i}")
            self.label = QtWidgets.QLabel(parent=self.frame)
            self.label.setMinimumSize(QtCore.QSize(150, 0))
            self.label.setMaximumSize(QtCore.QSize(150, 300))
            self.label.setWordWrap(True)
            self.label.setStyleSheet("background-color: #A8D8EA;\n"
                                        "border: 1px solid gray;")
            self.label.setObjectName(f"label_{i}")
            self.horizontalLayout.addWidget(self.label)
            _translate = QtCore.QCoreApplication.translate
            if self.data_type[i] == 'int' or self.data_type[i] == 'money' or self.data_type[i] == 'bigint' or self.data_type[i] == 'smallint' or self.data_type[i] == 'real' or self.data_type[i] == 'float' or self.data_type[i] == 'tinyint' or self.data_type[i] == 'decimal' or self.data_type[i] == 'smallmoney' or self.data_type[i] == 'float' or self.data_type[i] == 'numeric':
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
                        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
                        self.lineEdit.setObjectName(f"lineEdit_{i}")
                        self.dict_obj_name[f"lineEdit_{i}"] = self.data_type[i]
                        setattr(self, f"lineEdit_{i}", self.lineEdit)
                        self.horizontalLayout.addWidget(self.lineEdit)
                        self.lineEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[i]}"))
                else:
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
                    self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
                    self.lineEdit.setObjectName(f"lineEdit_{i}")
                    self.dict_obj_name[f"lineEdit_{i}"] = self.data_type[i]
                    setattr(self, f"lineEdit_{i}", self.lineEdit)
                    self.horizontalLayout.addWidget(self.lineEdit)
                    self.lineEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[i]}"))
            elif self.data_type[i] == 'bit':
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(["True", "False"])
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                else:
                    self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                    self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                    self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                    self.comboBox_keys.addItems(["True", "False"])
                    self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                    setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                    self.horizontalLayout.addWidget(self.comboBox_keys)
            elif self.data_type[i] == 'datetime' or self.data_type[i] == 'datetime2' or self.data_type[i] == 'datetimeoffset' or self.data_type[i] == 'smalldatetime':
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=self.frame)
                        self.dateTimeEdit.setMinimumSize(QtCore.QSize(0, 30))
                        #self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy")
                        self.dateTimeEdit.setObjectName(f"dateTimeEdit_{i}")
                        self.dict_obj_name[f"dateTimeEdit_{i}"] = self.data_type[i]
                        setattr(self, f"dateTimeEdit_{i}", self.dateTimeEdit)
                        self.horizontalLayout.addWidget(self.dateTimeEdit)
                else:
                    self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=self.frame)
                    self.dateTimeEdit.setMinimumSize(QtCore.QSize(0, 30))
                    #self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy")
                    self.dateTimeEdit.setObjectName(f"dateTimeEdit_{i}")
                    self.dict_obj_name[f"dateTimeEdit_{i}"] = self.data_type[i]
                    setattr(self, f"dateTimeEdit_{i}", self.dateTimeEdit)
                    self.horizontalLayout.addWidget(self.dateTimeEdit)
            elif self.data_type[i] == 'date':
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame)
                        self.dateEdit.setMinimumSize(QtCore.QSize(0, 30))
                        self.dateEdit.setObjectName(f"dateEdit_{i}")
                        self.dict_obj_name[f"dateEdit_{i}"] = self.data_type[i]
                        setattr(self, f"dateEdit_{i}", self.dateEdit)
                        self.horizontalLayout.addWidget(self.dateEdit)
                else:
                    self.dateEdit = QtWidgets.QDateEdit(parent=self.frame)
                    self.dateEdit.setMinimumSize(QtCore.QSize(0, 30))
                    self.dateEdit.setObjectName(f"dateEdit_{i}")
                    self.dict_obj_name[f"dateEdit_{i}"] = self.data_type[i]
                    setattr(self, f"dateEdit_{i}", self.dateEdit)
                    self.horizontalLayout.addWidget(self.dateEdit)
            elif self.data_type[i] == 'time':
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.timeEdit = QtWidgets.QTimeEdit(parent=self.frame)
                        self.timeEdit.setMinimumSize(QtCore.QSize(0, 30))
                        self.timeEdit.setObjectName(f"timeEdit_{i}")
                        self.dict_obj_name[f"timeEdit_{i}"] = self.data_type[i]
                        setattr(self, f"timeEdit_{i}", self.timeEdit)
                        self.horizontalLayout.addWidget(self.timeEdit)
                else:
                    self.timeEdit = QtWidgets.QTimeEdit(parent=self.frame)
                    self.timeEdit.setMinimumSize(QtCore.QSize(0, 30))
                    self.timeEdit.setObjectName(f"timeEdit_{i}")
                    self.dict_obj_name[f"timeEdit_{i}"] = self.data_type[i]
                    setattr(self, f"timeEdit_{i}", self.timeEdit)
                    self.horizontalLayout.addWidget(self.timeEdit)
            elif self.data_type[i] == 'text' or self.data_type[i] == 'ntext':
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.textEdit = QtWidgets.QTextEdit(parent=self.frame)
                        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
                        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
                        self.textEdit.setObjectName(f"textEdit_{i}")
                        self.dict_obj_name[f"textEdit_{i}"] = self.data_type[i]
                        setattr(self, f"textEdit_{i}", self.textEdit)
                        self.horizontalLayout.addWidget(self.textEdit)
                        self.textEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[i]}"))
                else:
                    self.textEdit = QtWidgets.QTextEdit(parent=self.frame)
                    self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
                    self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
                    self.textEdit.setObjectName(f"textEdit_{i}")
                    self.dict_obj_name[f"textEdit_{i}"] = self.data_type[i]
                    setattr(self, f"textEdit_{i}", self.textEdit)
                    self.horizontalLayout.addWidget(self.textEdit)
                    self.textEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[i]}"))
            else:
                if len(self.constraint_keys) != 0:
                    if self.column[i] == self.constraint_keys[j][1]:
                        self.comboBox_keys = QtWidgets.QComboBox(parent=self.frame)
                        self.comboBox_keys.setMinimumSize(QtCore.QSize(0, 30))
                        self.comboBox_keys.setObjectName(f"comboBox_keys_{i}")
                        self.comboBox_keys.addItems(self.edit_ui.select_foreign_values(self.constraint_keys[j][3], self.constraint_keys[j][2]))
                        self.dict_obj_name[f"comboBox_keys_{i}"] = self.data_type[i]
                        setattr(self, f"comboBox_keys_{i}", self.comboBox_keys)
                        self.horizontalLayout.addWidget(self.comboBox_keys)
                        if j < len(self.constraint_keys) - 1:
                            j += 1
                    else:
                        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
                        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
                        self.lineEdit.setObjectName(f"lineEdit_{i}")
                        self.dict_obj_name[f"lineEdit_{i}"] = self.data_type[i]
                        setattr(self, f"lineEdit_{i}", self.lineEdit)
                        self.horizontalLayout.addWidget(self.lineEdit)
                        self.lineEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[i]}"))
                else:
                    self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
                    self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
                    self.lineEdit.setObjectName(f"lineEdit_{i}")
                    self.dict_obj_name[f"lineEdit_{i}"] = self.data_type[i]
                    setattr(self, f"lineEdit_{i}", self.lineEdit)
                    self.horizontalLayout.addWidget(self.lineEdit)
                    self.lineEdit.setPlaceholderText(_translate("Dialog", f"Введите {self.column[i]}"))
            self.verticalLayout.addLayout(self.horizontalLayout)
            self.label.setText(_translate("Dialog", self.column[i]))

        self.btn_new_entry = QtWidgets.QPushButton(parent=self.frame)
        self.btn_new_entry.setMinimumSize(QtCore.QSize(0, 50))
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
        self.verticalLayout.addWidget(self.btn_new_entry)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add entry"))
        self.label_main_name.setText(_translate("Dialog", "Добавление записи"))
        self.btn_new_entry.setText(_translate("Dialog", "Добавить"))
