import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog, QTableWidgetItem
from WindowsPY.Admin.AllUsers import Ui_AllUsers
import requests
import os
from pathlib import Path
import Adminestrator.Admin as m
from PyQt5.QtGui import QIcon
import requests
from Adminestrator.Users.UsersCard.UserCard import UserCard
from Adminestrator.Users.CreateUser.CreateUserWindow import CreateUser
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class AllUsers(QMainWindow, Ui_AllUsers):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('')):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.icon = icon
        self.initUI()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
    def initUI(self):
        self.pushButtotBack.clicked.connect(self.go_back)
        self.tableWidgetAcrualTP.cellClicked.connect(self.clickUser)
        self.pushButton.clicked.connect(self.createUser)
        t = requests.get('http://127.0.0.1:8000/Пользователи/')
        self.users = t.json()
        for i in range(len(self.users)):
            actualRow = self.tableWidgetAcrualTP.rowCount()
            self.tableWidgetAcrualTP.insertRow(actualRow)
            self.tableWidgetAcrualTP.setItem(actualRow, 0, QTableWidgetItem(self.users[i]['userSurname']))
            self.tableWidgetAcrualTP.setItem(actualRow, 1, QTableWidgetItem(self.users[i]['userName']))
            self.tableWidgetAcrualTP.setItem(actualRow, 2, QTableWidgetItem(self.users[i]['userMiddleName']))

        
    def go_back(self):
        self.AdminW = m.AdminWindow(UserData=self.userD)
        self.AdminW.setWindowIcon(self.icon)
        self.AdminW.show()
        self.close()

    def createUser(self):
        self.CreateUser = CreateUser(UserData=self.userD, icon=self.icon)
        self.CreateUser.setWindowIcon(self.icon)
        self.CreateUser.show()
        self.close()

    def clickUser(self,row, column):
        self.UserW = UserCard(UserData=self.userD, icon=self.icon, thisUser=self.users[row])
        self.UserW.setWindowIcon(self.icon)
        self.UserW.show()
        self.close()