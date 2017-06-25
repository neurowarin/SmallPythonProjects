import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.question)
        self.show()

    def lorenz(self,x, y, z, r, s=10, b=2.667):
        x_dot = s * (y - x)
        y_dot = r * x - y - x * z
        z_dot = x * y - b * z
        return x_dot, y_dot, z_dot

    def drawGraph(self, n):
        dt = 0.01
        stepCnt = 10000

        xs = np.empty((stepCnt + 1,))
        ys = np.empty((stepCnt + 1,))
        zs = np.empty((stepCnt + 1,))

        xs[0], ys[0], zs[0] = (0., 1., 1.05)

        for i in range(stepCnt):
            x_dot, y_dot, z_dot = self.lorenz(xs[i], ys[i], zs[i], n)
            xs[i + 1] = xs[i] + (x_dot * dt)
            ys[i + 1] = ys[i] + (y_dot * dt)
            zs[i + 1] = zs[i] + (z_dot * dt)

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot(xs, ys, zs, lw=0.5)
        ax.set_xlabel("Ось X")
        ax.set_ylabel("Ось Y")
        ax.set_zlabel("Ось Z")
        ax.set_title("Аттрактор Лоренца")

        plt.show()

    def question(self):
        if (not self.ui.radioButton.isChecked() and not self.ui.radioButton_2.isChecked() and not self.ui.radioButton_3.isChecked()
        and not self.ui.radioButton_4.isChecked() and not self.ui.radioButton_5.isChecked()
        and not self.ui.radioButton_6.isChecked() and not self.ui.radioButton_7.isChecked()):
            QMessageBox.question(self,'Error',"Please select a condition", QMessageBox.Ok)
            self.show()
        if self.ui.radioButton.isChecked():
                self.drawGraph(0.3)
        if self.ui.radioButton_2.isChecked():
                self.drawGraph(1.8)
        if self.ui.radioButton_3.isChecked():
                self.drawGraph(3.7)
        if self.ui.radioButton_4.isChecked():
                self.drawGraph(10)
        if self.ui.radioButton_5.isChecked():
                self.drawGraph(16)
        if self.ui.radioButton_6.isChecked():
                self.drawGraph(24.06)
        if self.ui.radioButton_7.isChecked():
                self.drawGraph(28)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = form()
    sys.exit(app.exec_())