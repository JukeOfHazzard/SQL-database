"""
The file used to test an practice all things studdied out from sorces found on the internet.
The links to those found sources are in the README file.
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('spells.db')
c = conn.cursor()
conn.commit()

# load the data into a Pandas DataFrame
spell1 = pd.read_csv('Spells_Player.csv')
# write the data to a sqlite table
spell1.to_sql('spells', conn, if_exists='replace', index = False)

# get column names
c.execute("SELECT * FROM spells;")
row = list(c.description)
for collumn in row:
  convert = list(collumn)
  print(convert[0])
#   for top in convert:
#      print(top[0])
#print()


# display table
# c.execute("SELECT * FROM spells;")
# for line in c.fetchall():
#    print(line)
# print()

#for item in c.fetchall()
#    variable = input("")
#print()
#cursor.execute(f"INSERT INTO spells1 VALUES  WHERE values = (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
#connection.commit()


#data_search = input("What are you searching in a spell: ")
#variable = (input("What data are you expecting it to have: "))
#c.execute(f"SELECT * FROM spells1 WHERE {data_search} = {variable};")
#for line in c.fetchall():
#   print(line)
#print()