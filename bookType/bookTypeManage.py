# -*- coding: utf-8 -*-

import sys
from cProfile import runctx

# Form implementation generated from reading ui file '图书类别维护.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#图书类别管理模块,将数据库中的信息显示在该界面

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QSizePolicy, QAbstractItemView, QHeaderView, QTableWidget, \
    QTableWidgetItem, QMessageBox

from dao import bookTypeDao, bookDao
from entity.BookTypeModel import BookType


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint) #只显示最小化和关键按钮
        self.setupUi(self)
        self.initTable() #调用初始化表格

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(647, 646)
        self.bookTypeTable = QtWidgets.QTableWidget(Form)
        self.bookTypeTable.setGeometry(QtCore.QRect(30, 130, 571, 192))
        self.bookTypeTable.setObjectName("bookTypeTable")
        self.bookTypeTable.setColumnCount(0)
        self.bookTypeTable.setRowCount(0)

        #绑定行点击事件，获取行数据，设置表单
        self.bookTypeTable.clicked.connect(self.initForm)

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

        self.idInput.setReadOnly(True)#设置为只读，即可以在代码中向textEdit里面输入，但不能从界面上输入,没有这行代码即可以从界面输入
        self.idInput.setStyleSheet("background-color:gray") #设置背景为灰色

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

        #绑定修改按钮点击事件
        self.modifyBtn.clicked.connect(self.update)

        self.delBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.delBtn.setGeometry(QtCore.QRect(240, 210, 93, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delBtn.setIcon(icon2)
        self.delBtn.setObjectName("delBtn")

        #绑定删除按钮
        self.delBtn.clicked.connect(self.delete)

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
        self.label_3.setText(_translate("Form", "图书类别名称："))
        self.label_4.setText(_translate("Form", "描述："))
        self.modifyBtn.setText(_translate("Form", "修改"))
        self.delBtn.setText(_translate("Form", "删除"))

    #初始化表格
    def initTable(self):
        """
        根据条件初始化表格
        :param self:
        :return:
        """
        s_bookTypeName = self.s_bookTypeNameInput.text() #获取搜索条件(图书类别名称)
        result = bookTypeDao.list(s_bookTypeName)
        row = 0 #表格初始化0
        if result:
            row = len(result)
        self.bookTypeTable.setColumnCount(3)  #列
        self.bookTypeTable.setRowCount(row) #行
        self.bookTypeTable.verticalHeader().setVisible(False) #隐藏垂直标题 序号
        self.bookTypeTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) #禁止编辑单元格
        self.bookTypeTable.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding) #
        self.bookTypeTable.setHorizontalHeaderLabels(['编号','图书类别名称','描述']) #列标签
        self.bookTypeTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) #列头自适应
        self.bookTypeTable.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows #设置行的选择行为，以行为单位
        )

        for i in range(row): #行
            for j in range(3):  #列
                data=QTableWidgetItem(str(result[i][j])) #封装数据，第i行j列
                self.bookTypeTable.setItem(i,j,data)



    #表格点击事件获取数值  初始化
    def initForm(self,index:QModelIndex):  #点击事件获取回调index
        rowIndex=index.row() #获取行索引
        self.idInput.setText(self.bookTypeTable.item(rowIndex,0).text())#设置id编号
        self.bookTypeNameInput.setText(self.bookTypeTable.item(rowIndex, 1).text())  # 设置图书类别名称
        self.bookTypeDescInput.setPlainText(self.bookTypeTable.item(rowIndex, 2).text())  # 设置图书类别描述

    #更新表单
    def update(self):
        id=self.idInput.text()
        if id.strip()=="":
            QMessageBox.warning(None,'系统提示','请选中需要编辑的那一行记录！')
            return
        bookTypeName=self.bookTypeNameInput.text()
        if bookTypeName.strip()=="":
            QMessageBox.warning(None, '系统提示', '请输入图书类别名称！')
            return
        bookTypeDesc=self.bookTypeDescInput.toPlainText()
        bookType=BookType.my_constructor(id,bookTypeName,bookTypeDesc)
        if bookTypeDao.update(bookType)>0:
            QMessageBox.information(None,'系统提示','修改成功！')
            self.initTable()
        else:
            QMessageBox.information(None, '系统提示', '修改失败！')

    #删除
    def delete(self):
        id = self.idInput.text()
        if id.strip() == "":
            QMessageBox.warning(None, '系统提示', '请选中需要删除的那一行记录！')
            return
        reply=QMessageBox.question(self,'系统提示','您确定要删除这条记录吗？',QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                             QMessageBox.StandardButton.No) #确认框
        if reply==QMessageBox.StandardButton.Yes:
            #判断该图书类别下面是否有图书
            if bookDao.countBypeId(id)[0]>0: #有图书
                QMessageBox.information(None, '系统提示', '该类别下有图书，不能删除！')
                self.resetForm()
            else:
                if bookTypeDao.delete(id)>0:
                    QMessageBox.information(None,'系统提示','删除成功！')
                    self.initTable()
                    self.resetForm()
                else:
                    QMessageBox.information(None, '系统提示', '删除失败！')

    #重置
    def resetForm(self):
        self.idInput.setText("")
        self.bookTypeNameInput.setText("")
        self.bookTypeDescInput.setPlainText("")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ui=Ui_Form()
    ui.show()

    sys.exit(app.exec())