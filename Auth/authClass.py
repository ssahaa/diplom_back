import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Auth.authFunctions import *
from WindowsPY.authW import Ui_AuthMainWindow
import requests
from WindowsPY.userW import Ui_MainWindow
from User.MainWinodw import UserWindow
from Adminestrator.Admin import AdminWindow

class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AuthMainWindow()
        self.ui.setupUi(self)
        #self.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.authentication)
        self.ui.pushButton_9.clicked.connect(self.close)
        self.users = requests.get('http://127.0.0.1:8000/Пользователи/')

    def authentication(self):
        username = self.ui.lineEditLogin_5.text()
        password = self.ui.lineEditPassword_5.text()
        #print(f"Пользователь: {username}, Пароль: {password}")
        if (isCurrentLogin(username, password)):
            UserData = setUser(username, password)
            self.userData = UserData
            if(isAdministrator(username, password)):
                self.menu = AdminWindow()
                self.menu.show()
                self.close()
            self.menu = UserWindow(UserData=self.userData)
            self.menu.show()
            self.close()
        #self.hide()  # Скройте текущее окно вместо закрытия
        #User_Window = UserWindow(self)  # Передайте self в качестве родительского окна
        #User_Window.show()




