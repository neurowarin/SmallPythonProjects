import sys
from interface import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.data)
        self.i = 0
        self.show()

    def data(self):
        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()+1)
        self.ui.tableWidget.setItem(self.i, 0, QTableWidgetItem(str(self.i+1)))
        self.ui.tableWidget.setItem(self.i, 1, QTableWidgetItem(self.ui.lineEdit.text()))
        self.ui.tableWidget.setItem(self.i, 2, QTableWidgetItem(self.ui.lineEdit_2.text()))
        self.ui.tableWidget.setItem(self.i, 3, QTableWidgetItem(self.ui.lineEdit_3.text()))
        self.ui.lcdNumber.display(self.i+1)
        self.i += 1

app = QApplication(sys.argv)
fm = form()
sys.exit(app.exec_())