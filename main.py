#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import fuseGUI
import mainGUI  # import du fichier GUI.py généré par pyuic5

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainGUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('WFS.png'))
        self.setWindowTitle('Wii U File System Qt')
        
        
        # un clic sur le bouton appellera la méthode 'action_bouton'
        self.ui.pushButton.clicked.connect(self.action_bouton)
    
    def action_bouton(self):
        print('Appui bouton.')

    def on_item_changed(self):
        print(self.ui.listWidget.currentItem().text())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
