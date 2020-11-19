from PyQt5 import QtWidgets, uic, QtGui, QtCore
from DBController import SQLExecutor
import sqlite3
import sys
import DBController

tabledata = DBController.SQLExecutor(host="159.203.59.83", username="gamestop", password="Sn123456",
                                     database="gamestop")
start = True
rowid = 0


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('a.ui', self)

        # GameTable
        self.button = self.findChild(QtWidgets.QPushButton, 'search1')  # Find the button
        self.button.clicked.connect(self.searchGame)

        self.input = self.findChild(QtWidgets.QLineEdit, 'searchBox1')

        self.pss = self.findChild(QtWidgets.QTableWidget, 'tableGame')
        self.pss.viewport().installEventFilter(self)

        self.checkboxgame = self.findChild(QtWidgets.QAbstractButton, 'checkBoxGame')

        self.addGameOndb = self.findChild(QtWidgets.QPushButton, 'add1')
        self.addGameOndb.clicked.connect(self.AddGameWindow)

        self.refreshList = self.findChild(QtWidgets.QPushButton, 'RefreshBtn')
        self.refreshList.clicked.connect(self.RefreshListBtn)

        self.delete = self.findChild(QtWidgets.QPushButton, 'delete1')
        self.delete.clicked.connect(self.deleteByUserid)

        self.edit = self.findChild(QtWidgets.QPushButton, 'Edit1')
        self.edit.clicked.connect(self.EditGameWin)

        # CustomerTable
        self.CostomerTable = self.findChild(QtWidgets.QTableWidget, 'tableGame2')
        self.CostomerTable.viewport().installEventFilter(self)

        self.SearchCustomer = self.findChild(QtWidgets.QPushButton, 'search2')  # Find the button
        self.SearchCustomer.clicked.connect(self.SearchCus)

        self.refreshCustomer = self.findChild(QtWidgets.QPushButton, 'RefreshBtn2')  # Find the button
        self.refreshCustomer.clicked.connect(self.CustomerTableList)

        self.addCos = self.findChild(QtWidgets.QPushButton, 'add2')  # Find the button
        self.addCos.clicked.connect(self.addCustomer)

        self.delCus = self.findChild(QtWidgets.QPushButton, 'delete2')  # Find the button
        self.delCus.clicked.connect(self.delCustomer)

        self.editCus = self.findChild(QtWidgets.QPushButton, 'Edit2')  # Find the button
        self.editCus.clicked.connect(self.editCustomer)

        self.search2 = self.findChild(QtWidgets.QLineEdit, 'searchBox2')

        #Set
        self.pss.setColumnCount(6)
        self.CostomerTable.setColumnCount(6)

        self.FirstTimeList()
        self.CustomerTableList()

        # self.pss.setItem(1, 1, QtWidgets.QTableWidgetItem(str("123")))

        self.show()

    def SearchDev(self):
        self.DeveloperTable.setRowCount(0)
        id = self.search2.text()
        if id.isnumeric():
            print(tabledata.list_developer_games())
            for row_number, row_data in enumerate((tabledata.check_customer_memberships(id),)):
                self.CostomerTable.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.CostomerTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def editCustomer(self):
        self.eCustomer = editCustomer()

    def delCustomer(self):
        self.delCustomer = deleteCustomer()

    def addCustomer(self):
        self.adCos = adCustomer()

    def SearchCus(self):
        self.CostomerTable.setRowCount(0)
        id = self.search2.text()
        if id.isnumeric():
            print(tabledata.check_customer_memberships(id))
            for row_number, row_data in enumerate((tabledata.check_customer_memberships(id),)):
                self.CostomerTable.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.CostomerTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        # else:
        #     for row_number, row_data in enumerate((tabledata.select_game_by_name(id))):
        #         self.pss.insertRow(row_number)
        #         print(row_data, row_number)
        #         for column_number, data in enumerate(row_data):
        #             self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def EditGameWin(self):
        self.editGame = EditGame()
        self.editGame.show()

    def deleteByUserid(self):

        global rowid
        print(rowid)
        print(self.pss.item(rowid, 0).text())
        tabledata.delete_game(game_id=self.pss.item(rowid, 0).text())
        self.FirstTimeList()

    def CustomerTableList(self):
        self.CostomerTable.setRowCount(0)
        for row_number, row_data in enumerate(tabledata.list_customer()):
            self.CostomerTable.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.CostomerTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def FirstTimeList(self):  # L:List Game Table
        self.pss.setRowCount(0)
        for row_number, row_data in enumerate(tabledata.getTabledata()):
            self.pss.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def ListAll(self, id: str):

        # var_name = self.dateEdit.date()
        # if self.checkboxgame.isChecked():
        #     for row_number, row_data in enumerate((tabledata.list_game_by_date())):
        #         self.pss.insertRow(row_number)
        #         print(row_data, row_number)
        #         for column_number, data in enumerate(row_data):
        #             self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

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

    def RefreshListBtn(self):
        self.FirstTimeList()

    def AddGameWindow(self):
        self.addGame = AddGameWin()
        self.addGame.show()
        # print(self.addGame.gameName.input.text())

    def searchGame(self):
        print(self.pss.item(1, 1).text())
        self.pss.setRowCount(0)
        self.ListAll(self.input.text())

    def eventFilter(self, source, event):
        if self.pss.selectedIndexes() is not []:

            if event.type() == QtCore.QEvent.MouseButtonPress:
                if event.button() == QtCore.Qt.LeftButton:
                    row = self.pss.currentRow()
                    col = self.pss.currentColumn()

                    # print(self.pss.item(row, 0).text())
                    # print(self.pss.item(row, 0).text())
                    if (row != -1):
                        self.returnGameTabRow(row)

        return QtCore.QObject.event(source, event)

    def returnGameTabRow(self, row):
        global rowid
        rowid = row
        print(row)


