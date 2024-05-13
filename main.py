import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
# Импортируйте код интерфейса нового окна
from WindowsPY.userW import Ui_MainWindow
from WindowsPY.authW import Ui_AuthMainWindow
from WindowsPY.createTPW import Ui_CreateTP


def iscurrentLogin(login = 0, password = 0):
    data = requests.get('http://127.0.0.1:8000/Пользователи/')

    for i in range(len(data.json())):
        if data.json()[i]['login'] == login:
            if data.json()[i]['password'] == password:
                return True
    return False

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
        if (iscurrentLogin(username, password)):
            self.menu = UserWindow()
            self.menu.show()
            self.close()
        #self.hide()  # Скройте текущее окно вместо закрытия
        #User_Window = UserWindow(self)  # Передайте self в качестве родительского окна
        #User_Window.show()

class UserWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_CreateTP.clicked.connect(self.createTP)
        self.ui.pushButton_Exit.clicked.connect(self.close)

    def createTP(self):
        self.hide()
        new_windowTP = CreateTP(self)  # Передайте self в качестве родительского окна
        new_windowTP.show()

class CreateTP(QMainWindow, Ui_CreateTP):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.go_back)

    def go_back(self):
        self.close()
        self.parent().show()  # Покажите родительское окно (UserWindow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec_())