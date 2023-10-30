import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QMessageBox, QWidget
from PyQt6.QtGui import QAction, QIcon, QKeySequence
import pyqtgraph as pg
from random import randint


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Awesome App")
        self.centralWidget = QPushButton("Employee")
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        self.setCentralWidget(self.centralWidget)

        '''l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(lambda checked: self.toggle_window(self.window1))
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(lambda checked: self.toggle_window(self.window2))
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)'''
    
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
    
    def onEmployeeBtnClicked(self):
        dlg = EmployeeDlg(self)
        dlg.exec()

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class EmployeeDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #loadUi("dialog.ui", self)
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()