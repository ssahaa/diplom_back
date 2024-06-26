import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog, QTableWidgetItem
from WindowsPY.NeedChange import Ui_NeedChange
from User.NeedChange.functions import getTP
import requests
import os
import User.MainWinodw as m
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window
class NeedChange(QMainWindow, Ui_NeedChange):
    def __init__(self, parent=None, UserData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButtonBack.clicked.connect(self.go_back)
        self.initUI()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
        self.userD = UserData
    def initUI(self):
        self.dataTP = getTP()
        for i in range(len(self.dataTP)):
            actualRow = self.tableWidgetNeedChange.rowCount()
            self.tableWidgetNeedChange.insertRow(actualRow)
            self.tableWidgetNeedChange.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[i]['TpName']))
            if self.dataTP[i]['needForChange'] == True:
                self.tableWidgetNeedChange.setItem(actualRow, 1,QTableWidgetItem( "Требуется изменение"))
            else:
                self.tableWidgetNeedChange.setItem(actualRow, 1, QTableWidgetItem("Изменение не требуется"))



    def go_back(self):
        self.menu = m.UserWindow(UserData=self.userD)
        self.menu.show()
        self.close()
