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
        self.ui.pushButton_3.clicked.connect(self.action_3)
        self.ui.pushButton_2.clicked.connect(self.action_2)
        self.ui.pushButton_5.clicked.connect(self.action_5)
        self.ui.pushButton_6.clicked.connect(self.action_6)
        self.ui.checkBox.toggled['bool'].connect(self.mlc)
        self.ui.checkBox_2.toggled['bool'].connect(self.device)

    def mount_action(self):
        seepromFile = self.ui.lineEdit.text()
        otpFile = self.ui.lineEdit_2.text()
        imgFile = self.ui.lineEdit_3.text()
        pathFile = self.ui.lineEdit_5.text()
        mntWre = self.ui.lineEdit_7.text()
        PassWord = self.ui.lineEdit_8.text()
        if self.ui.checkBox.isChecked() == False :
            MLC = "--usb"
        else:
            MLC = "--mlc"
        print(f'seeprom : {seepromFile}')
        os.system(f'echo {PassWord} | sudo -S ./wfs-fuse {imgFile} {mntWre} --otp {otpFile} --seeprom {seepromFile} -o allow_other {MLC}')

    def action_4(self):
        webbrowser.open("https://discord.gg/PynXrnU")

    def action_5(self):
        webbrowser.open("https://github.com/TriRetr0/Wii-U-File-System-QT")

    def action_6(self):
        webbrowser.open("https://github.com/koolkdev/wfslib")

    def action_3(self):
        if self.ui.checkBox.isChecked() == False :
            MLC = "--usb"
        else:
            MLC = "--mlc"
        seepromFile = self.ui.lineEdit.text()
        otpFile = self.ui.lineEdit_2.text()
        imgFile = self.ui.lineEdit_3.text()
        ExtFile = self.ui.lineEdit_6.text()
        OutDir = self.ui.lineEdit_9.text()
        os.system(f'./wfs-extract --input {imgFile} --otp {otpFile} --seeprom {seepromFile} --output {OutDir} --dump-path {ExtFile} {MLC}')

    def action_2(self):
        if self.ui.checkBox.isChecked() == False :
            MLC = "--usb"
        else:
            MLC = "--mlc"
        seepromFile = self.ui.lineEdit.text()
        otpFile = self.ui.lineEdit_2.text()
        imgFile = self.ui.lineEdit_3.text()
        injFile = self.ui.lineEdit_4.text()
        injPath = self.ui.lineEdit_5.text()
        os.system(f'./wfs-file-injector --image {imgFile} --inject-file {injFile} --inject-path {injPath} --otp {otpFile} --seeprom {seepromFile} {MLC}')

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
            self.ui.lineEdit_3.setText("/dev/???/")
        else:
            self.ui.label_3.setText("Image")
            self.ui.lineEdit_3.setText("")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
