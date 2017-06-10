# import tkinter as tk
# from tkinter import Canvas as cnvs
# from tkinter import Label as lbl
# from tkinter import Button as btn
# from tkinter import Entry as entr
# from tkinter import StringVar as strvr
#
#
#
# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#
# def buttonClick():
#     print('hello')
#
#     #def readstr():
#
#     #s = str.get()
#     #label = lbl(root, text=s)
#     #label.pack(side="bottom")
#     #print(entry.get())
#     #print("the text is", entry.get())
#     #entry
#
#
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     str = strvr()
#     str.set("Input your phrase here")
#     app = Main(root)
#     root.title("Srting mixer")
#     root.geometry("100x70+300+300")
#     canvas = cnvs(root, width =1000, height=110, bg='#FFF')
#     canvas.pack()
#     entry = entr(canvas, textvariable=str)
#     entry.grid()
#     #entry.pack()
#     #button = btn(root, text="change", command=readstr()).pack(side="top")
#     button = btn(root, command=buttonClick(), text="Submit")
#     button.pack()
#     canvas.pack()
#     app.pack()
#     app.mainloop()

import tkinter as tk
from tkinter.constants import *


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        self.out = []

        self.btn1 = tk.Button(self, text="change")
        self.btn1.pack()
        self.btn1.bind('<Button-1>', lambda e: self.out.append('btn1  click'))

        self.lab1 = tk.Label(self, text='test 1')
        self.lab1.pack()
        self.lab1.bind('<Button-1>', lambda e: self.out.append('label1 click'))
        self.lab2 = tk.Label(self, text='test 2')
        self.lab2.pack()
        self.lab2.bind('<Button-1>', lambda e: self.out.append('label2 click'))


        


if __name__ == '__main__':
    root = App()
    root.master.title('Window')
    root.master.geometry('300x70+500+500')
    root.mainloop()
    print(root.out)