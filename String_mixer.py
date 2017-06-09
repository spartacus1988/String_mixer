import tkinter as tk
from tkinter import Canvas as cnvs
from tkinter import Label as lbl
from tkinter import Button as btn
from tkinter import Entry as entr
from tkinter import StringVar as strvr


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

def readstr():
    nop
    #intext = str.get()
    #label = lbl(canvas, text=intext).pack()

if __name__ == "__main__":
    root = tk.Tk()
    str = strvr()
    #str = "Input your phrase here"
    app = Main(root)
    root.title("Srting mixer")
    root.geometry("1024x220+300+300")
    #root.resizable(False, False)
    canvas = cnvs(root, width =1000, height=110, bg='#FFF')
    #canvas.pack()
    #label = lbl(canvas, text="Input your phrase here").pack()
    #button = btn(canvas, text = "OK", command = readstr, fg ='red', bg = 'blue' ).pack()

    entry = entr(canvas, textvariable=str).pack()

    button = btn(root, text="OK", command=readstr).pack(side="top")

    canvas.pack()
    app.pack
    app.mainloop()


