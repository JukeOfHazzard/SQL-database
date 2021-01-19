import sqlite3
import table_reader as TR
import pandas as pd


#TODO: make the lines of code that run the table reader file.
sheet_1 = TR.table_reader("spells", "Spells_Player.csv")

sheet_1.UI()