# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuthMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthMainWindow(object):
    def setupUi(self, AuthMainWindow):
        AuthMainWindow.setObjectName("AuthMainWindow")
        AuthMainWindow.resize(1463, 731)
        AuthMainWindow.setStyleSheet("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 160, 81, 255), stop:1 rgba(255, 120, 161, 255))qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(136, 160, 152, 255), stop:1 rgba(248, 255, 198, 255))")
        self.centralwidget = QtWidgets.QWidget(AuthMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("padding: 10;\n"
"font-size: 30px;")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 3)
        self.lineEditPassword_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword_5.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEditPassword_5.setStyleSheet("background:rgb(243, 255, 234)")
        self.lineEditPassword_5.setObjectName("lineEditPassword_5")
        self.lineEditPassword_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_5.addWidget(self.lineEditPassword_5, 3, 1, 1, 2)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_10.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 5, 0, 1, 2)
        self.labelLogin_5 = QtWidgets.QLabel(self.centralwidget)
        self.labelLogin_5.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.labelLogin_5.setObjectName("labelLogin_5")
        self.gridLayout_5.addWidget(self.labelLogin_5, 2, 0, 1, 1)
        self.lineEditLogin_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLogin_5.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEditLogin_5.setStyleSheet("background:rgb(243, 255, 234)")
        self.lineEditLogin_5.setObjectName("lineEditLogin_5")
        self.gridLayout_5.addWidget(self.lineEditLogin_5, 2, 1, 1, 2)
        self.labelPassword_5 = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword_5.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.labelPassword_5.setObjectName("labelPassword_5")
        self.gridLayout_5.addWidget(self.labelPassword_5, 3, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_9.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 6, 0, 1, 1)
        AuthMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AuthMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1463, 21))
        self.menubar.setObjectName("menubar")
        AuthMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AuthMainWindow)
        self.statusbar.setObjectName("statusbar")
        AuthMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthMainWindow)

    def retranslateUi(self, AuthMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthMainWindow.setWindowTitle(_translate("AuthMainWindow", "MainWindow"))
        self.label.setText(_translate("AuthMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:23pt;\">Введите Логин и Пароль</span></p></body></html>"))
        self.pushButton_10.setText(_translate("AuthMainWindow", "Войти"))
        self.labelLogin_5.setText(_translate("AuthMainWindow", "Логин"))
        self.labelPassword_5.setText(_translate("AuthMainWindow", "Пароль"))
        self.pushButton_9.setText(_translate("AuthMainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AuthMainWindow()
    ui.setupUi(AuthMainWindow)
    AuthMainWindow.show()
    sys.exit(app.exec_())