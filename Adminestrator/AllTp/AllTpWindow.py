import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from WindowsPY.Admin.AllTP import Ui_ALLTPS
from User.AllTp.functions import getTp, getOldTP
from User.AllTp.OldTpCard.OldTpCardWindow import OldTpCard
import Adminestrator.Admin as m
from PyQt5.QtGui import QIcon
from Adminestrator.AllTp.TpCard.TpCardWindow import TpCard




class AllTP(QMainWindow, Ui_ALLTPS):
    def __init__(self, parent=None, UserData = {}, icon = QIcon('') ):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.icon = icon
        self.userD = UserData
        #self.setWindowIcon(icon) 
    

    def initUI(self):
        dataTP = getTp()
        oldTP = getOldTP()
        self.dataTP = dataTP
        self.dataOld = oldTP
        self.pushButtonBack.clicked.connect(self.go_back)
        self.tableWidgetAcrualTP.cellClicked.connect(self.clickTp)
        for i in range(len(dataTP)):
            actualRow = self.tableWidgetAcrualTP.rowCount()
            self.tableWidgetAcrualTP.insertRow(actualRow)
            self.tableWidgetAcrualTP.setItem(actualRow, 0, QTableWidgetItem(dataTP[i]['TpName']))



    def clickTp(self,row, column):
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