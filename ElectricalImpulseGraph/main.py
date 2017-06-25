from numpy import *
from tkinter import *
import matplotlib.pyplot as plt

class ButGraph:
    def __init__(self):
        global root
        self.but = Button(root,text="ShowGraph",width = 50, height = 5)
        self.but.bind("<Button-1>",self.graph)
        self.but.pack()
    def graph(self, event):
        x = linspace(0.0,5.0,100)
        y = cos(2*pi*x)*exp(-x)
        a = exp(-x)
        plt.plot(x,y,'r-')
        plt.plot(x,a,'g--')
        plt.xlabel('время(секунды)')
        plt.ylabel('напряжение(мВольт)')
        ttl = plt.title('cos(2Пx*e^(-x))')
        grid = plt.grid(True)
        plt.show()

root = Tk()
obj = ButGraph()
root.mainloop()
