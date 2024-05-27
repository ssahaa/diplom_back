import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Auth.authFunctions import *
from WindowsPY.authW import Ui_AuthMainWindow
import requests
from WindowsPY.userW import Ui_MainWindow
from User.MainWinodw import UserWindow
from Adminestrator.Admin import AdminWindow
import os
from PyQt5.QtGui import QIcon
import ctypes
class AuthWindow(QMainWindow):
    def __init__(self):
        myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        super().__init__()
        self.ui = Ui_AuthMainWindow()
        self.ui.setupUi(self)
        #self.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.authentication)
        self.ui.pushButton_9.clicked.connect(self.close)
        self.users = requests.get('http://127.0.0.1:8000/Пользователи/')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path[:-4]
        self.icon = QIcon(dir_path + r'Icons\icon.png')
        self.setWindowIcon(self.icon)



    def authentication(self):
        username = self.ui.lineEditLogin_5.text()
        password = self.ui.lineEditPassword_5.text()
        #print(f"Пользователь: {username}, Пароль: {password}")
       # QMessageBox.information(self.centralwidget, "Ошибка", '123123')
        
        if (isCurrentLogin(username, password)):
            UserData = setUser(username, password)
            self.userData = UserData
            if(isAdministrator(username, password)):
                self.menu = AdminWindow(UserData=self.userData)
                self.menu.show()
                self.close()
                return
            self.menu = UserWindow(UserData=self.userData)
            self.menu.show()
            self.close()
        else:
            QMessageBox.information(self.centralWidget(), "Ошибка", "Введите верные данные")
        #self.hide()  # Скройте текущее окно вместо закрытия
        #User_Window = UserWindow(self)  # Передайте self в качестве родительского окна
        #User_Window.show()




