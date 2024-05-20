import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog, QTableWidgetItem
from WindowsPY.AgreementAllTP import Ui_AgreementAllTP
import requests
import os
from pathlib import Path
import User.Agreement.ALLAgreementWindow as m
from WindowsPY.Admin.CreateGost import Ui_CreateGOST
from PyQt5.QtGui import QIcon
from User.CreateTp.functions import getGOST
from User.AllTp.functions import getTp
from User.Agreement.CreateAgreement.CreateAgreementWindow import CreateAgreement
class CreateAgreementALLTP(QMainWindow, Ui_AgreementAllTP):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('')):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.icon = icon
        self.pushButtonBack.clicked.connect(self.go_back)
        self.tableWidgetALLTP.cellClicked.connect(self.clickTP)
        self.initUI()

    def initUI(self):
        self.dataTP = getTp()
        for i in range(len(self.dataTP)):
            actualRow = self.tableWidgetALLTP.rowCount()
            self.tableWidgetALLTP.insertRow(actualRow)
            self.tableWidgetALLTP.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[i]['TpName']))

    def clickTP(self, row, column):
        dataThisTP = self.dataTP[row]
        self.createGOSTS = CreateAgreement(UserData=self.userD, icon=self.icon, dataThisTP = dataThisTP)
        self.createGOSTS.setWindowIcon(self.icon) 
        self.createGOSTS.show()
        self.close()


    def go_back(self):
        self.menu = m.AllAgreementUser(UserData=self.userD, icon=self.icon)
        self.menu.setWindowIcon(self.icon) 
        self.menu.show()
        self.close()

