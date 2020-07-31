# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './wfs fuse.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(444, 166)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 130, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 161, 20))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(170, 60, 71, 26))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 60, 112, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 65, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(2, 65, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 100, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 95, 112, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(210, 95, 71, 26))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 100, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_3.setBuddy(Dialog.lineEdit_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "/!\\ Fuse is only for linux /!\\"))
        self.toolButton.setText(_translate("Dialog", "Choose"))
        self.label_2.setText(_translate("Dialog", "/dev/sd? to mount your USB"))
        self.label_3.setText(_translate("Dialog", "Image"))
        self.label_4.setText(_translate("Dialog", "Mount where ?"))
        self.toolButton_2.setText(_translate("Dialog", "Choose"))
        self.label_5.setText(_translate("Dialog", "Choose an empty folder"))

