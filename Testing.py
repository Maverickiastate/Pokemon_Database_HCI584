from tkinter import *
from pandastable import Table

root = Tk()

frame = Frame(root)

frame.pack()

table = Table(frame)

table.show()

root.mainloop
