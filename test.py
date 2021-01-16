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
row = c.fetchone()
column_names = row
print(column_names)

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