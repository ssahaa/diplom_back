import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WindowsPY.createTPW import Ui_CreateTP

class CreateTP(QMainWindow, Ui_CreateTP):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.close()
        self.parent().show()  