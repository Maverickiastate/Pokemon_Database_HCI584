from tkinter import *
import pandas as pd
from pandastable import Table, TableModel, config


class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('PokemonCyclonepedia')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            data = pd.read_csv(r'c:\Users\franc\OneDrive\Documents\HCI584X\Pokemon_Database_HCI584\data.csv')
            df = pd.DataFrame(data)
            self.table = pt = Table(f, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            pt.show()
                        #set some options
            options = {'colheadercolor':'green','floatprecision': 5}
            config.apply_options(options, pt)
            pt.show()
            return

app = TestApp()
#launch the app
app.mainloop()