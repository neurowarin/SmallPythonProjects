# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\uipython\rgr\inter.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(209, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 320, 201, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 201, 311))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 70, 201, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 110, 201, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 150, 201, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 190, 201, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 230, 201, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 270, 201, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аттрактор Лоренца"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.groupBox.setTitle(_translate("MainWindow", "Start condition"))
        self.radioButton.setText(_translate("MainWindow", "r=0,3"))
        self.radioButton_2.setText(_translate("MainWindow", "r=1,8"))
        self.radioButton_3.setText(_translate("MainWindow", "r=3,7"))
        self.radioButton_4.setText(_translate("MainWindow", "r=10"))
        self.radioButton_5.setText(_translate("MainWindow", "r=16"))
        self.radioButton_6.setText(_translate("MainWindow", "r=24.06"))
        self.radioButton_7.setText(_translate("MainWindow", "r=28"))

