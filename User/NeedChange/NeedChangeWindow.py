import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog, QTableWidgetItem
from WindowsPY.NeedChange import Ui_NeedChange
from User.NeedChange.functions import getTP
import requests
import os
import User.MainWinodw as m

class NeedChange(QMainWindow, Ui_NeedChange):
    def __init__(self, parent=None, UserData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButtonBack.clicked.connect(self.go_back)
        self.initUI()
        self.userD = UserData
    def initUI(self):
        self.dataTP = getTP()
        for i in range(len(self.dataTP)):
            actualRow = self.tableWidgetNeedChange.rowCount()
            self.tableWidgetNeedChange.insertRow(actualRow)
            self.tableWidgetNeedChange.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[i]['TpName']))
            self.tableWidgetNeedChange.setItem(actualRow, 1, QTableWidgetItem("Изменение не требуется") if QTableWidgetItem(self.dataTP[i]['needForChange']) else QTableWidgetItem( "Требуется изменение"))



    def go_back(self):
        self.menu = m.UserWindow(UserData=self.userD)
        self.menu.show()
        self.close()
