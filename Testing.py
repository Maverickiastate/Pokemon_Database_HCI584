from gettext import install
from tkinter import *

import pip
from pandastable import Table

root = Tk()

frame = Frame(root)

frame.pack()

table = Table(frame)

table.show()

root.mainloop


