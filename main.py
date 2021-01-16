import sqlite3
import table_reader as TR
import pandas as pd


conn1 = sqlite3.connect('spells.db')
c1 = conn1.cursor()

# load the data into a Pandas DataFrame
spell1 = pd.read_csv('Spells_Player.csv')
# write the data to a sqlite table
spell1.to_sql('spells', conn1, if_exists='replace', index = False)

Path('spellsX.db').touch()
conn2 = sqlite3.connect('spellsX.db')
c2 = conn2.cursor()
# load the data into a Pandas DataFrame
spell2 = pd.read_csv('Spells_Xanthar.csv')
# write the data to a sqlite table
spell2.to_sql('spellsX', conn2, if_exists='replace', index = False)
#======================
#======================
#======================
#======================
#======================
#get connection from the database that exists.

connection1 = sqlite3.connect('spells.db')
cursor1 = connection1.cursor()

connection2 = sqlite3.connect('spellsX.db')
cursor2 = connection1.cursor()

read1 = TR.table_reader("spells.db", "spells")
read2 = TR.table_reader("spellsX.db", "spellsX")