# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.SendButton.setObjectName("SendButton")
        self.RequestButton = QtWidgets.QPushButton(self.centralwidget)
        self.RequestButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.RequestButton.setObjectName("RequestButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 47, 13))
        self.label.setObjectName("label")
        self.HRvalueLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.HRvalueLineEdit.setGeometry(QtCore.QRect(10, 50, 71, 20))
        self.HRvalueLineEdit.setObjectName("HRvalueLineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SendButton.setText(_translate("MainWindow", "Send"))
        self.RequestButton.setText(_translate("MainWindow", "Request"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
