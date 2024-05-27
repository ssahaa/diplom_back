import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog
from WindowsPY.Admin.ArgeementCreateTP import Ui_AgreementNewTP
import requests
import os
from pathlib import Path
import Adminestrator.Agreement.AllAgrement as m
from PyQt5.QtGui import QIcon
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class CreateTPAgreement(QMainWindow, Ui_AgreementNewTP):
    def __init__(self, parent=None, UserData = {}, icon = QIcon(''), agreementData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.icon = icon
        self.AgreementData = agreementData
        data = requests.get(f'http://127.0.0.1:8000/Пользователи/{self.AgreementData['creator']}/')
        self.userData = data.json()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)

        self.initUI()

    def initUI(self):
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushButtonCheckOldAgreement_2.clicked.connect(self.BadArgeement)
        self.pushButtonCheckOldAgreement_3.clicked.connect(self.DownloadDock)
        self.pushButtonCheckOldAgreement.clicked.connect(self.AgreementTrue)
        self.labelName.setText(self.AgreementData['NewName'])
        self.labelUserComment.setText(self.AgreementData['comment'])
        self.labelCreator.setText(self.userData['userSurname'] + ' ' + self.userData['userName'] + ' ' + self.userData['userMiddleName'])


    def DownloadDock(self):
        url = self.AgreementData['dock']
        save_path = self.lineEditPathToDownload.text()
        if url is None:
            return
        
        if (len(save_path)<2):
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите путь!!")
            return
        
        response = requests.get(url)
        if response.status_code == 200:
            self.file_path = os.path.join(save_path, "Документ для рассмотрения" + ".docx")
            if len(self.file_path) > 32:
                try:
                    with open(self.file_path, "wb") as file:
                        file.write(response.content)
                        file.close()
                        QMessageBox.information(self.centralwidget, "Успешно", "Файл успешно загружен")
                        return
                except:
                    pass
        QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка Загрузки!!")

    def AgreementTrue(self):
        urlTP = "http://127.0.0.1:8000/ТП/"

        dataTP = requests.get('http://127.0.0.1:8000/ТП/')
        self.dataTP = dataTP.json()
        for i in range(len(self.dataTP)):
            if(self.dataTP[i]['TpName'] == self.AgreementData['NewName']):
                QMessageBox.information(self.centralwidget, "Ошибка", "Данный ТП уже существует Заявка отклонена")
                urlBadAgreement = f"http://127.0.0.1:8000/Согласование%20ТП/{self.AgreementData['id']}/"
                data = {
                    "isActual": False,
                }
                r = requests.patch(urlBadAgreement, data=data)
                self.allgostss = m.AllAgreement(UserData=self.userD, icon=self.icon)
                self.allgostss.setWindowIcon(self.icon) 
                self.allgostss.show()
                self.close()
                return

        try:
            with open(self.file_path, 'rb') as file:
                file_data = file.read()
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Загрузите и проверьте документ")
            return
        
        files = {
            'currentVersionTP': (self.AgreementData['NewName'], file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }

        data = {
            "TpName": self.AgreementData['NewName'],
            "needForChange": False,
            "idCreator": self.AgreementData['creator'],
            "comment": "Создание нового ТП",
        }
        r = requests.post(urlTP, files=files, data=data)
        try:
            if r.status_code == 201:
                QMessageBox.information(self.centralwidget, "Успешно", "ТП создан")
            else:
                QMessageBox.information(self.centralwidget, "Ошибка", r.status_code + r.text)
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка в запросе")

        dataTP = requests.get('http://127.0.0.1:8000/ТП/')
        lens = len(dataTP.json())
        self.dataNewTP = dataTP.json()[lens-1]
        urlSetGosts = "http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/"

        arrayIdGpst = [str(x) for x in self.AgreementData['idTpStringNew'].split() if x != "-"]
        for i in range(len(arrayIdGpst)):
            data = {
                "idGOST": arrayIdGpst[i],
                "idDOCK": self.dataNewTP["id"]
            }
            r = requests.post(urlSetGosts, data=data)
        urlBadAgreement = f"http://127.0.0.1:8000/Согласование%20ТП/{self.AgreementData['id']}/"
        data = {
            "isActual": False,
        }
        r = requests.patch(urlBadAgreement, data=data)
        self.allgostss = m.AllAgreement(UserData=self.userD, icon=self.icon)
        self.allgostss.setWindowIcon(self.icon) 
        self.allgostss.show()
        self.close()



    def BadArgeement(self):
        url = f"http://127.0.0.1:8000/Согласование%20ТП/{self.AgreementData['id']}/"
        adminComment = self.lineEditAdminCommnet.text()
        if (len(adminComment) < 3):
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите причину отказа")
            return
        data = {
            "AdminComment": adminComment,
            "IsUserAswerCommnet": False,
        }
        r = requests.patch(url, data=data)
        QMessageBox.information(self.centralwidget, "Успешно", "Замечаня высланы пользователю")

    def go_back(self):
        #self.close()
        #self.parent().show()  
        self.allgostss = m.AllAgreement(UserData=self.userD, icon=self.icon)
        self.allgostss.setWindowIcon(self.icon) 
        self.allgostss.show()
        self.close()
