from PyQt6 import QtCore, QtGui, QtWidgets
import design.resources


class Ui_Dialog_Auth(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 310)
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
        self.comboBox_type_connect = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox_type_connect.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_type_connect.setStyleSheet("QComboBox {\n"
"background-color: #AA96DA;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"color: #FCE38A;\n"
"font-size: 14px;\n"
"border: 1px solid white\n"
"}")
        self.comboBox_type_connect.setObjectName("comboBox_type_connect")
        self.comboBox_type_connect.addItems(["SQL Server Authentication", "Windows Authentication"])
        self.verticalLayout.addWidget(self.comboBox_type_connect)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(100, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setStyleSheet("background-color: #A8D8EA;\n"
"border: 1px solid gray;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setStyleSheet("border: 1px solid state black;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMinimumSize(QtCore.QSize(100, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("background-color: #A8D8EA;\n"
"border: 1px solid gray;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("border: 1px solid state black;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(100, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("background-color: #A8D8EA;\n"
"border: 1px solid gray;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("border: 1px solid state black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_auth = QtWidgets.QPushButton(parent=self.frame)
        self.btn_auth.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("arial rounded mt 13")
        font.setBold(True)
        self.btn_auth.setFont(font)
        self.btn_auth.setStyleSheet("QPushButton {\n"
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
        self.btn_auth.setIcon(icon)
        self.btn_auth.setIconSize(QtCore.QSize(24, 24))
        self.btn_auth.setObjectName("btn_auth")
        self.verticalLayout.addWidget(self.btn_auth)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Authorization"))
        self.label_main_name.setText(_translate("Dialog", "Авторизация"))
        self.label_3.setText(_translate("Dialog", "Сервер:"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Введите ip-адрес"))
        self.label.setText(_translate("Dialog", "Логин:"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Введите логин"))
        self.label_2.setText(_translate("Dialog", "Пароль:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Введите пароль"))
        self.btn_auth.setText(_translate("Dialog", "Авторизоваться"))
