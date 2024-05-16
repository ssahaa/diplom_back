import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WindowsPY.userW import Ui_MainWindow
from User.CreateTp.CreateTpWindow import CreateTP
from User.AllTp.allTpWindow import AllTP
import datetime
class UserWindow(QMainWindow):
    def __init__(self, parent=None, UserData={}):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.userD = UserData
        #print(self.userD)
        self.ui.labelFIO.setText(self.userD['userSurname'] + ' ' + self.userD['userName'] + ' ' + self.userD['userMiddleName'])
        dateNOW = str(datetime.datetime.now())
        self.ui.labelDATE.setText(dateNOW[0:10])
        self.ui.pushButton_CreateTP.clicked.connect(self.createTP)
        self.ui.pushButton_Exit.clicked.connect(self.close)
        self.ui.pushButton_AllTP.clicked.connect(self.allTp)

    def createTP(self):
        self.hide()
        #new_windowTP = CreateTP(self, UserData = self.userD) 
        #new_windowTP.show()
        self.new_windowTP = CreateTP(self, UserData = self.userD) 
        self.new_windowTP.show()

    def allTp(self):
        self.hide()
        #self.allTp = AllTP(self)
        #self.allTp.show()
        #self.close()
        newWindowAllTP = AllTP(self)
        newWindowAllTP.show()