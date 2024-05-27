import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QVBoxLayout, QCheckBox, QMessageBox
from WindowsPY.AgreementCardNewAgreement import Ui_AgreementUserCard
import User.Agreement.ALLAgreementWindow as m
from PyQt5.QtGui import QIcon
import requests
from User.Agreement.CreateAgreement.AllTPAGreementWindow import CreateAgreementALLTP
from pathlib import Path
from User.CreateTp.functions import getGOST
import os
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window
class NewAgreement(QMainWindow, Ui_AgreementUserCard):
    def __init__(self, parent=None, UserData = {}, icon = QIcon(''), agreementData={} ):
        super().__init__(parent)
        self.setupUi(self)
        self.icon = icon
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
        self.userD = UserData
        self.agreementData = agreementData
        self.initUI()
        #self.setWindowIcon(icon) 
    

    def initUI(self):
        self.ALLTP = requests.get("http://127.0.0.1:8000/ТП/").json()
        self.dataThisTP = requests.get(f"http://127.0.0.1:8000/ТП/{self.agreementData['idTP']}/").json()
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushButtonCheckOldAgreement_3.clicked.connect(self.downloadTP)
        for i in range(len(self.ALLTP)):
            if self.ALLTP[i]['id'] == self.agreementData['idTP']:
                self.labelName.setText(self.ALLTP[i]['TpName'])
                self.labelNewName.setText('-' if len(self.agreementData['NewName']) < 2 else self.agreementData['NewName'])
                self.labelUserComment.setText('-' if len(self.agreementData['comment']) < 2 else self.agreementData['comment'])

        if (self.agreementData['IsNewTP'] == True):
            self.labelName.setText('-')
            self.labelNewName.setText(self.agreementData['NewName'])
            self.labelUserComment.setText('-' if len(self.agreementData['comment']) < 2 else self.agreementData['comment'])

        if self.agreementData['IsNewTP'] == False or self.agreementData['IsNewTP'] == True:
            self.checkboxes = []
            self.GOSTS = getGOST()
            self.GOSTTP = requests.get('http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/').json()
            self.verticalLayout = QVBoxLayout(self.scrollAreaGosts)
            self.arrayIdGostNew = [str(x) for x in self.agreementData['idTpStringNew'].split() if x != "-"]
            for i in range(len(self.GOSTS)):
                isTRUE = 0
                checkbox = QCheckBox(self.GOSTS[i]['gostName'], self.scrollAreaGosts)
                checkbox.setObjectName(f"checkBox_{i}")

                #for j in range(len(self.arrayIdGostNew)):
                #    if self.GOSTTP[i]['idDOCK'] == self.dataThisTP['id']:
                #        if int(self.GOSTTP[i]['idGOST']) == int(self.arrayIdGostNew[j]):
               #             print("вошли в 3")
                #            isTRUE = 1
                #            break
                for j in range(len(self.arrayIdGostNew)):
                    if int(self.GOSTS[i]['id']) == int(self.arrayIdGostNew[j]):
                        isTRUE = 1
                if (isTRUE == 1):
                    checkbox.setChecked(True)
                else:
                    checkbox.setChecked(False)
                isTRUE = 0
                self.checkboxes.append(checkbox)
                self.verticalLayout.addWidget(checkbox)

    def downloadTP(self):
        url = self.agreementData['dock']
        save_path = self.lineEditPathToDownload.text()
        if url is None:
            return
        if len(save_path) < 2:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите верный путь!")
            return
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_path, "ТП из заявки на рассмотрение" + ".docx")
            if len(file_path) > 3:
                try:
                    with open(file_path, "wb") as file:
                        file.write(response.content)
                        file.close()
                        QMessageBox.information(self.centralwidget, "Успешно", "Файл успешно загружен")
                        return
                except:
                    QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка Загрузки!!")
        

    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.pathToFile = Path(file_path)     
        self.lineEditPathToDownload.setText(file_path)

    def go_back(self):
        self.menu = m.AllAgreementUser(UserData=self.userD, icon=self.icon)
        self.menu.setWindowIcon(self.icon) 
        self.menu.show()
        self.close()