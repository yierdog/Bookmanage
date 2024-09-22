# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '图书类别维护.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(647, 646)
        self.bookTypeTable = QtWidgets.QTableWidget(Form)
        self.bookTypeTable.setGeometry(QtCore.QRect(30, 130, 571, 192))
        self.bookTypeTable.setObjectName("bookTypeTable")
        self.bookTypeTable.setColumnCount(0)
        self.bookTypeTable.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 571, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 30, 111, 21))
        self.label.setObjectName("label")
        self.s_bookTypeNameInput = QtWidgets.QLineEdit(self.groupBox)
        self.s_bookTypeNameInput.setGeometry(QtCore.QRect(190, 30, 191, 21))
        self.s_bookTypeNameInput.setObjectName("s_bookTypeNameInput")
        self.searchBtn = QtWidgets.QPushButton(self.groupBox)
        self.searchBtn.setGeometry(QtCore.QRect(410, 30, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setObjectName("searchBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 350, 571, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(240, 40, 101, 20))
        self.label_3.setObjectName("label_3")
        self.bookTypeNameInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.bookTypeNameInput.setGeometry(QtCore.QRect(350, 40, 201, 21))
        self.bookTypeNameInput.setObjectName("bookTypeNameInput")
        self.idInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.idInput.setGeometry(QtCore.QRect(110, 40, 81, 21))
        self.idInput.setObjectName("idInput")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 41, 16))
        self.label_4.setObjectName("label_4")
        self.bookTypeDescInput = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.bookTypeDescInput.setGeometry(QtCore.QRect(110, 90, 441, 81))
        self.bookTypeDescInput.setObjectName("bookTypeDescInput")
        self.modifyBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.modifyBtn.setGeometry(QtCore.QRect(70, 210, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/modify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifyBtn.setIcon(icon1)
        self.modifyBtn.setObjectName("modifyBtn")
        self.delBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.delBtn.setGeometry(QtCore.QRect(240, 210, 93, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delBtn.setIcon(icon2)
        self.delBtn.setObjectName("delBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书类别信息管理"))
        self.groupBox.setTitle(_translate("Form", "查询操作"))
        self.label.setText(_translate("Form", "图书类别名称："))
        self.searchBtn.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.label_2.setText(_translate("Form", "编号："))
        self.label_3.setText(_translate("Form", "图书类别描述："))
        self.label_4.setText(_translate("Form", "描述："))
        self.modifyBtn.setText(_translate("Form", "修改"))
        self.delBtn.setText(_translate("Form", "删除"))
