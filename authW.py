# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1276, 617)
        Dialog.setStyleSheet("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 160, 81, 255), stop:1 rgba(255, 120, 161, 255))qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(136, 160, 152, 255), stop:1 rgba(248, 255, 198, 255))")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("padding: 10;\n"
"font-size: 30px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(17, 53, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.labelLogin = QtWidgets.QLabel(Dialog)
        self.labelLogin.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.labelLogin.setObjectName("labelLogin")
        self.gridLayout.addWidget(self.labelLogin, 0, 0, 1, 1)
        self.lineEditLogin = QtWidgets.QLineEdit(Dialog)
        self.lineEditLogin.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEditLogin.setStyleSheet("background:rgb(243, 255, 234)")
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.gridLayout.addWidget(self.lineEditLogin, 0, 1, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setMinimumSize(QtCore.QSize(0, 60))
        self.lineEditPassword.setStyleSheet("background:rgb(243, 255, 234)")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 1, 1, 1, 1)
        self.labelPassword = QtWidgets.QLabel(Dialog)
        self.labelPassword.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.labelPassword.setObjectName("labelPassword")
        self.gridLayout.addWidget(self.labelPassword, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(17, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setStyleSheet("background:rgb(243, 255, 234);\n"
"padding: 10;\n"
"font-size: 15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:23pt;\">Введите Логин и Пароль</span></p></body></html>"))
        self.labelLogin.setText(_translate("Dialog", "Логин"))
        self.labelPassword.setText(_translate("Dialog", "Пароль"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "Выход"))