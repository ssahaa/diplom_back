import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog
from WindowsPY.Admin.ArgeementReductTP import Ui_AgreementNewTP
import requests
import os
from pathlib import Path
import Adminestrator.Agreement.AllAgrement as m
from PyQt5.QtGui import QIcon
from User.CreateTp.functions import getGOST
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class AgreementNormal(QMainWindow, Ui_AgreementNewTP):
    def __init__(self, parent=None, UserData = {}, icon = QIcon(''), agreementData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.userD = UserData
        self.icon = icon
        self.AgreementData = agreementData
        self.OLDTP = requests.get(f'http://127.0.0.1:8000/ТП/{self.AgreementData['idTP']}/').json()
        self.pathToPldWersion = self.OLDTP['currentVersionTP']
        data = requests.get(f'http://127.0.0.1:8000/Пользователи/{self.AgreementData['creator']}/')
        self.userData = data.json()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
        self.initUI()

    def initUI(self):
        self.dataTP = requests.get(f'http://127.0.0.1:8000/ТП/{self.AgreementData['idTP']}')
        self.dataTP = self.dataTP.json()
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushButtonCheckOldAgreement_2.clicked.connect(self.BadArgeement)
        self.pushButtonCheckOldAgreement_3.clicked.connect(self.DownloadDock)
        self.pushButtonCheckOldAgreement.clicked.connect(self.AgreementTrue)
        self.labelName.setText(self.dataTP['TpName'])
        if (self.AgreementData['NewName'] is None):
            self.labelNewName.setText('-')
        else:
            self.labelNewName.setText(self.AgreementData['NewName'])
        self.labelUserComment.setText(self.AgreementData['comment'])
        self.labelCreator.setText(self.userData['userSurname'] + ' ' + self.userData['userName'] + ' ' + self.userData['userMiddleName'])


        arrayIdGpstNew = [str(x) for x in self.AgreementData['idTpStringNew'].split() if x != "-"]
        GostTPALL = requests.get(f'http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/').json()
        self.OldDock = []
        for i in range(len(GostTPALL)):
            for j in range(len(arrayIdGpstNew)):
                if int(GostTPALL[i]['idDOCK']) == int(self.AgreementData['idTP']):
                    if int(GostTPALL[i]['idGOST']) == int(arrayIdGpstNew[j]):
                        self.OldDock.append(GostTPALL[i]['idGOST'])

        self.ALLGOST = getGOST()
        strOldGost = ''
        for i in range(len(self.ALLGOST)):
            for j in range(len(arrayIdGpstNew)):
                if int(self.ALLGOST[i]['id']) == int(arrayIdGpstNew[j]):
                    strOldGost += self.ALLGOST[i]['gostName']
                    strOldGost += '; '
        self.labelGOST.setText(strOldGost)
        

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
                except:
                    pass
 
        responceOldDock = requests.get(self.pathToPldWersion)
        self.pathToOldDock = os.path.join(save_path, "Старая верси ТП" + ".docx")
        try:
            with open(self.pathToOldDock, "wb") as file:
                file.write(response.content)
                file.close()
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка Загрузки старой версии ТП")

    def AgreementTrue(self):
        urlTP = f"http://127.0.0.1:8000/ТП/{self.AgreementData['idTP']}/"
        self.GOSTTP = requests.get('http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/').json()
        dataTP = requests.get('http://127.0.0.1:8000/ТП/')
        self.dataTP = dataTP.json()
        with open(self.file_path, 'rb') as file:
            file_data = file.read()
        for i in range(len(self.dataTP)):
            if self.dataTP[i]['id'] == self.AgreementData['idTP']:
                TPName = self.dataTP[i]['TpName']
                self.thisTP = self.dataTP[i]
        files = {
            'currentVersionTP': ('currentVersionTP', file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }
        data = {
            "TpName":TPName if self.AgreementData['NewName'] == '-' else self.AgreementData['NewName'],
            "needForChange": False,
            "idCreator": self.AgreementData['creator'],
            "comment": self.AgreementData['comment'],
        }
        r = requests.patch(urlTP, files=files, data=data)
        try:
            if r.status_code == 200:
                QMessageBox.information(self.centralwidget, "Успешно", "ТП измёнён")
            else:
                QMessageBox.information(self.centralwidget, "Ошибка", r.status_code + r.text)
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка в запросе")

        dataTP = requests.get('http://127.0.0.1:8000/ТП/')
        lens = len(dataTP.json())
        self.dataNewTP = dataTP.json()[lens-1]
        urlSetGosts = "http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/"

        arrayIdGpst = [str(x) for x in self.AgreementData['idTpStringNew'].split() if x != "-"]

        for i in range(len(self.GOSTTP)):
            if self.GOSTTP[i]['idDOCK'] == self.thisTP['id']:
                r = requests.delete(f'http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/{self.GOSTTP[i]['id']}/')


        for i in range(len(self.ALLGOST)):
            for j in range(len(arrayIdGpst)):
                if self.ALLGOST[i]['id'] == int(arrayIdGpst[j]):
                    data = {
                    "idGOST": arrayIdGpst[j],
                    "idDOCK": self.thisTP['id']
                }
                    r = requests.post(urlSetGosts, data=data)

        urlGOODAgreement = f"http://127.0.0.1:8000/Согласование%20ТП/{self.AgreementData['id']}/"
        data = {
            "isActual": False,
        }
        r = requests.patch(urlGOODAgreement, data=data)

        with open(self.pathToOldDock, 'rb') as file:
            file_data = file.read()

        files = {
            'dock': ('currentVersionTP', file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }
        data = {
            "idTP":self.AgreementData['idTP'],
        }
        urlOldTP = 'http://127.0.0.1:8000/Старые%20ТП/'
        r = requests.post(urlOldTP, files=files, data=data)
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

