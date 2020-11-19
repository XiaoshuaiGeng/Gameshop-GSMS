import sys
import PyQt5
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QAbstractItemView
import DBController
from DBController import SQLExecutor

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
        self.pss.setSelectionBehavior(QAbstractItemView.SelectRows)

        # For test use only, print the current clicked item id
        # self.pss.itemClicked.connect(lambda: self.test_click(self.pss))

        self.checkboxgame = self.findChild(QtWidgets.QAbstractButton, 'checkBoxGame')

        self.addGameOndb = self.findChild(QtWidgets.QPushButton, 'add1')
        self.addGameOndb.clicked.connect(self.AddGameWindow)

        self.refreshList = self.findChild(QtWidgets.QPushButton, 'RefreshBtn')
        self.refreshList.clicked.connect(self.RefreshListBtn)

        self.delete = self.findChild(QtWidgets.QPushButton, 'delete1')
        self.delete.clicked.connect(self.deleteGameById)

        self.edit = self.findChild(QtWidgets.QPushButton, 'Edit1')
        self.edit.clicked.connect(self.EditGameWin)

        # CustomerTable
        self.CustomerTable = self.findChild(QtWidgets.QTableWidget, 'tableGame2')
        # self.CustomerTable = QtWidgets.QTableWidget(self.CustomerTable)
        self.CustomerTable.setSelectionBehavior(QAbstractItemView.SelectRows)

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

        # Developer
        self.DeveloperTable = self.findChild(QtWidgets.QTableWidget, 'tableDeveloper')



        self.SearchDeveloper = self.findChild(QtWidgets.QPushButton, 'search2')  # Find the button
        self.SearchDeveloper.clicked.connect(self.searchdev)

        # Set
        self.pss.setColumnCount(6)
        self.CustomerTable.setColumnCount(6)
        self.DeveloperTable.setColumnCount(6)

        self.FirstTimeList()
        self.CustomerTableList()
        self.list_developer_table()

        # self.pss.setItem(1, 1, QtWidgets.QTableWidgetItem(str("123")))

        self.show()

    # def test_click(self,obj:QtWidgets.QTableWidget):
    #     print("ID: {0}".format(obj.item(obj.currentRow(), 0).text()))
    #     print("test Click ", obj.currentItem().isSelected())

    def list_developer_table(self):
        self.DeveloperTable.setRowCount(0)
        for row_number, row_data in enumerate((tabledata.list_developer())):
            self.DeveloperTable.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.DeveloperTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def searchdev(self):
        self.DeveloperTable.setRowCount(0)
        id = self.search2.text()
        if id.isnumeric():
            for row_number, row_data in enumerate((tabledata.list_developer())):
                self.CostomerTable.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.CostomerTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def editCustomer(self):
        self.eCustomer = editCustomer()

    def delCustomer(self):
        """
        Delete selected row from Customer Table

        Call SQLExecutor in the background to delete the item from DB
        :return:
        """
        # check if user selected item or not
        if len(self.CustomerTable.selectedItems()):
            print(self.CustomerTable.item(self.CustomerTable.currentRow(), 0).text())
            # pass the id of current row item into SQL to delete item in db
            tabledata.delete_customer(self.CustomerTable.item(self.CustomerTable.currentRow(), 0).text())
            #remove current row from Table Widget
            self.CustomerTable.removeRow(self.CustomerTable.currentRow())
        # self.delCustomer = deleteCustomer()

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

    def deleteGameById(self):
        """
        Delete current selected row from db & GUI
        :return:
        """
        # check if user selected item or not
        if len(self.pss.selectedItems()):
            print(self.pss.item(self.pss.currentRow(),0).text())

            # pass the id of current row item into SQL to delete item in db
            tabledata.delete_game(self.pss.item(self.pss.currentRow(), 0).text())

            #remove current row from Table Widget
            self.pss.removeRow(self.pss.currentRow())

    def CustomerTableList(self):
        self.CustomerTable.setRowCount(0)
        for row_number, row_data in enumerate(tabledata.list_customer()):
            self.CustomerTable.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.CustomerTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    # :List Game Table
    def FirstTimeList(self):

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
        self.addGame = AddGameWin(self)
        self.addGame.show()
        # print(self.addGame.gameName.input.text())

    def searchGame(self):
        self.pss.setRowCount(0)
        self.ListAll(self.input.text())



class AddGameWin(QtWidgets.QWidget):
    def __init__(self, parent_window: QtWidgets.QWidget):
        super(AddGameWin, self).__init__()
        self.parent_window = parent_window
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
        tabledata.add_game(game_name=self.gameName.text(), release_date=self.rDate.text(), genre=self.genre.text(),
                           platform=self.platForm.text(), price=self.price.text(), availability=self.aval.text())
        self.close()
        self.parent_window.FirstTimeList()

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

        self.gameId = self.findChild(QtWidgets.QLineEdit, 'gameId')
        self.gameName = self.findChild(QtWidgets.QLineEdit, 'gameName')
        self.rDate = self.findChild(QtWidgets.QAbstractSpinBox, 'releaseDate')
        self.genre = self.findChild(QtWidgets.QLineEdit, 'genre')
        self.platForm = self.findChild(QtWidgets.QLineEdit, 'platform')
        self.price = self.findChild(QtWidgets.QLineEdit, 'gamePrice')
        self.aval = self.findChild(QtWidgets.QLineEdit, 'aval')

    def updateToDB(self):
        tabledata.update_game(game_id=self.gameId.text(), game_name=self.gameName.text(),
                              release_date=self.rDate.text(), genre=self.genre.text(), platform=self.platForm.text(),
                              price=self.price.text(), availability=self.aval.text())
        self.close()

    def closeWin(self):
        self.close()

class adCustomer(QtWidgets.QWidget):
    def __init__(self):
        super(adCustomer, self).__init__()

        uic.loadUi('addCustomer.ui', self)

        self.show()

        self.address = self.findChild(QtWidgets.QLineEdit, 'Address')
        self.firstName = self.findChild(QtWidgets.QLineEdit, 'cFirstName')
        self.lastName = self.findChild(QtWidgets.QLineEdit, 'cLastName')

        self.add = self.findChild(QtWidgets.QPushButton, 'add_3')
        self.add.clicked.connect(self.addData)

        self.cancel = self.findChild(QtWidgets.QPushButton, 'cancel_3')
        self.cancel.clicked.connect(self.closeWin)

    def addData(self):
        tabledata.add_customer(fname=self.firstName.text(), lname=self.lastName.text(), address=self.address.text())

    def closeWin(self):
        self.close()


class editCustomer(QtWidgets.QWidget):
    def __init__(self):
        super(editCustomer, self).__init__()

        uic.loadUi('editCustomer.ui', self)

        self.show()

        self.Cusid = self.findChild(QtWidgets.QLineEdit, 'id')
        self.fName = self.findChild(QtWidgets.QLineEdit, 'fName')
        self.lName = self.findChild(QtWidgets.QLineEdit, 'lName')
        self.Address = self.findChild(QtWidgets.QLineEdit, 'address')

        self.edit_btn = self.findChild(QtWidgets.QPushButton, 'Edit')
        self.edit_btn.clicked.connect(self.editCus)

    def editCus(self):
        tabledata.update_customer(customer_id=self.Cusid.text(), fname=self.fName.text(), lname=self.lName.text(),
                                  address=self.Address.text())
        self.close()


test = SQLExecutor(host="159.203.59.83", username="gamestop", password="Sn123456", database="gamestop")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


