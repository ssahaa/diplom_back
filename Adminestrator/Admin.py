import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WindowsPY.userW import Ui_MainWindow
from WindowsPY.Admin.Admin import Ui_AdminWindow
import os
from PyQt5.QtGui import QIcon
import datetime
from Adminestrator.AllTp.AllTpWindow import AllTP
from Adminestrator.GOSTS.GOSTSWindow import ALLGosts
class AdminWindow(QMainWindow, Ui_AdminWindow):
    def __init__(self, parent=None, UserData = {}):
        super().__init__(parent)
        self.userD = UserData
        self.setupUi(self)
        self.setIcon()
        self.setupLabel()
        self.pushButton_Exit.clicked.connect(self.close)
        self.pushButton_TP.clicked.connect(self.AllTp)
        self.pushButton_GOST.clicked.connect(self.AllGosts)




    def AllTp(self):
        self.new_windowAllTP = AllTP(UserData = self.userD, icon=self.icon)
        self.new_windowAllTP.setWindowIcon(self.icon) 
        self.new_windowAllTP.show()
        self.close()


    def setupLabel(self):
        self.labelFIO.setText(self.userD['userSurname'] + ' ' + self.userD['userName'] + ' ' + self.userD['userMiddleName'])
        dateNOW = str(datetime.datetime.now())
        self.labelDATE.setText(dateNOW[0:10])

    def AllGosts(self):
        self.new_windowAllGOST = ALLGosts(UserData = self.userD, icon=self.icon)
        self.new_windowAllGOST.setWindowIcon(self.icon) 
        self.new_windowAllGOST.show()
        self.close()


    def setIcon(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path[:-13]
        self.icon = QIcon(dir_path + r'Icons\icon.png')
        self.setWindowIcon(self.icon)


