import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.TpCard import Ui_MainWindow
from User.AllTp.TpCard.TpCardFunctions import getUserDataID
import requests
import os


class TpCard(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None,data={} ):
        super().__init__(parent)
        self.setupUi(self)
        self.data = data
        self.dataUser = getUserDataID(self.data['idCreator'])
        self.initUI()

        
    
    def initUI(self):
        self.pushButton.clicked.connect(self.go_back)
        self.labelCreator.setText(self.dataUser.json()['userSurname'] + ' ' + self.dataUser.json()['userName'] + ' ' + self.dataUser.json()['userMiddleName'])
        self.labelName_2.setText(self.data['TpName'])
        self.labelCreationDate.setText(self.data['creationDate'])
        self.labelLastModified.setText(self.data['lastModified'])
        self.LabelNeedForChange.setText('Изменения не требуются' if self.data['needForChange']!= True else 'Изменения требуются')
        self.LavelOldWersion.setText('Несогласованная верси есть' if self.data['newDockVersion'] else 'Несогласованной версии нет')
        self.pushButtonDownloadNew.clicked.connect(self.downloadNewTp)
        self.pushButtonDownloadOld.clicked.connect(self.downloadNewNewTp)
        
    def downloadNewTp(self):
        url = self.data['currentVersionTP']
        save_path = self.lineEditPathNewTP.text()
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_path, "ТП" + " " + self.data['TpName'] + ".docx")
            try:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    file.close()
            except:
                pass


    def downloadNewNewTp(self):
        url = self.data['newDockVersion']
        save_path = self.lineEditPathOldTP.text()
        if url is None:
            return
        response = requests.get(url)
        if response.status_code == 200:
            #print('Мы в условии')
            file_path = os.path.join(save_path, "Не согласованый ТП" + " " + self.data['TpName'] + ".docx")
            try:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    file.close()
            except:
                #print("Мы в эксепшане")
                pass

    def go_back(self):
        self.close()
        self.parent().show()




# Отправляем GET-запрос для загрузки файла


# Проверяем, успешно ли загружен файл
