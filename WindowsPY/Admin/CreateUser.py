# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        CreateUser.setObjectName("CreateUser")
        CreateUser.resize(946, 599)
        CreateUser.setStyleSheet("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 160, 81, 255), stop:1 rgba(255, 120, 161, 255))qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(136, 160, 152, 255), stop:1 rgba(248, 255, 198, 255))")
        self.centralwidget = QtWidgets.QWidget(CreateUser)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditPassword.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 4, 1, 1, 3)
        self.pushButtotBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtotBack.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtotBack.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.pushButtotBack.setObjectName("pushButtotBack")
        self.gridLayout.addWidget(self.pushButtotBack, 6, 3, 1, 2)
        self.pushButtonCreate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCreate.setMinimumSize(QtCore.QSize(250, 50))
        self.pushButtonCreate.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.gridLayout.addWidget(self.pushButtonCreate, 6, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        self.label_6.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEditLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLogin.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditLogin.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.gridLayout.addWidget(self.lineEditLogin, 3, 1, 1, 3)
        self.scrollAreaAllGrade = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaAllGrade.setMinimumSize(QtCore.QSize(0, 300))
        self.scrollAreaAllGrade.setStyleSheet("background:rgb(243, 255, 234);\n"
"font-size:16pt")
        self.scrollAreaAllGrade.setWidgetResizable(True)
        self.scrollAreaAllGrade.setObjectName("scrollAreaAllGrade")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 614, 298))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaAllGrade.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollAreaAllGrade, 0, 4, 5, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditOtch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOtch.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditOtch.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.lineEditOtch.setObjectName("lineEditOtch")
        self.gridLayout.addWidget(self.lineEditOtch, 2, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditFamil = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFamil.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditFamil.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.lineEditFamil.setObjectName("lineEditFamil")
        self.gridLayout.addWidget(self.lineEditFamil, 0, 1, 1, 3)
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEditName.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 3, 1, 1)
        CreateUser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateUser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        CreateUser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateUser)
        self.statusbar.setObjectName("statusbar")
        CreateUser.setStatusBar(self.statusbar)

        self.retranslateUi(CreateUser)
        QtCore.QMetaObject.connectSlotsByName(CreateUser)

    def retranslateUi(self, CreateUser):
        _translate = QtCore.QCoreApplication.translate
        CreateUser.setWindowTitle(_translate("CreateUser", "MainWindow"))
        self.label_5.setText(_translate("CreateUser", "Логин"))
        self.pushButtotBack.setText(_translate("CreateUser", "Назад"))
        self.pushButtonCreate.setText(_translate("CreateUser", "Создать"))
        self.label_6.setText(_translate("CreateUser", "Пароль"))
        self.label_3.setText(_translate("CreateUser", "Имя"))
        self.label_4.setText(_translate("CreateUser", "Отчество"))
        self.label.setText(_translate("CreateUser", "Фамилия"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateUser = QtWidgets.QMainWindow()
    ui = Ui_CreateUser()
    ui.setupUi(CreateUser)
    CreateUser.show()
    sys.exit(app.exec_())