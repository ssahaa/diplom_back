import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QCheckBox, QMessageBox,QFileDialog
from WindowsPY.AgreementCardBadAgreeement import Ui_AgreementUserCardBadAgreement
import User.Agreement.ALLAgreementWindow as m
from PyQt5.QtGui import QIcon
import requests
from User.Agreement.CreateAgreement.AllTPAGreementWindow import CreateAgreementALLTP
from User.CreateTp.functions import getGOST
import os
from pathlib import Path
from docx import Document
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window
import re
class BadAgreement(QMainWindow, Ui_AgreementUserCardBadAgreement):
    def __init__(self, parent=None, UserData = {}, icon = QIcon(''), agreementData={}):
        super().__init__(parent)
        self.setupUi(self)
        self.icon = icon
        self.userD = UserData
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
        self.agreementData = agreementData
        self.initUI()
        #self.setWindowIcon(icon) 
    

    def initUI(self):
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushButtonCheckOldAgreement_3.clicked.connect(self.downloadTP)
        self.pushButtonCheckOldAgreement_4.clicked.connect(self.selectFile)
        self.pushButtonToAgreemennt.clicked.connect(self.agreement)
        self.ALLTP = requests.get("http://127.0.0.1:8000/ТП/").json()
        self.dataThisTP = requests.get(f"http://127.0.0.1:8000/ТП/{self.agreementData['idTP']}/").json()
        for i in range(len(self.ALLTP)):
            if self.ALLTP[i]['id'] == self.agreementData['idTP']:
                self.labelName.setText(self.ALLTP[i]['TpName'])
                self.labelNewName.setText('-' if len(self.agreementData['NewName']) < 2 else self.agreementData['NewName'])
                self.labelUserComment.setText(self.agreementData['AdminComment'])

        if (self.agreementData['IsNewTP'] == True):
            self.labelName.setText('-')
            self.labelNewName.setText(self.agreementData['NewName'])
            self.labelUserComment.setText(self.agreementData['AdminComment'])

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
                        self.pathToFile = file_path
                        QMessageBox.information(self.centralwidget, "Успешно", "Файл успешно загружен")
                        return
                except:
                    QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка Загрузки!!")
    

    def selectFile(self):
        if len(self.lineEditPathToDownload.text()) < 2:
            file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
            if file_path:
                self.pathToFile = Path(file_path)     
            self.lineEditPathToDownload_2.setText(file_path)
        else:
            self.lineEditPathToDownload_2.setText(self.pathToFile)

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
                    self.checkboxes[i].setChecked(True)
            
        matches = [match for match in matches if match not in [gost['gostName'] for gost in found_gosts]]
        if len(matches) > 0:
            error_message = "В документе указаны ГОСТ которых нет в системе:\n" + "\n".join(matches) + "\nОбратитесь к администратору для их добавления"
            QMessageBox.information(self.centralwidget, "Ошибка", error_message)



        

    def agreement(self):
        self.ALLAGrementt = requests.get('http://127.0.0.1:8000/Согласование%20ТП/').json()
        url = f"http://127.0.0.1:8000/Согласование%20ТП/{self.agreementData['id']}/"
        self.selected_items = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        #self.selected_items
        self.GOSTSID = ''
        for i in range(len(self.selected_items)):
            for j in range(len(self.GOSTS)):
                if self.GOSTS[j]['gostName'] == self.selected_items[i]:
                    self.GOSTSID += str(self.GOSTS[j]['id']) + ' '
        self.GOSTSID += '-'
        if (len(self.GOSTSID) < 2):
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите ГОСТ")
            return
        try:
            with open(self.pathToFile, 'rb') as file:
                file_data = file.read()
        except:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите файл")
            return

        files = {
            'dock': ('TP', file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }

        data = {
            "idTpStringNew": self.GOSTSID,
            "IsUserAswerCommnet": True
        }

        r = requests.patch(url, files=files, data=data)
        try:
            if r.status_code == 200:
                QMessageBox.information(self.centralwidget, "Успешно", "Отправлено на согласование")
            else:
                QMessageBox.information(self.centralwidget, "Ошибка", r.status_code + r.text)
        except:
            print(r.status_code)
            QMessageBox.information(self.centralwidget, "Ошибка", "Ошибка в запросе")

        files = {
            'dock': ('newDockVersion', file_data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }
        url = f"http://127.0.0.1:8000/ТП/{self.dataThisTP['id']}/"
        r = requests.post(url, files=files)
        self.menu = m.AllAgreementUser(UserData=self.userD, icon=self.icon)
        self.menu.setWindowIcon(self.icon) 
        self.menu.show()
        self.close()


    def go_back(self):
        self.menu = m.AllAgreementUser(UserData=self.userD, icon=self.icon)
        self.menu.setWindowIcon(self.icon) 
        self.menu.show()
        self.close()