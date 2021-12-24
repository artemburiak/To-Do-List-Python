from PyQt5 import QtCore, QtGui, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, tsk, updater):
        super().__init__()
        self.updater = updater

        self.tasks = tsk
        self.resize(318, 141)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(self, text = 'Add Task')
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.verticalLayout.addWidget(self.lineEdit2)

        self.pushButton = QtWidgets.QPushButton(self, text = 'ADD')
        self.verticalLayout.addWidget(self.pushButton)
        self.addsignal()
        
    def addsignal(self):
        self.pushButton.clicked.connect(self.btnclick)

    def btnclick(self):
        text = self.lineEdit.text()
        text2 = self.lineEdit2.text()
        self.tasks.addtask(text, text2)
        self.updater()
        self.close()
    
