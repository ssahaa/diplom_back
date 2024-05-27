import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from WindowsPY.Admin.TpCard import Ui_MainWindow
from User.AllTp.TpCard.TpCardFunctions import getUserDataID
import requests
import os
import Adminestrator.AllTp.AllTpWindow as m
from PyQt5.QtGui import QIcon
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class TpCard(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None,data={}, UserD = {}, dataTP = {}, icon = QIcon('')):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)

        self.dataUser = UserD
        self.dataTP = dataTP
        self.icon = icon
        #self.setWindowIcon(icon) 
        self.initUI()

    def initUI(self):
        self.dataUserTP = getUserDataID(self.dataTP['idCreator'])
        self.labelCreator.setText(self.dataUserTP.json()['userSurname'] + ' ' + self.dataUserTP.json()['userName'] + ' ' + self.dataUserTP.json()['userMiddleName'])
        self.labelName_2.setText(self.dataTP['TpName'])
        self.labelCreationDate.setText(self.dataTP['creationDate'])
        self.labelLastModified.setText(self.dataTP['lastModified'])
        self.LabelNeedForChange.setText('Изменения не требуются' if self.dataTP['needForChange']!= True else 'Изменения требуются')
        self.LavelOldWersion.setText('Несогласованная верси есть' if self.dataTP['newDockVersion'] else 'Несогласованной версии нет')

        self.pushButton.clicked.connect(self.go_back)
        self.pushButtonDownloadNew.clicked.connect(self.downloadNewTp)
        self.pushButtonDownloadOld.clicked.connect(self.downloadNewNewTp)
        self.pushButton_2.clicked.connect(self.deleteTP)


    def downloadNewTp(self):
        url = self.dataTP['currentVersionTP']
        save_path = self.lineEditPathNewTP.text()
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_path, "ТП" + " " + self.dataTP['TpName'] + ".docx")
            if len(save_path) < 2:
                QMessageBox.information(self.centralwidget, "Ошибка", "Указан неверый путь")
                return
            try:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    file.close()
                    QMessageBox.information(self.centralwidget, "Успех", "Файл успешно загружен")
            except:
                QMessageBox.information(self.centralwidget, "Ошибка", "Указан неверый путь")
                pass


    def downloadNewNewTp(self):
        url = self.dataTP['newDockVersion']
        save_path = self.lineEditPathOldTP.text()
        if url is None:
            QMessageBox.information(self.centralwidget, "Ошибка", "Нет новой версии ТП")
            return
        response = requests.get(url)
        if response.status_code == 200:
            #print('Мы в условии')
            file_path = os.path.join(save_path, "Не согласованый ТП" + " " + self.dataTP['TpName'] + ".docx")
            try:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    file.close()
                    QMessageBox.information(self.centralwidget, "Успех", "Файл успешно загружен")
            except:
                QMessageBox.information(self.centralwidget, "Ошибка", "Укажите верный путь")
                pass

    def deleteTP(self):
        r = requests.delete(f'http://127.0.0.1:8000/ТП/{self.dataTP['id']}') 
        QMessageBox.information(self.centralwidget, "Успешно", "ТП удалён")



    def go_back(self):
        self.AllTPW = m.AllTP(UserData = self.dataUser, icon=self.icon)
        self.AllTPW.setWindowIcon(self.icon)
        self.AllTPW.show()
        self.close()
        
