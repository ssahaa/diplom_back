import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox, QVBoxLayout, QMessageBox, QFileDialog, QTableWidgetItem
from WindowsPY.AllGosts import Ui_AllGosts
from User.AllGosts.functions import getGost
import requests
import os
import User.MainWinodw as m

class AllGost(QMainWindow, Ui_AllGosts):
    def __init__(self, parent=None, UserData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButtonBack.clicked.connect(self.go_back)
        self.tableWidgetAcrualTP.cellClicked.connect(self.clickGOST)
        self.initUI()
        self.userD = UserData
    def initUI(self):
        self.dataTP = getGost()
        for i in range(len(self.dataTP)):
            actualRow = self.tableWidgetAcrualTP.rowCount()
            self.tableWidgetAcrualTP.insertRow(actualRow)
            self.tableWidgetAcrualTP.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[i]['gostName']))
            self.tableWidgetAcrualTP.setItem(actualRow, 1, QTableWidgetItem(self.dataTP[i]['lastModified']))
            self.tableWidgetAcrualTP.setItem(actualRow, 2, QTableWidgetItem(self.dataTP[i]['creationDate']))

    def clickGOST(self, row, column):
        self.data = self.dataTP[row]
        url = self.data['file']
        save_path = self.lineEditPathDownload.text()
        if len(save_path) < 1:
            QMessageBox.information(self.centralwidget, "Ошибка", "Укажите путь для загрузки ТП")
            return
        response = requests.get(url)


        if response.status_code == 200:
            #print('Мы в условии')
            file_path = os.path.join(save_path, self.data['gostName'] + ".docx")
            try:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    file.close()
                QMessageBox.information(self.centralwidget, "Успех", "ГОСТ загружен")
            except:
                QMessageBox.information(self.centralwidget, "Ошибка", "Укажите верный путь")
                pass

    def go_back(self):
        #self.close()
        #self.parent().show()  

        self.menu = m.UserWindow(UserData=self.userD)
        self.menu.show()
        self.close()
