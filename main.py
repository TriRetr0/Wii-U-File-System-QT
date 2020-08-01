#!/usr/bin/python3
# -*- coding: utf-8 -*-
import webbrowser
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import mainGUI

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainGUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('WFS.png'))
        self.setWindowTitle('Wii U File System Qt')

        self.ui.pushButton.clicked.connect(self.mount_action)
        self.ui.pushButton_4.clicked.connect(self.action_4)
        self.ui.pushButton_5.clicked.connect(self.action_5)
        self.ui.pushButton_6.clicked.connect(self.action_6)
        self.ui.lineEdit.editingFinished.connect(self.seeprom)
        self.ui.lineEdit_2.editingFinished.connect(self.otp)
        self.ui.lineEdit_3.editingFinished.connect(self.img)
        self.ui.lineEdit_4.editingFinished.connect(self.filein)
        self.ui.lineEdit_5.editingFinished.connect(self.path)
        self.ui.lineEdit_6.editingFinished.connect(self.fileex)
        self.ui.lineEdit_7.editingFinished.connect(self.mount)
        self.ui.checkBox.toggled['bool'].connect(self.mlc)
        self.ui.checkBox_2.toggled['bool'].connect(self.device)


    def mount_action(self):
        os.system("./wfs-fuse --image ")

    def action_4(self):
        webbrowser.open("https://discord.gg/PynXrnU")

    def action_5(self):
        webbrowser.open("https://github.com/TriRetr0/Wii-U-File-System-QT")

    def action_6(self):
        webbrowser.open("https://github.com/koolkdev/wfslib")

    def seeprom(self):
        print(self.ui.lineEdit.text())

    def otp(self):
        print(self.ui.lineEdit_2.text())

    def img(self):
        print(self.ui.lineEdit_3.text())

    def filein(self):
        print(self.ui.lineEdit_4.text())

    def path(self):
        print(self.ui.lineEdit_5.text())

    def fileex(self):
        print(self.ui.lineEdit_6.text())

    def mount(self):
        print(self.ui.lineEdit_7.text())

    def mlc(self):
        if self.ui.checkBox.isChecked() == False :
            self.ui.lineEdit.setEnabled(True)
            self.ui.toolButton.setEnabled(True)
            self.ui.label.setEnabled(True)
        else:
            self.ui.lineEdit.setEnabled(False)
            self.ui.toolButton.setEnabled(False)
            self.ui.label.setEnabled(False)

    def device(self):
        if self.ui.checkBox_2.isChecked() == True :
            self.ui.label_3.setText("Device")
            self.ui.lineEdit_3.setText("/dev/sd?")
        else:
            self.ui.label_3.setText("Image")
            self.ui.lineEdit_3.setText("")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
