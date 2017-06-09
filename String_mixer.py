import tkinter as tk
from tkinter import Canvas as cnvs
from tkinter import Label as lbl
from tkinter import Button as btn
from tkinter import Entry as entr
from tkinter import StringVar as strvr


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

def readstr(entry):
    #username = str.get()
    #print(entry("textvariable"))
    #s = entry.get()
    print("dd")


    #label("text") = "ddd"
    #str.set("sdfgfdg")
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
    label = lbl(canvas, text="Input your phrase here")
    label.pack()

    entry = entr(canvas, textvariable=str).pack()
    #entry.insert(0, "a default value")
    #s = entry.get()
    str.set("a default value")
    s = str.get()

    print(s)

    button = btn(root, text="OK", command=readstr(entry)).pack(side="top")

    canvas.pack()
    app.pack
    app.mainloop()


