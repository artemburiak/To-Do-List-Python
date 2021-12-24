from PyQt5 import QtCore, QtGui, QtWidgets
from design_2 import Dialog
from infodialog import InfoDialog

class MainWindow(QtWidgets.QWidget):
    def __init__(self, tsk):
        super().__init__()

        self.tasks_container = tsk
        self.resize(574, 461)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.tasks = QtWidgets.QListWidget(self)
        self.verticalLayout.addWidget(self.tasks)
        self.addbtn = QtWidgets.QPushButton(self, text = 'ADD')
        self.verticalLayout.addWidget(self.addbtn)
        self.updateList()
        self.addsignals()

        self.tasks.installEventFilter(self)


    def addsignals(self):
        self.addbtn.clicked.connect(self.opendialog)
        self.tasks.itemDoubleClicked.connect(self.taskinfo)

    def opendialog(self):
        self.dialog = Dialog(self.tasks_container, self.updateList)
        self.dialog.exec()

    def updateList(self):
        self.tasks.clear()
        t = self.tasks_container.gettasks()
        # self.tasks.addItems(t)
        for i in t:
            itm = QtWidgets.QListWidgetItem(i['text'])
            itm.setData(1, i['text2'])
            self.tasks.addItem(itm)

    def taskinfo(self, e):
        print(e.text())
        i = InfoDialog(e.text(), e.data(1))
        i.exec()

    def closeEvent(self, e):
        self.tasks_container.save()

    def eventFilter(self, s, e):
        def delete():
            self.tasks_container.deltask(t2 , t1)
            self.updateList()
        if e.type() == QtCore.QEvent.ContextMenu:
            print(e.globalPos())
            el = self.tasks.itemAt(e.x(), e.y())
            if el != None:
                t1 = el.data(1)
                t2 = el.text()
                m = QtWidgets.QMenu()
                m.move(e.globalPos())
                m.addAction('Delete').triggered.connect(delete)
                m.exec()



        return super().eventFilter(s, e)
        


        

    
