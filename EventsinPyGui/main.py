import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt

class form(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Events")

        self.lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.sld)

        self.sld.valueChanged.connect(self.lcd.display)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = form()
    sys.exit(app.exec_())
