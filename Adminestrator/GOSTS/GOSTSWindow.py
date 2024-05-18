import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.Admin.AllTP import Ui_ALLTPS
#from User.AllTp.functions import getTp, getOldTP
from User.AllGosts.functions import getGost
from User.AllTp.OldTpCard.OldTpCardWindow import OldTpCard
import Adminestrator.Admin as m
from PyQt5.QtGui import QIcon
from WindowsPY.Admin.AllGosts import Ui_AllGosts
from Adminestrator.GOSTS.CreateGost.CreateGostWindow import CreateGOST


class ALLGosts(QMainWindow, Ui_AllGosts):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('') ):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.icon = icon
        self.userD = UserData
        #self.setWindowIcon(icon) 
    

    def initUI(self):
        self.dataGOST = getGost()
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushCreateGost.clicked.connect(self.CreateGost)
        self.tableWidgetAcrualTP.cellClicked.connect(self.clickTp)
        for i in range(len(self.dataGOST)):
            actualRow = self.tableWidgetAcrualTP.rowCount()
            self.tableWidgetAcrualTP.insertRow(actualRow)
            self.tableWidgetAcrualTP.setItem(actualRow, 0, QTableWidgetItem(self.dataGOST[i]['gostName']))
            self.tableWidgetAcrualTP.setItem(actualRow, 1, QTableWidgetItem(self.dataGOST[i]['lastModified']))
            self.tableWidgetAcrualTP.setItem(actualRow, 2, QTableWidgetItem(self.dataGOST[i]['creationDate']))

    def CreateGost(self):
        self.createGOSTS = CreateGOST(UserData=self.userD, icon=self.icon)
        self.createGOSTS.setWindowIcon(self.icon) 
        self.createGOSTS.show()
        self.close()


    def clickTp(self,row, column):
        return
        data = self.dataTP[row]
        self.TpCatdW = TpCard(UserD = self.userD, dataTP = data, icon=self.icon)
        self.TpCatdW.setWindowIcon(self.icon) 
        self.TpCatdW.show()
        self.close()

    def go_back(self):
        #self.close()
        #self.parent().show()
        self.menu = m.AdminWindow(UserData=self.userD)
        self.menu.show()
        self.close()