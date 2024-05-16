import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog
from WindowsPY.CreateTP import Ui_CreateTp
from User.CreateTp.functions import getGOST
import requests
import os
from pathlib import Path

class CreateTP(QMainWindow, Ui_CreateTp):
    def __init__(self, parent=None, UserData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushButtonDownloadTp.clicked.connect(self.downloadShablon)
        self.pushButtonSelectFile.clicked.connect(self.selectFile)
        self.pushButtonAgreement.clicked.connect(self.argeement)
        self.checkboxes = []
        self.GOSTS = getGOST()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        for i in range(len(self.GOSTS)): #Заполнение перечня ГОСТ
            #checkbox = QCheckBox(f"Элемент {i+1}", self.scrollAreaWidgetContents_2)
            checkbox = QCheckBox(self.GOSTS[i]['gostName'], self.scrollAreaWidgetContents_2)
            checkbox.setObjectName(f"checkBox_{i}")
            self.checkboxes.append(checkbox)
            self.verticalLayout.addWidget(checkbox)
        


        

    def downloadShablon(self):
        url = 'http://127.0.0.1:8000/ТП/3/'
        save_path = self.lineEditPathDownload.text()
        if url is None:
            return
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_path, "Шаблон ТП" + ".docx")
            if len(file_path) > 16:
                try:
                    with open(file_path, "wb") as file:
                        file.write(response.content)
                        file.close()
                        QMessageBox.information(self.centralwidget, "Успешно", "Файл успешно загружен")
                        return
                except:
                    pass
        QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка Загрузки!!")

    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.pathToFile = Path(file_path)     
        self.label_3.setText(file_path)



    def argeement(self):
        self.name = self.lineEditName.text()
        self.comment = self.lineEditComment.text()

        url = "http://127.0.0.1:8000/Согласование%20ТП/"
        self.selected_items = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        #self.selected_items
        self.GOSTSID = ''
        for i in range(len(self.selected_items)):
            for j in range(len(self.GOSTS)):
                if self.GOSTS[j]['gostName'] == self.selected_items[i]:
                    self.GOSTSID += str(self.GOSTS[j]['id']) + ' '
        self.GOSTSID += '-'
        url = "http://127.0.0.1:8000/Согласование%20ТП/"

        try:
            with open(self.pathToFile, 'rb') as file:
                file_data = file.read()
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите файл")
            return
        
        if (self.name):
            pass   
        else:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите наименование ТП")
            return

        files = {
            'dock': (self.name, file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }

        data = {
            "comment": self.comment if self.comment else '',
            "creator": self.userD['id'],
            "isActual": True,
            "idTpStringNew": self.GOSTSID,
            "NewName": self.name
        }

        r = requests.post(url, files=files, data=data)
        try:
            if r.status_code == 201:
                QMessageBox.information(self.centralwidget, "Успешно", "Отправлено на согласование")
            else:
                QMessageBox.information(self.centralwidget, "Ошибка", r.status_code + r.text)
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка в запросе")


    def go_back(self):
        self.close()
        self.parent().show()  




    def getPath(self):
        pass