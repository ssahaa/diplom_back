import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WindowsPY.userW import Ui_MainWindow
from User.CreateTp.CreateTpWindow import CreateTP
from User.AllTp.allTpWindow import AllTP
from User.AllGosts.AllGostsWindow import AllGost
from User.NeedChange.NeedChangeWindow import NeedChange
from User.Agreement.ALLAgreementWindow import AllAgreementUser
import datetime
import os
from PyQt5.QtGui import QIcon
from WindowSet import WINDOW_HEIGHT, WINDOW_WIDTH, center_window



class UserWindow(QMainWindow):
    def __init__(self, parent=None, UserData={}):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.userD = UserData

        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        center_window(self)


        #print(self.userD)
        self.ui.labelFIO.setText(self.userD['userSurname'] + ' ' + self.userD['userName'] + ' ' + self.userD['userMiddleName'])
        dateNOW = str(datetime.datetime.now())
        self.ui.labelDATE.setText(dateNOW[0:10])
        self.ui.pushButton_CreateTP.clicked.connect(self.createTP)
        self.ui.pushButton_Exit.clicked.connect(self.close)
        self.ui.pushButton_AllTP.clicked.connect(self.allTp)
        self.ui.pushButton_NeedToChange.clicked.connect(self.NeedChange)
        self.ui.pushButton_AllGOST.clicked.connect(self.AllGosts)
        self.ui.pushButton_approveTP.clicked.connect(self.AllAgeementUser)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path[:-4]
        self.icon = QIcon(dir_path + r'Icons\icon.png')
        self.setWindowIcon(self.icon)


    def createTP(self):
        self.new_windowTP = CreateTP(UserData = self.userD) 
        self.new_windowTP.setWindowIcon(self.icon)  
        self.new_windowTP.show()
        self.close()


    def allTp(self):
        #self.hide()

        self.newWindowAllTP = AllTP(UserData = self.userD)
        self.newWindowAllTP.setWindowIcon(self.icon)  
        self.newWindowAllTP.show()
        self.close()
        #newWindowAllTP.show()
    
    def AllGosts(self):
        #self.hide()
        self.new_windowAllGosts = AllGost(UserData = self.userD)
        self.new_windowAllGosts.setWindowIcon(self.icon) 
        self.new_windowAllGosts.show()
        self.close()

    def NeedChange(self):
        #self.hide()
        self.new_windowNeedChange = NeedChange(UserData = self.userD)
        self.new_windowNeedChange.setWindowIcon(self.icon) 
        self.new_windowNeedChange.show()
        self.close()

    def AllAgeementUser(self):
        self.new_windowAllAgreement = AllAgreementUser(UserData = self.userD, icon=self.icon)
        self.new_windowAllAgreement.setWindowIcon(self.icon) 
        self.new_windowAllAgreement.show()
        self.close()


