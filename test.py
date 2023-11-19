from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        combobox1 = QComboBox()
        combobox1.addItems(['1', '2', '3', '4'])

        combobox2 = QComboBox()
        combobox2.addItems(['a', 'b', 'c', 'd', 'e'])

        combobox3 = QComboBox()
        combobox3.addItems(['One', 'Two', 'Three', 'Four'])
        combobox3.insertItem(2, 'Hello!')

        combobox4 = QComboBox()
        combobox4.addItems(['One', 'Two', 'Three', 'Four'])
        combobox4.insertItems(2, ['Hello!', 'again'])

        layout = QVBoxLayout()
        layout.addWidget(combobox1)
        layout.addWidget(combobox2)
        layout.addWidget(combobox3)
        layout.addWidget(combobox4)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def current_text_changed(self, s):
        print("Current text: ", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()