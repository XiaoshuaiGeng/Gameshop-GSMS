from PyQt5 import QtWidgets

# Used to show Error Messages
class ErrorMessageBox(QtWidgets.QMessageBox):
    def __init__(self):
        super(ErrorMessageBox, self).__init__()
        self.setWindowTitle("Warning")
        self.setIcon(QtWidgets.QMessageBox.Warning)
        self.setText("The lower bound & higher bound of the price need to be specified")
        # self.setGeometry(500,500,640,480)
        self.exec_()