class AddGameWin(QtWidgets.QWidget):
    def __init__(self):
        super(AddGameWin, self).__init__()

        uic.loadUi('1.ui', self)

        self.show()

        self.add = self.findChild(QtWidgets.QPushButton, 'add')
        self.add.clicked.connect(self.addtoDB)

        self.dele = self.findChild(QtWidgets.QPushButton, 'cancel')
        self.dele.clicked.connect(self.closeWin)

        self.gameName = self.findChild(QtWidgets.QLineEdit, 'gameName')
        self.rDate = self.findChild(QtWidgets.QAbstractSpinBox, 'releaseDate')
        self.genre = self.findChild(QtWidgets.QLineEdit, 'genre')
        self.platForm = self.findChild(QtWidgets.QLineEdit, 'platform')
        self.price = self.findChild(QtWidgets.QLineEdit, 'gamePrice')
        self.aval = self.findChild(QtWidgets.QLineEdit, 'aval')

    def addtoDB(self):
        tabledata.add_game(game_name=self.gameName.text(), release_date=self.rDate.text(),genre=self.genre.text(),platform=self.platForm.text(),price=self.price.text(), availability=self.aval.text())
        self.close()

    def closeWin(self):
        self.close()


class EditGame(QtWidgets.QWidget):
    def __init__(self):
        super(EditGame, self).__init__()

        uic.loadUi('editGame.ui', self)

        self.show()

        self.add = self.findChild(QtWidgets.QPushButton, 'add')
        self.add.clicked.connect(self.updateToDB)

        self.dele = self.findChild(QtWidgets.QPushButton, 'cancel')
        self.dele.clicked.connect(self.closeWin)

        self.gameId = self.findChild(QtWidgets.QLineEdit,'gameId')
        self.gameName = self.findChild(QtWidgets.QLineEdit, 'gameName')
        self.rDate = self.findChild(QtWidgets.QAbstractSpinBox, 'releaseDate')
        self.genre = self.findChild(QtWidgets.QLineEdit, 'genre')
        self.platForm = self.findChild(QtWidgets.QLineEdit, 'platform')
        self.price = self.findChild(QtWidgets.QLineEdit, 'gamePrice')
        self.aval = self.findChild(QtWidgets.QLineEdit, 'aval')

    def updateToDB(self):
        tabledata.update_game(game_id=self.gameId.text(), game_name=self.gameName.text(), release_date=self.rDate.text(),genre=self.genre.text(),platform=self.platForm.text(),price=self.price.text(), availability=self.aval.text())
        self.close()

    def closeWin(self):
        self.close()


class adCustomer(QtWidgets.QWidget):
    def __init__(self):
        super(adCustomer, self).__init__()

        uic.loadUi('addCustomer.ui', self)

        self.show()

        self.address = self.findChild(QtWidgets.QLineEdit,'Address')
        self.firstName = self.findChild(QtWidgets.QLineEdit, 'cFirstName')
        self.lastName = self.findChild(QtWidgets.QLineEdit, 'cLastName')

        self.add = self.findChild(QtWidgets.QPushButton, 'add_3')
        self.add.clicked.connect(self.addData)

        self.cancel = self.findChild(QtWidgets.QPushButton, 'cancel_3')
        self.add.clicked.connect(self.closeWin)

    def addData(self):
        tabledata.add_customer(fname=self.firstName.text(), lname= self.lastName.text(), address= self.address.text())

    def closeWin(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


