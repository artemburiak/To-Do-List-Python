# py -m PyQt5.uic.pyuic untitled.ui -o design.py

from PyQt5.QtWidgets import QApplication
from design import MainWindow
from task_container import Task_container

tsk = Task_container()

app = QApplication([])
win = MainWindow(tsk)


win.show()
app.exec()