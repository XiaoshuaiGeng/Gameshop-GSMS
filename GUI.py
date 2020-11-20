import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QAbstractItemView

import DBController
import ErrorMessage
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
        self.pss.setSortingEnabled(True)
        # For test use only, print the current clicked item id
        # self.pss.itemClicked.connect(lambda: self.test_click(self.pss))

        self.checkboxgame = self.findChild(QtWidgets.QAbstractButton, 'checkBoxGame')

        self.addGameOndb = self.findChild(QtWidgets.QPushButton, 'add1')
        self.addGameOndb.clicked.connect(self.AddGameWindow)

        self.refreshList = self.findChild(QtWidgets.QPushButton, 'RefreshBtn')
        self.refreshList.clicked.connect(self.load_game_list)

        self.delete = self.findChild(QtWidgets.QPushButton, 'delete1')
        self.delete.clicked.connect(self.deleteGameById)

        self.edit = self.findChild(QtWidgets.QPushButton, 'Edit1')
        self.edit.clicked.connect(self.EditGameWin)

        # checkboxes in Game Tab
        self.GamePriceCheckBox = self.findChild(QtWidgets.QCheckBox, 'GamePriceCheckBox')
        self.GameReleaseDateCheckBox = self.findChild(QtWidgets.QCheckBox, 'GameReleaseDateCheckBox')

        self.GameStartPrice = self.findChild(QtWidgets.QLineEdit, 'GameStartPrice')
        self.GameEndPrice = self.findChild(QtWidgets.QLineEdit, 'GameEndPrice')

        self.GameStartDate = self.findChild(QtWidgets.QDateEdit, 'GameStartDate')
        self.GameEndDate = self.findChild(QtWidgets.QDateEdit, 'GameEndDate')

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
        self.DeveloperTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SearchDeveloper = self.findChild(QtWidgets.QPushButton, 'search1_5')  # Find the button
        self.SearchDeveloper.clicked.connect(self.searchdev)

        self.searchTextLine = self.findChild(QtWidgets.QLineEdit, 'searchBox1_5')

        self.RefreshDeveloper = self.findChild(QtWidgets.QPushButton, 'RefreshBtn_5')  # Find the button
        self.RefreshDeveloper.clicked.connect(self.list_developer_table)

        self.addDeveloper = self.findChild(QtWidgets.QPushButton, 'add1_4')  # Find the button
        self.addDeveloper.clicked.connect(self.add_developer_table)

        self.deleteDeveloper = self.findChild(QtWidgets.QPushButton, 'delete1_4')  # Find the button
        self.deleteDeveloper.clicked.connect(self.delete_developer)

        self.selfDeveloperTable = self.findChild(QtWidgets.QTableWidget, 'DeveloperGamesTable')

        self.selfDeveloperInput = self.findChild(QtWidgets.QLineEdit, 'DeveloperIDInput')

        self.checkDeveloper = self.findChild(QtWidgets.QPushButton, 'CheckPublishedGamesBtn')  # Find the button
        self.checkDeveloper.clicked.connect(self.list_selfdeveloper_table)

        # Store

        self.StoreTable = self.findChild(QtWidgets.QTableWidget, 't_3')
        # self.StoreTable = QtWidgets.QTableWidget(self.StoreTable)
        self.StoreTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.searchStoreLine = self.findChild(QtWidgets.QLineEdit, 'searchBox1_6')

        self.refreshStore = self.findChild(QtWidgets.QPushButton, 'RefreshBtn_6')  # Find the button
        self.refreshStore.clicked.connect(self.refresh_store_table)

        self.searchStore = self.findChild(QtWidgets.QPushButton, 'search1_6')  # Find the button
        self.searchStore.clicked.connect(self.search_store_table)

        self.addStore = self.findChild(QtWidgets.QPushButton, 'add1_6')  # Find the button
        self.addStore.clicked.connect(self.add_store_table)

        self.editStore = self.findChild(QtWidgets.QPushButton, 'Edit1_6')  # Find the button
        self.editStore.clicked.connect(self.edit_store_table)

        self.deleteStore = self.findChild(QtWidgets.QPushButton, 'delete1_6')  # Find the button
        self.deleteStore.clicked.connect(self.delete_store_table)

        self.searchStoreId = self.findChild(QtWidgets.QLineEdit, 'StoreIDInput')

        self.checkStoreId = self.findChild(QtWidgets.QPushButton, 'CheckStoreStatusBtn')  # Find the button
        self.checkStoreId.clicked.connect(self.check_store_status)

        self.totalGameCopy = self.findChild(QtWidgets.QLabel, 'TotalGameCopies')
        self.totalGames = self.findChild(QtWidgets.QLabel, 'TotalGames')

        # Set
        # self.StoreTable.setColumnCount(6)
        # self.pss.setColumnCount(6)
        # self.CustomerTable.setColumnCount(6)
        # self.DeveloperTable.setColumnCount(6)

        self.load_game_list()
        self.CustomerTableList()
        self.list_developer_table()
        self.list_store_table()

        # self.pss.setItem(1, 1, QtWidgets.QTableWidgetItem(str("123")))

        self.show()

    # def test_click(self,obj:QtWidgets.QTableWidget):
    #     print("ID: {0}".format(obj.item(obj.currentRow(), 0).text()))
    #     print("test Click ", obj.currentItem().isSelected())

    def check_store_status(self):
        num_of_copies = str(tabledata.num_of_copies(store_id=self.searchStoreId.text())[2])
        num_of_games = str(tabledata.num_of_games(store_id=self.searchStoreId.text())[2])
        # print(num_of_copies)
        # print(num_of_games)
        self.totalGameCopy.setText("Number of total game copies: " + num_of_copies)
        self.totalGames.setText("Number of total games: " + num_of_games)

    def list_selfdeveloper_table(self):
        store_id = self.selfDeveloperInput.text()
        if store_id.isnumeric():
            self.selfDeveloperTable.setRowCount(0)
            for row_number, row_data in enumerate(tabledata.list_developer_games(store_id)):
                self.selfDeveloperTable.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.selfDeveloperTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def delete_store_table(self):
        self.deleteStoreWin = delete_store()

    def edit_store_table(self):
        self.editStoreWin = edit_store()

    def add_store_table(self):
        self.addStoreWin = add_store()

    def search_store_table(self):
        store_id = self.searchStoreLine.text()
        if store_id.isnumeric():
            self.StoreTable.setRowCount(0)
            for row_number, row_data in enumerate(tabledata.search_store_by_id(store_id)):
                self.StoreTable.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.StoreTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def refresh_store_table(self):
        self.list_store_table()

    def list_store_table(self):
        self.StoreTable.setRowCount(0)
        for row_number, row_data in enumerate((tabledata.list_store())):
            self.StoreTable.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.StoreTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def delete_developer(self):
        self.deldev = delete_developer()

    def add_developer_table(self):
        self.addDeveloperWin = add_developer()

    def list_developer_table(self):
        self.DeveloperTable.setRowCount(0)
        for row_number, row_data in enumerate((tabledata.list_developer())):
            self.DeveloperTable.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.DeveloperTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def searchdev(self, id: str):
        self.DeveloperTable.setRowCount(0)
        id = self.searchTextLine.text()
        if id.isnumeric():
            for row_number, row_data in enumerate(tabledata.search_developer_by_id(id)):
                self.DeveloperTable.insertRow(row_number)
                print(row_data, row_number)
                for column_number, data in enumerate(row_data):
                    self.DeveloperTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

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
            # remove current row from Table Widget
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
            print(self.pss.item(self.pss.currentRow(), 0).text())

            # pass the id of current row item into SQL to delete item in db
            tabledata.delete_game(self.pss.item(self.pss.currentRow(), 0).text())

            # remove current row from Table Widget
            self.pss.removeRow(self.pss.currentRow())

    def CustomerTableList(self):
        self.CustomerTable.setRowCount(0)
        for row_number, row_data in enumerate(tabledata.list_customer()):
            self.CustomerTable.insertRow(row_number)
            print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.CustomerTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # :List Game Table
    def load_game_list(self):
        self.pss.setSortingEnabled(False)
        self.pss.setRowCount(0)
        for row_number, row_data in enumerate(tabledata.getTabledata()):
            self.pss.insertRow(row_number)
            # print(row_data, row_number)
            for column_number, data in enumerate(row_data):
                self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.pss.setSortingEnabled(True)

    def AddGameWindow(self):
        self.addGame = AddGameWin(self)
        self.addGame.show()
        # print(self.addGame.gameName.input.text())

    def searchGame(self):

        # get input from search bar
        keyword = self.input.text()
        # initialize values for parameters
        sort_filter = {'price': False, 'date': False}
        start_price = None
        end_price = None
        start_date = None
        end_date = None

        # if checkboxes are checked
        if self.GamePriceCheckBox.isChecked():
            if len(self.GameStartPrice.text()) > 0 and len(self.GameEndPrice.text()) > 0:
                sort_filter['price'] = True
                start_price = self.GameStartPrice.text()
                end_price = self.GameEndPrice.text()
            else:
                ErrorMessage.ErrorMessageBox()

        if self.GameReleaseDateCheckBox.isChecked():
            sort_filter['date'] = True
            start_date = self.GameStartDate.text()
            end_date = self.GameEndDate.text()

        if len(keyword) > 0:
            self.pss.setRowCount(0)
            if keyword.isnumeric():

                for row_number, row_data in enumerate((tabledata.select_game_by_id(keyword))):
                    self.pss.insertRow(row_number)
                    # print(row_data, row_number)
                    for column_number, data in enumerate(row_data):
                        self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                print((tabledata.select_game_by_name(keyword, filter=sort_filter,
                                                     start_price=start_price,
                                                     end_price=end_price,
                                                     start_date=start_date,
                                                     end_date=end_date)))
                for row_number, row_data in enumerate((tabledata.select_game_by_name(keyword, filter=sort_filter,
                                                                                     start_price=start_price,
                                                                                     end_price=end_price,
                                                                                     start_date=start_date,
                                                                                     end_date=end_date))):
                    self.pss.insertRow(row_number)
                    # print(row_data, row_number)
                    for column_number, data in enumerate(row_data):
                        self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.pss.setRowCount(0)
            if all(sort_filter.values()):
                for row_number, row_data in enumerate(
                        (tabledata.search_game_by_price_release_date(start_date=start_date,
                                                                     end_date=end_date,
                                                                     start_price=start_price,
                                                                     end_price=end_price))):
                    self.pss.insertRow(row_number)
                    # print(row_data, row_number)
                    for column_number, data in enumerate(row_data):
                        self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            elif sort_filter['price']:
                # print(tabledata.list_game_by_price(low=start_price, high=end_price))
                for row_number, row_data in enumerate((tabledata.list_game_by_price(low=start_price, high=end_price))):
                    self.pss.insertRow(row_number)
                    # print(row_data, row_number)
                    for column_number, data in enumerate(row_data):
                        self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            elif sort_filter['date']:
                print("go in")
                print(tabledata.list_game_by_date(start_date=start_date, end_date=end_date))
                for row_number, row_data in enumerate(
                        (tabledata.list_game_by_date(start_date=start_date, end_date=end_date))):
                    self.pss.insertRow(row_number)
                    # print(row_data, row_number)
                    for column_number, data in enumerate(row_data):
                        self.pss.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                pass


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
        self.rDate = self.findChild(QtWidgets.QAbstractSpinBox, 'r`eleaseDate')
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


