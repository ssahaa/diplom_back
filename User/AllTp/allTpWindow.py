import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.Alltp import Ui_ALLTPS
from User.AllTp.functions import getTp, getOldTP
from User.AllTp.TpCard.TpCardWindow import TpCard
from User.AllTp.OldTpCard.OldTpCardWindow import OldTpCard
import User.MainWinodw as m
class AllTP(QMainWindow, Ui_ALLTPS):
    def __init__(self, parent=None, UserData = {}):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButtonBack.clicked.connect(self.go_back)
        self.initUI()
        self.tableWidgetAcrualTP.cellClicked.connect(self.clickTp)
        self.tableWidgetOldTP.cellClicked.connect(self.clickedOldTp)
        self.userD = UserData
    
    def initUI(self):
        dataTP = getTp()
        oldTP = getOldTP()
        self.dataTP = dataTP
        self.dataOld = oldTP
        for i in range(len(dataTP)):
            actualRow = self.tableWidgetAcrualTP.rowCount()
            self.tableWidgetAcrualTP.insertRow(actualRow)
            self.tableWidgetAcrualTP.setItem(actualRow, 0, QTableWidgetItem(dataTP[i]['TpName']))
            self.tableWidgetAcrualTP.setItem(actualRow, 1, QTableWidgetItem(dataTP[i]['lastModified']))

        for i in range(len(oldTP)):
            actualRow = self.tableWidgetOldTP.rowCount()
            self.tableWidgetOldTP.insertRow(actualRow)
            self.tableWidgetOldTP.setItem(actualRow, 0, QTableWidgetItem(dataTP[i]['TpName']))
            self.tableWidgetOldTP.setItem(actualRow, 1, QTableWidgetItem(dataTP[i]['lastModified']))
    
    def clickTp(self,row, column):
        self.hide()
        data = self.dataTP[row]
        self.TPCardW = TpCard(self,data=data)
        self.TPCardW.show()
        
        #self.close()
        #newWindowAllTP = Ui_MainWindow(self)
        #newWindowAllTP.show()

    def clickedOldTp(self, row, column):
        self.hide()
        data = self.dataOld[row]
        dataMainTp = self.dataTP[row]
        self.OldTPCardW = OldTpCard(self,data=data, dataMainTP=dataMainTp)
        self.OldTPCardW.show()

    def go_back(self):
        #self.close()
        #self.parent().show()

        self.menu = m.UserWindow(UserData=self.userD)
        self.menu.show()
        self.close()