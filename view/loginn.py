# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#管理员登录模块

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 311)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 100, 301, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.usernameinput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameinput.setObjectName("usernameinput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameinput)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.passwordinpurt = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordinpurt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordinpurt.setObjectName("passwordinpurt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordinpurt)
        self.loginbtn = QtWidgets.QPushButton(Form)
        self.loginbtn.setGeometry(QtCore.QRect(130, 210, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbtn.setIcon(icon)
        self.loginbtn.setObjectName("loginbtn")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 210, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../image/book(2).png"))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员登录"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密  码："))
        self.loginbtn.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.label_3.setText(_translate("Form", "图书管理系统"))

#测试
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=Ui_Form()
    ui.show()

    sys.exit(app.exec())