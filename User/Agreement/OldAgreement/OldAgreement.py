import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.OldAgreement import Ui_OldAgreement
import User.Agreement.ALLAgreementWindow as m
from PyQt5.QtGui import QIcon
import requests
from User.Agreement.CreateAgreement.AllTPAGreementWindow import CreateAgreementALLTP
from User.Agreement.AgreementNew.AgreementNewWIndow import NewAgreement
from User.Agreement.BadAgreement.BadAgreeemntWindow import BadAgreement
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window
class OldAgreement(QMainWindow, Ui_OldAgreement):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('') ):
        super().__init__(parent)
        self.setupUi(self)
        self.icon = icon
        self.userD = UserData
        self.pushButtonBack.clicked.connect(self.go_back)
        self.dataAgreeement = requests.get('http://127.0.0.1:8000/Согласование%20ТП/').json()
        self.dataTP = requests.get('http://127.0.0.1:8000/ТП/').json()
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)

        for i in range(len(self.dataAgreeement)):
            flag = 1
            actualRow = self.tableWidgetAllAgreement.rowCount()
            self.tableWidgetAllAgreement.insertRow(actualRow)

            for j in range(len(self.dataTP)):
                if self.dataTP[j]['id'] == self.dataAgreeement[i]['idTP']:
                    name = self.dataTP[j]['TpName']

            if self.dataAgreeement[i]['isActual'] == True:
                flag = 0
            if flag == 1:
                self.tableWidgetAllAgreement.setItem(actualRow, 0, QTableWidgetItem(name if self.dataAgreeement[i]['IsNewTP'] == False else self.dataAgreeement[i]['NewName']))
                self.tableWidgetAllAgreement.setItem(actualRow, 1, QTableWidgetItem(self.dataAgreeement[i]['comment']))
                self.tableWidgetAllAgreement.setItem(actualRow, 2, QTableWidgetItem(self.dataAgreeement[i]['AdminComment']))
                self.tableWidgetAllAgreement.setItem(actualRow, 3, QTableWidgetItem("Создание нового ТП" if self.dataAgreeement[i]['IsNewTP'] == True else "Внесение изменений"))
            else:
                self.tableWidgetAllAgreement.setRowHidden(actualRow, True)
            

    def go_back(self):
        self.menu = m.AllAgreementUser(UserData=self.userD, icon=self.icon)
        self.menu.show()
        self.close()