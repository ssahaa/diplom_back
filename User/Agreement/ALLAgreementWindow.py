import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.AllAgreement import Ui_AllAgreementUser
import User.MainWinodw as m
from PyQt5.QtGui import QIcon
import requests
from User.Agreement.CreateAgreement.AllTPAGreementWindow import CreateAgreementALLTP
from User.Agreement.AgreementNew.AgreementNewWIndow import NewAgreement
from User.Agreement.BadAgreement.BadAgreeemntWindow import BadAgreement
from User.Agreement.OldAgreement.OldAgreement import OldAgreement
class AllAgreementUser(QMainWindow, Ui_AllAgreementUser):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('') ):
        super().__init__(parent)
        self.setupUi(self)
        self.icon = icon
        self.userD = UserData
        self.initUI()
        #self.setWindowIcon(icon) 
    

    def initUI(self):
        self.pushButtonBack.clicked.connect(self.go_back)
        self.tableWidgetAllAgreement.cellClicked.connect(self.clickNewAgreeement)
        self.tableWidgetAllAgreement_2.cellClicked.connect(self.clickBAdAgreement)
        self.pushButtonCreateNewAgreement.clicked.connect(self.clickCreateNewAgreement)
        self.pushButtonCheckOldAgreement.clicked.connect(self.OLdAgreement)
        data = requests.get('http://127.0.0.1:8000/Согласование%20ТП/')
        dataTP = requests.get('http://127.0.0.1:8000/ТП/')
        self.agreementData = data.json()
        self.dataTP = dataTP.json()
        self.agreementData = data.json()
        for i in range(len(self.agreementData)):
            if (self.agreementData[i]['IsUserAswerCommnet'] != True and self.agreementData[i]['isActual'] == True and self.agreementData[i]['result'] == False and self.agreementData[i]['creator'] == self.userD['id']):
                if self.agreementData[i]['IsUserAswerCommnet'] != False:
                    actualRow = self.tableWidgetAllAgreement.rowCount()
                    self.tableWidgetAllAgreement.insertRow(actualRow)
                    for j in range(len(self.dataTP)):
                        if self.agreementData[i]['idTP'] == self.dataTP[j]['id']:
                            if self.agreementData[i]['isActual'] == True:
                                self.tableWidgetAllAgreement.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[j]['TpName']))
                    if (self.agreementData[i]['IsNewTP'] == True):
                        if self.agreementData[i]['isActual'] == True:
                            self.tableWidgetAllAgreement.setItem(actualRow, 0, QTableWidgetItem(self.agreementData[i]['NewName']))

                    self.tableWidgetAllAgreement.setItem(actualRow, 1, QTableWidgetItem(self.agreementData[i]['creationDate']))
                    if (self.agreementData[i]['IsNewTP'] == True):
                        self.tableWidgetAllAgreement.setItem(actualRow, 2, QTableWidgetItem('Создание ТП'))
                    else:
                        self.tableWidgetAllAgreement.setItem(actualRow, 2, QTableWidgetItem('Изменение данных о ТП'))
            else:
                actualRow = self.tableWidgetAllAgreement.rowCount()
                self.tableWidgetAllAgreement.insertRow(actualRow)
                self.tableWidgetAllAgreement.setRowHidden(actualRow, True)

            
        for i in range(len(self.agreementData)):
            if ((self.agreementData[i]['IsUserAswerCommnet'] == False) and self.agreementData[i]['isActual'] == True and self.agreementData[i]['result'] == False and self.agreementData[i]['creator'] == self.userD['id']):
                actualRow = self.tableWidgetAllAgreement_2.rowCount()
                self.tableWidgetAllAgreement_2.insertRow(actualRow)
                for j in range(len(self.dataTP)):
                    if self.agreementData[i]['idTP'] == self.dataTP[j]['id']:
                        if self.agreementData[i]['isActual'] == True:
                            self.tableWidgetAllAgreement_2.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[j]['TpName']))
                if (self.agreementData[i]['IsNewTP'] == True):
                    if self.agreementData[i]['isActual'] == True:
                        self.tableWidgetAllAgreement_2.setItem(actualRow, 0, QTableWidgetItem(self.agreementData[i]['NewName']))

                self.tableWidgetAllAgreement_2.setItem(actualRow, 1, QTableWidgetItem(self.agreementData[i]['creationDate']))
                self.tableWidgetAllAgreement_2.setItem(actualRow, 2, QTableWidgetItem(self.agreementData[i]['AdminComment']))
            else:
                actualRow = self.tableWidgetAllAgreement_2.rowCount()
                self.tableWidgetAllAgreement_2.insertRow(actualRow)
                self.tableWidgetAllAgreement_2.setRowHidden(actualRow, True)
                
    
    def clickNewAgreeement(self, row, column):
        self.createGOSTS = NewAgreement(UserData=self.userD, icon=self.icon, agreementData = self.agreementData[row])
        self.createGOSTS.setWindowIcon(self.icon) 
        self.createGOSTS.show()
        self.close()

    def clickBAdAgreement(self, row, column):
        self.createGOSTS = BadAgreement(UserData=self.userD, icon=self.icon, agreementData = self.agreementData[row])
        self.createGOSTS.setWindowIcon(self.icon) 
        self.createGOSTS.show()
        self.close()

    def clickCreateNewAgreement(self):
        self.createGOSTS = CreateAgreementALLTP(UserData=self.userD, icon=self.icon)
        self.createGOSTS.setWindowIcon(self.icon) 
        self.createGOSTS.show()
        self.close()

    def OLdAgreement(self):
        self.OldAgreement = OldAgreement(UserData=self.userD, icon=self.icon)
        self.OldAgreement.setWindowIcon(self.icon) 
        self.OldAgreement.show()
        self.close()

    def go_back(self):
        self.menu = m.UserWindow(UserData=self.userD)
        self.menu.show()
        self.close()