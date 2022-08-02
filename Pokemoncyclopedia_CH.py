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

            # please don't hardcode files!
            #data = pd.read_csv(r'c:\Users\franc\OneDrive\Documents\HCI584X\Pokemon_Database_HCI584\data.csv')
            data = pd.read_csv(r'data.csv')
            df = pd.DataFrame(data)
            self.table = pt = Table(f, dataframe=df, col=10,
                                    showtoolbar=True, showstatusbar=True)
            options = {'colheadercolor':'green','floatprecision': 5}
            config.apply_options(options, pt)
            
            pt.expandColumns(10) # make columns 10 chars(?) wide
            pt.show()
            return

app = TestApp()
#launch the app
app.mainloop()