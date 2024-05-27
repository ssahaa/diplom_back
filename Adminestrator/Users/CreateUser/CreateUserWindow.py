import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog
from WindowsPY.CreateTP import Ui_CreateTp
from WindowsPY.Admin.CreateUser import Ui_CreateUser
import requests
import os
from pathlib import Path
import Adminestrator.Users.AllUsersWindow as m
from PyQt5.QtGui import QIcon
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class CreateUser(QMainWindow, Ui_CreateUser):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('')):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.icon = icon
        grade = requests.get('http://127.0.0.1:8000/Должности/')
        self.grades = grade.json()
        self.initUI()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)

    def initUI(self):
        self.pushButtotBack.clicked.connect(self.go_back)
        self.pushButtonCreate.clicked.connect(self.changeUser)

        self.checkboxes = []
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)

        for i in range(len(self.grades)):
            checkbox = QCheckBox(self.grades[i]['gradeName'] + '  Зарплата:' + str(self.grades[i]['salary']) + ' Уровень доступа:' + str(self.grades[i]['accessLevel']), self.scrollAreaWidgetContents_3)
            checkbox.setObjectName(f"checkBox_{i}")
            self.checkboxes.append(checkbox)
            self.verticalLayout.addWidget(checkbox)

    def changeUser(self):
        url = f"http://127.0.0.1:8000/Пользователи/"

        if len(self.lineEditLogin.text()) > 0:
            pass
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите логин")
            return

        if len(self.lineEditFamil.text()) > 0:
            pass
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите фамилию")
            return

        if len(self.lineEditName.text()) > 0:
            pass
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите имя")
            return

        if len(self.lineEditOtch.text()) > 0:
            pass
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите Отчество")
            return

        if len(self.lineEditPassword.text()) > 0:
            pass
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите пароль")
            return
        
        self.selected_items = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        if (len(self.selected_items) > 1):
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите только одну должность")
            return
        
        if (len(self.selected_items) == 0):
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите должность")
            return
        temp = self.selected_items[0].index(' ')
        self.selecterGradeName = self.selected_items[0][:temp]

        idWorkgrade = 0
        for i in range(len(self.grades)):
            if(self.selecterGradeName == self.grades[i]['gradeName']):
                idWorkgrade = i
        data = {
            "userName": self.lineEditName.text(),
            "userSurname": self.lineEditFamil.text(),
            "userMiddleName": self.lineEditOtch.text(),
            "WorkerGrade": self.grades[idWorkgrade]['id'],
            "password": self.lineEditPassword.text(),
            "login": self.lineEditLogin.text()
        }

        r = requests.post(url, data=data)
        if r.status_code == 201:
            QMessageBox.information(self.centralwidget, "Успешно", "Пользователь создан")
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", str(r.status_code) + r.text)


    def go_back(self):
        self.allgostss = m.AllUsers(UserData=self.userD, icon=self.icon)
        self.allgostss.setWindowIcon(self.icon) 
        self.allgostss.show()
        self.close()