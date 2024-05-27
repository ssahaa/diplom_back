import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog
from WindowsPY.CreateTP import Ui_CreateTp
from User.CreateTp.functions import getGOST
import requests
import os
from pathlib import Path
import User.MainWinodw as m
from docx import Document
import re
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window
import pdf2docx 
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
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
        self.GOSTS = getGOST()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.userD = UserData
        for i in range(len(self.GOSTS)):
            #checkbox = QCheckBox(f"Элемент {i+1}", self.scrollAreaWidgetContents_2)
            checkbox = QCheckBox(self.GOSTS[i]['gostName'], self.scrollAreaWidgetContents_2)
            checkbox.setObjectName(self.GOSTS[i]['gostName'])
            self.checkboxes.append(checkbox)
            self.verticalLayout.addWidget(checkbox)




        

    def downloadShablon(self):

        allTP = requests.get("http://127.0.0.1:8000/ТП/").json()

        for i in range(len(allTP)):
            if allTP[i]['TpName'] == "Шаблон":
                id = allTP[i]['id']
                break
        dataShablon = requests.get(f"http://127.0.0.1:8000/ТП/{id}/").json()

        url = dataShablon['currentVersionTP']
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
        else:
            return
        
        doc = Document(self.pathToFile)
        found_gosts = []
        pattern = r'ГОСТ [\w-]+'
        matches = []

        for paragraph in doc.paragraphs:
            if re.search(pattern, paragraph.text):
                matches.extend(re.findall(pattern, paragraph.text))
            for run in paragraph.runs:
                for gost in self.GOSTS:
                    if gost['gostName'] in run.text:
                        found_gosts.append(gost)
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)
        if len(found_gosts) == 0:
            QMessageBox.information(self.centralwidget, "Ошибка", "В документе не указаны ГОСТ")
            return

        for i in range (len(found_gosts)):
            for checkbox in range(len(self.checkboxes)):
                if self.checkboxes[checkbox].text()== found_gosts[i]['gostName']:
                    self.checkboxes[checkbox].setChecked(True)
            
        matches = [match for match in matches if match not in [gost['gostName'] for gost in found_gosts]]
        if len(matches) > 0:
            error_message = "В документе указаны ГОСТ которых нет в системе:\n" + "\n".join(matches) + "\nОбратитесь к администратору для их добавления"
            QMessageBox.information(self.centralwidget, "Ошибка", error_message)



        
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
            "NewName": self.name,
            "IsNewTP": True
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
        #self.close()
        #self.parent().show()  
        self.menu = m.UserWindow(UserData=self.userD)
        self.menu.show()
        self.close()
