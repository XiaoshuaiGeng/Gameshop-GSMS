from PyQt5 import QtWidgets, uic, QtGui, QtCore
from DBController import SQLExecutor
import sqlite3
import sys
import DBController

tabledata = DBController.SQLExecutor(host="159.203.59.83", username="gamestop", password="Sn123456",
                                     database="gamestop")
start = True

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('a.ui', self)




        self.button = self.findChild(QtWidgets.QPushButton, 'search1') # Find the button
        self.button.clicked.connect(self.searchGame)

        self.input = self.findChild(QtWidgets.QLineEdit, 'searchBox1')
        self.pss = self.findChild(QtWidgets.QTableWidget, 'tableGame')
        self.checkboxgame = self.findChild(QtWidgets.QAbstractButton, 'checkBoxGame')

        self.pss.setColumnCount(6)

        self.FirstTimeList()

        #self.pss.setItem(1, 1, QtWidgets.QTableWidgetItem(str("123")))

        self.show()

    def FirstTimeList(self):
        for row_number, row_data in enumerate(tabledata.getTabledata()):
            self.pss.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        start = False

    def ListAll(self, id:str):

        #var_name = self.dateEdit.date()
        if self.checkboxgame.isChecked():
            for row_number, row_data in enumerate((tabledata.list_game_by_date())):
                self.pss.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        if id.isnumeric():
            for row_number, row_data in enumerate((tabledata.select_game_by_id(id))):
                self.pss.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            for row_number, row_data in enumerate((tabledata.select_game_by_name(id))):
                self.pss.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))





    def searchGame(self):
        self.pss.setRowCount(0)
        self.ListAll(self.input.text())

        
test = SQLExecutor(host="159.203.59.83",username="gamestop",password="Sn123456",database="gamestop")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


