import tkinter as tk
from tkinter.constants import *
import csv

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill=BOTH)
        self.create_widgets()
        self.mixstr()

    def mixstr(self):
        temp = self.entr.get()
        lst = next(csv.reader([temp], delimiter=' '), [])
        i = 1
        outlst = []
        for row in lst:
            if i % 2 != 0:
                row = row.upper()
                outlst.append(row)
            if i % 2 == 0:
                row = row[::-1]
                outlst.append(row)
            i += 1
        outstr = ' '.join(outlst)
        self.strlab.set(outstr)

    def create_widgets(self):
        self.out = []

        self.btn1 = tk.Button(self, text="mix phrase")
        self.btn1.pack()
        self.btn1.bind('<Button-1>', lambda e: self.mixstr())

        self.str = tk.StringVar(self, value='Michelle ma belle these are words that go together well')
        self.entr = tk.Entry(self, textvariable=self.str, width=50)
        self.entr.pack()

        self.strlab = tk.StringVar(self, value='result')
        self.lab1 = tk.Label(self, textvariable=self.strlab)
        self.lab1.pack()

if __name__ == '__main__':
    root = App()
    root.master.title('Window')
    root.master.geometry('400x70+500+500')
    root.mainloop()
