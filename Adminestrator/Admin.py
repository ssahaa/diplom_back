import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WindowsPY.userW import Ui_MainWindow
class AdminWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
