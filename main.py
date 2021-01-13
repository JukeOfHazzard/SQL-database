import sqlite3
import SQL_basics as sql
import pandas as pd

from pathlib import Path

Path('spells.db').touch()

conn = sqlite3.connect('spells.db')
c = conn.cursor()
c.execute('''CREATE TABLE spells (id_index int PRIMARY KEY,
name text,
level int,
type text,
ritual bool,
casting_time text,
components text
duration text,
bard_access bool,
barbarian_access bool,
cleric_access bool,
druid_access bool,
figher_rogue_access bool,
monk_access bool,
paladin_access bool,
ranger_access bool,
sorcerer_access bool,
warlock_access bool,
wizard_access bool)''')

# load the data into a Pandas DataFrame
spell1 = pd.read_csv('Spells_Player.csv')
# write the data to a sqlite table
spell1.to_sql('spells', conn, if_exists='replace', index = False)

# load the data into a Pandas DataFrame
spell2 = pd.read_csv('Spells_Xanthar.csv')
# write the data to a sqlite table
spell2.to_sql('spellsX', conn, if_exists='replace', index = False)

#get connection from the database that exists.

connection = sqlite3.connect('spells.db')
cursor = connection.cursor()

'''put in the table_reader file'''
while True:
    print("1) Display ")
    print("2) Add ")
    print("3) Update ")
    print("4) Delete ")
    print("5) Query")
    print("6) Quit")
    choice = input("> ")

    #1 = Display
    if   choice == "1": sql.table_reader.display_db_contents()
    #2 = Add
    elif choice == "2": sql.table_reader.add()
    #3 = Update
    elif choice == "3": sql.table_reader.update()
    #4 = Delete
    elif choice == "4": sql.table_reader.delete()
    #5 = Query
    elif choice == "5": sql.table_reader.querey()
    #6 = Quit
    else: break
