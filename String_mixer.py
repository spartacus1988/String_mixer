import tkinter as tk
from tkinter import Canvas as cnvs
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.title("Srting mixer")
    root.geometry("1024x120+300+300")
    root.resizable(False, False)
    canvas = cnvs(root, width = 1000, height = 110, bg = '#555')
    canvas.pack()
    app.pack
    app.mainloop()


