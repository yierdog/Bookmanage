# -*- coding: utf-8 -*-
#图书添加模块
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from dao import bookTypeDao, bookDao
from entity.BookModel import Book


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint) #只显示最小化和关键按钮
        self.setupUi(self)

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
        self.bookTypeComboBox.setGeometry(QtCore.QRect(160, 210, 171, 22))
        self.bookTypeComboBox.setObjectName("bookTypeComboBox")

        #初始化下拉框
        self.initBookTypeLisComBox()

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

        #默认选中男
        self.manRadio.setChecked(True)

        self.femaleRadio = QtWidgets.QRadioButton(Form)
        self.femaleRadio.setGeometry(QtCore.QRect(220, 140, 51, 19))
        self.femaleRadio.setObjectName("femaleRadio")
        self.addBtn = QtWidgets.QPushButton(Form)
        self.addBtn.setGeometry(QtCore.QRect(130, 400, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/add(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setObjectName("addBtn")

        #添加按钮绑定事件
        self.addBtn.clicked.connect(self.add)

        self.resetBtn = QtWidgets.QPushButton(Form)
        self.resetBtn.setGeometry(QtCore.QRect(270, 400, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetBtn.setIcon(icon1)
        self.resetBtn.setObjectName("resetBtn")

        #重置按钮绑定点击事件
        self.resetBtn.clicked.connect(self.reset)

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

    #初始化下拉框数据
    def initBookTypeLisComBox(self):
        bookTypeList=bookTypeDao.list("") #获取图书类别信息
        self.bookTypeComboBox.addItem("请选择图书类别！",-1)
        for bookType in bookTypeList:
            self.bookTypeComboBox.addItem(bookType[1],bookType[0])

    def add(self):
        """
        添加图书信息
        :return:
        """
        bookName=self.bookNameInput.text()
        if bookName.strip()=="":
            QMessageBox.warning(None,'系统提示','图书名称不能为空！')
            return
        author=self.authorInput.text()
        if author.strip()=="":
            QMessageBox.warning(None,'系统提示','图书作者不能为空！')
            return
        sex=''
        if self.manRadio.isChecked():
            sex='男'
        else:
            sex='女'
        price=self.priceInput.text()
        if price.strip()=="":
            QMessageBox.warning(None,'系统提示','价格不能为空！')
            return
        bookTypeId=self.bookTypeComboBox.currentData()
        if bookTypeId==-1:
            QMessageBox.warning(None,'系统提示','请选择图书类别！')
            return
        bookDesc=self.bookDescInput.toPlainText()
        book=Book.my_constructor(bookName,author,sex,price,bookTypeId,bookDesc)
        if bookDao.add(book)>0:
            QMessageBox.information(None,'系统提示','添加成功！')
            self.reset()
        else:
            QMessageBox.warning(None,'系统提示','添加失败！')

    def reset(self):
        self.bookNameInput.setText("")
        self.authorInput.setText("")
        self.priceInput.setText("")
        self.manRadio.setChecked(True)
        self.bookTypeComboBox.setCurrentIndex(0)
        self.bookDescInput.setPlainText("")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=Ui_Form()
    ui.show()

    sys.exit(app.exec())