class add_developer(QtWidgets.QWidget):
    def __init__(self):
        super(add_developer, self).__init__()

        uic.loadUi('addDeveloper.ui', self)

        self.show()

        self.developerName = self.findChild(QtWidgets.QLineEdit, 'devName')
        self.developerAdress = self.findChild(QtWidgets.QLineEdit, 'address')

        self.edit_btn = self.findChild(QtWidgets.QPushButton, 'Update')
        self.edit_btn.clicked.connect(self.addDev)

    def addDev(self):
        tabledata.add_developer(developer_name=self.developerName.text(), address=self.developerAdress.text())
        self.close()


class delete_developer(QtWidgets.QWidget):
    def __init__(self):
        super(delete_developer, self).__init__()

        uic.loadUi('deleteDeveloper.ui', self)

        self.show()

        self.developerId = self.findChild(QtWidgets.QLineEdit, 'del')

        self.delete_btn = self.findChild(QtWidgets.QPushButton, 'delBtn')
        self.delete_btn.clicked.connect(self.deleteDev)

    def deleteDev(self):
        tabledata.delete_developer(developer_id=self.developerId.text())
        self.close()


class add_store(QtWidgets.QWidget):
    def __init__(self):
        super(add_store, self).__init__()

        uic.loadUi('addStore.ui', self)

        self.show()

        self.storeName = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.storeAddress = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')

        self.add_btn = self.findChild(QtWidgets.QPushButton, 'Add')
        self.add_btn.clicked.connect(self.addStore)

    def addStore(self):
        tabledata.add_store(store_name=self.storeName.text(), address=self.storeAddress.text())
        self.close()


class edit_store(QtWidgets.QWidget):
    def __init__(self):
        super(edit_store, self).__init__()
        uic.loadUi('editStore.ui', self)
        self.show()

        self.storeId = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.storeName = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.storeAddress = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')

        self.edit_btn = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.edit_btn.clicked.connect(self.editStore)

    def editStore(self):
        tabledata.update_store(store_id=self.storeId.text(), store_name=self.storeName.text(),
                               address=self.storeAddress.text())
        self.close()


class delete_store(QtWidgets.QWidget):
    def __init__(self):
        super(delete_store, self).__init__()
        uic.loadUi('deleteStore.ui', self)
        self.show()

        self.storeId = self.findChild(QtWidgets.QLineEdit, 'lineEdit')

        self.delete_btn = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.delete_btn.clicked.connect(self.deleteStore)

    def deleteStore(self):
        tabledata.delete_store(store_id=self.storeId.text())
        self.close()


test = SQLExecutor(host="159.203.59.83", username="gamestop", password="Sn123456", database="gamestop")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
