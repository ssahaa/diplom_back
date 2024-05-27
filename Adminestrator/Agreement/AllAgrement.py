import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.Admin.AllAgreement import Ui_Argreement
import Adminestrator.Admin as m
from PyQt5.QtGui import QIcon
import requests
from Adminestrator.Agreement.CreateTP.CreateTPWindow import CreateTPAgreement
from Adminestrator.Agreement.NormalAgreement.NormalAgreement import AgreementNormal
from Adminestrator.OLDAgreement.OldAgreeementWindow import OldAgreement
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class AllAgreement(QMainWindow, Ui_Argreement):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('') ):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.icon = icon
        self.userD = UserData
        #self.setWindowIcon(icon) 
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)
    

    def initUI(self):
        self.pushButtonBack.clicked.connect(self.go_back)
        self.tableWidgetAllAgreement.cellClicked.connect(self.clickAgreement)
        self.pushButtonCheckOldAgreement.clicked.connect(self.clickOldAgreement)
        data = requests.get('http://127.0.0.1:8000/Согласование%20ТП/')
        dataTP = requests.get('http://127.0.0.1:8000/ТП/')
        self.agreementData = data.json()
        self.dataTP = dataTP.json()
        flag = 0
        self.tableWidgetAllAgreement.setShowGrid(False)
        self.tableWidgetAllAgreement.horizontalHeader().setVisible(True)
        self.tableWidgetAllAgreement.verticalHeader().setVisible(False)
        for i in range(len(self.agreementData)):
            if(self.agreementData[i]['isActual'] == True and self.agreementData[i]['IsUserAswerCommnet'] != False):
                actualRow = self.tableWidgetAllAgreement.rowCount()
                self.tableWidgetAllAgreement.insertRow(actualRow)
                for j in range(len(self.dataTP)):
                    if self.agreementData[i]['idTP'] == self.dataTP[j]['id']:
                        self.tableWidgetAllAgreement.setItem(actualRow, 0, QTableWidgetItem(self.dataTP[j]['TpName']))
                        self.tableWidgetAllAgreement.setItem(actualRow, 2, QTableWidgetItem('-'))
                        flag = 1
                if (flag == 0):
                    self.tableWidgetAllAgreement.setItem(actualRow, 0, QTableWidgetItem('Создание нового ТП'))
                    self.tableWidgetAllAgreement.setItem(actualRow, 2, QTableWidgetItem('+'))
                
                if self.agreementData[i]['NewName'] is None:
                    self.tableWidgetAllAgreement.setItem(actualRow, 1, QTableWidgetItem("Нет нового наименования"))
                else:
                    self.tableWidgetAllAgreement.setItem(actualRow, 1, QTableWidgetItem(self.agreementData[i]['NewName']))
                self.tableWidgetAllAgreement.setItem(actualRow, 3, QTableWidgetItem(self.agreementData[i]['comment']))
                flag = 0
            else:
                actualRow = self.tableWidgetAllAgreement.rowCount()
                self.tableWidgetAllAgreement.insertRow(actualRow)
                self.tableWidgetAllAgreement.setRowHidden(actualRow, True)


    def clickOldAgreement(self):
        self.AgreementCreateTP = OldAgreement(UserData=self.userD, icon=self.icon)
        self.AgreementCreateTP.setWindowIcon(self.icon) 
        self.AgreementCreateTP.show()
        self.close()

    def clickAgreement(self, row, column):
        pass
        if (self.agreementData[row]['IsNewTP'] == True):
            self.AgreementCreateTP = CreateTPAgreement(UserData=self.userD, icon=self.icon, agreementData = self.agreementData[row])
            self.AgreementCreateTP.setWindowIcon(self.icon) 
            self.AgreementCreateTP.show()
            self.close()
        else:
            self.AgreementCreateTP = AgreementNormal(UserData=self.userD, icon=self.icon, agreementData = self.agreementData[row])
            self.AgreementCreateTP.setWindowIcon(self.icon) 
            self.AgreementCreateTP.show()
            self.close()


    def go_back(self):
        self.menu = m.AdminWindow(UserData=self.userD)
        self.menu.show()
        self.close()