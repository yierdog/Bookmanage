#图书类别添加模块
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from dao import bookTypeDao
from entity.BookTypeModel import BookType
class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint) #只显示最小化和关键按钮
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(444, 299)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.bookTypeNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bookTypeNameInput.setObjectName("bookTypeNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bookTypeNameInput)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.bookTypeDescInput = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.bookTypeDescInput.setObjectName("bookTypeDescInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bookTypeDescInput)
        self.addBtn = QtWidgets.QPushButton(Form)
        self.addBtn.setGeometry(QtCore.QRect(130, 240, 93, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setObjectName("addBtn")

        #添加按钮绑定事件
        self.addBtn.clicked.connect(self.add)

        self.resetBtn = QtWidgets.QPushButton(Form)
        self.resetBtn.setGeometry(QtCore.QRect(290, 240, 93, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetBtn.setIcon(icon1)
        self.resetBtn.setObjectName("resetBtn")


        #绑定重置按钮的点击事件
        self.resetBtn.clicked.connect(self.reset)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书类别添加"))
        self.label.setText(_translate("Form", "图书类别名称"))
        self.label_2.setText(_translate("Form", "图书类别描述"))
        self.addBtn.setText(_translate("Form", "添加"))
        self.resetBtn.setText(_translate("Form", "重置"))

    #重置
    def reset(self):
        self.bookTypeNameInput.setText("")
        self.bookTypeDescInput.setPlainText("")

    def add(self):
        """
        添加图书类别信息
        :return:
        """
        bookTypeName=self.bookTypeNameInput.text()
        bookTypeDesc=self.bookTypeDescInput.toPlainText()
        if bookTypeName.strip()=="":
            QMessageBox.warning(None,'系统提示','图书类别名称不能为空！')
        else:
            booktype=BookType(bookTypeName,bookTypeDesc)
            if bookTypeDao.add(booktype)>0:
                QMessageBox.information(None,'系统提示','添加成功！')
                self.reset()
            else:
                QMessageBox.warning(None,'系统提示','图书类别名称不能为空！')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=Ui_Form()
    ui.show()

    sys.exit(app.exec())