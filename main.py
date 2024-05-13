import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Auth.authClass import AuthWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec_())