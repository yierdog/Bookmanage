# -*- coding: utf-8 -*-
#主界面
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from view.login import Ui_Form


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint) #只显示最小化和关键按钮
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 649)
        MainWindow.setMouseTracking(True)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/main(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/add(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon1)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setIcon(icon1)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/book(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_3.setIcon(icon2)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setIcon(icon)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image/modify(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_5.setIcon(icon3)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../image/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_6.setIcon(icon4)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_9 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../image/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_9.setIcon(icon5)
        self.action_9.setObjectName("action_9")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_9)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书管理系统"))
        self.menu.setTitle(_translate("MainWindow", "图书管理"))
        self.menu_2.setTitle(_translate("MainWindow", "图书类别管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统设置"))
        self.action.setText(_translate("MainWindow", "图书添加"))
        self.action_2.setText(_translate("MainWindow", "图书类别添加"))
        self.action_3.setText(_translate("MainWindow", "图书信息管理"))
        self.action_4.setText(_translate("MainWindow", "图书类别信息管理"))
        self.action_5.setText(_translate("MainWindow", "修改密码"))
        self.action_6.setText(_translate("MainWindow", "安全退出"))
        self.action_7.setText(_translate("MainWindow", "关于作者"))
        self.action_9.setText(_translate("MainWindow", "关于作者"))

#测试
if __name__ =='__main__':
    app=QApplication(sys.argv)
    ui=Ui_MainWindow()
    ui.show()

    sys.exit(app.exec())