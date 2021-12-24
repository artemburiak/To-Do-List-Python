
from PyQt5 import QtCore, QtGui, QtWidgets


class InfoDialog(QtWidgets.QDialog):
    def __init__(self, text, text2):
        super().__init__()
        self.text = text
        self.text2 = text2
        self.resize(398, 278)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        
        self.label = QtWidgets.QLabel(self, text = self.text)
        
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self)      
        self.verticalLayout.addWidget(self.textBrowser)
        self.textBrowser.setText(self.text2)
        

