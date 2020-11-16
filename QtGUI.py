from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,500,1280,720)
    win.setWindowTitle("Test Window")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50, 50)

    btn = QtWidgets.QPushButton(win)
    btn.setText("Text")

    win.show()
    sys.exit(app.exec_())


window()
