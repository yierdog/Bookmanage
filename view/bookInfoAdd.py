# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '图书信息添加.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(659, 489)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 140, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 72, 15))
        self.label_5.setObjectName("label_5")
        self.bookTypeComboBox = QtWidgets.QComboBox(Form)
        self.bookTypeComboBox.setGeometry(QtCore.QRect(160, 210, 87, 22))
        self.bookTypeComboBox.setObjectName("bookTypeComboBox")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 260, 72, 15))
        self.label_6.setObjectName("label_6")
        self.bookNameInput = QtWidgets.QLineEdit(Form)
        self.bookNameInput.setGeometry(QtCore.QRect(160, 80, 113, 21))
        self.bookNameInput.setObjectName("bookNameInput")
        self.authorInput = QtWidgets.QLineEdit(Form)
        self.authorInput.setGeometry(QtCore.QRect(430, 80, 113, 21))
        self.authorInput.setObjectName("authorInput")
        self.priceInput = QtWidgets.QLineEdit(Form)
        self.priceInput.setGeometry(QtCore.QRect(430, 140, 113, 21))
        self.priceInput.setObjectName("priceInput")
        self.bookDescInput = QtWidgets.QPlainTextEdit(Form)
        self.bookDescInput.setGeometry(QtCore.QRect(160, 260, 401, 87))
        self.bookDescInput.setObjectName("bookDescInput")
        self.manRadio = QtWidgets.QRadioButton(Form)
        self.manRadio.setGeometry(QtCore.QRect(160, 140, 51, 19))
        self.manRadio.setObjectName("manRadio")
        self.femaleRadio = QtWidgets.QRadioButton(Form)
        self.femaleRadio.setGeometry(QtCore.QRect(220, 140, 51, 19))
        self.femaleRadio.setObjectName("femaleRadio")
        self.addBtn = QtWidgets.QPushButton(Form)
        self.addBtn.setGeometry(QtCore.QRect(130, 400, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/add(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setObjectName("addBtn")
        self.resetBtn = QtWidgets.QPushButton(Form)
        self.resetBtn.setGeometry(QtCore.QRect(270, 400, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetBtn.setIcon(icon1)
        self.resetBtn.setObjectName("resetBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书信息添加"))
        self.label.setText(_translate("Form", "图书名称："))
        self.label_2.setText(_translate("Form", "图书作者："))
        self.label_3.setText(_translate("Form", "作者性别："))
        self.label_4.setText(_translate("Form", "图书价格："))
        self.label_5.setText(_translate("Form", "图书类别："))
        self.label_6.setText(_translate("Form", "图书描述："))
        self.manRadio.setText(_translate("Form", "男"))
        self.femaleRadio.setText(_translate("Form", "女"))
        self.addBtn.setText(_translate("Form", "添加"))
        self.resetBtn.setText(_translate("Form", "重置"))
