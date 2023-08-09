import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import random
import sys

class Stock:
    def __init__(self, price, percent_range):
        self.price = price
        self.percent_range = percent_range
    
    def change(self):
        change_range = float(self.price) * self.percent_range / 2.00
        new_value = round(random.uniform(self.price - change_range, self.price + change_range), 2)
        self.price = new_value

AAAA = Stock(1000, 0.04)

fig, ax = plt.subplots()
y = []

def animate(i):
    AAAA.change()
    y.append(AAAA.price)
    ax.clear()
    ax.plot(y)

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().grid(column=0,row=1)

        self.label = tkinter.Label(self,text="AAAA ticker price, currently: "+ str(AAAA.price))
        self.label.grid(column=0, row=0)
        label = self.label

        self.button = tkinter.Button(self, text="exit", command=sys.exit)
        self.button.grid(column=1, row=0)

        
        def loop():
            label.config(text=("AAAA ticker price, currently: "+ str(AAAA.price)))
            self.after(1000, loop)
        
        loop()
ani = FuncAnimation(fig, animate, interval=1000)

app = App()
app.mainloop()
