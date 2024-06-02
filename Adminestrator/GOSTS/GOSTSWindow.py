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
from Adminestrator.GOSTS.ChangeGost.ChangeGostWindow import ChangeGost
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window

class ALLGosts(QMainWindow, Ui_AllGosts):
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
        self.dataGOST = getGost()
        self.pushButtonBack.clicked.connect(self.go_back)
        self.pushCreateGost.clicked.connect(self.CreateGost)
        self.tableWidgetAcrualTP.cellClicked.connect(self.changeGost)
        for i in range(len(self.dataGOST)):
            actualRow = self.tableWidgetAcrualTP.rowCount()
            self.tableWidgetAcrualTP.insertRow(actualRow)
            self.tableWidgetAcrualTP.setItem(actualRow, 0, QTableWidgetItem(self.dataGOST[i]['gostName']+ ' ' + self.dataGOST[i]['gostNameReal']))
            self.tableWidgetAcrualTP.setItem(actualRow, 1, QTableWidgetItem(self.dataGOST[i]['lastModified']))
            self.tableWidgetAcrualTP.setItem(actualRow, 2, QTableWidgetItem(self.dataGOST[i]['creationDate']))

    def CreateGost(self):
        self.createGOSTS = CreateGOST(UserData=self.userD, icon=self.icon)
        self.createGOSTS.setWindowIcon(self.icon) 
        self.createGOSTS.show()
        self.close()

    def changeGost(self,row, column):
        data = self.dataGOST[row]
        self.new_windowAllGOST = ChangeGost(UserData = self.userD, icon=self.icon, dataGost=data)
        self.new_windowAllGOST.setWindowIcon(self.icon) 
        self.new_windowAllGOST.show()
        self.close()

    def go_back(self):
        #self.close()
        #self.parent().show()
        self.menu = m.AdminWindow(UserData=self.userD)
        self.menu.show()
        self.close()