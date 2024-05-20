import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog
from WindowsPY.CreateTP import Ui_CreateTp
from User.CreateTp.functions import getGOST
import requests
import os
from pathlib import Path
import Adminestrator.GOSTS.GOSTSWindow as m
from WindowsPY.Admin.CreateGost import Ui_CreateGOST
from PyQt5.QtGui import QIcon


class CreateGOST(QMainWindow, Ui_CreateGOST):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('')):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.icon = icon
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushButtonSelectFile.clicked.connect(self.selectFile)
        self.pushButtonCreate.clicked.connect(self.CreateGost)


    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.pathToFile = Path(file_path)     
        self.label_3.setText(file_path)

    def CreateGost(self):
        self.name = self.lineEdit.text()

        url = "http://127.0.0.1:8000/ГОСТ/"

        try:
            with open(self.pathToFile, 'rb') as file:
                file_data = file.read()
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите файл")
            return
        
        if (self.name):
            pass   
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите наименование ГОСТ")
            return

        files = {
            'file': (self.name, file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }

        data = {
            "gostName": self.name,
            "idCreator": self.userD['id']
        }

        r = requests.post(url, files=files, data=data)
        try:
            if r.status_code == 201:
                QMessageBox.information(self.centralwidget, "Успешно", "ГОСТ создан")
            else:
                QMessageBox.information(self.centralwidget, "Ошибка", r.status_code + r.text)
        except:
            print(r.status_code)
            print(r.text)
            QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка в запросе")


    def go_back(self):
        #self.close()
        #self.parent().show()  
        self.menu = m.ALLGosts(UserData=self.userD, icon=self.icon)
        self.menu.show()
        self.close()
