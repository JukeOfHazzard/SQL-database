import sqlite3
import table_reader as TR
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

Path('spellsX.db').touch()
conn = sqlite3.connect('spellsX.db')
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
spell2 = pd.read_csv('Spells_Xanthar.csv')
# write the data to a sqlite table
spell2.to_sql('spellsX', conn, if_exists='replace', index = False)

#get connection from the database that exists.

connection1 = sqlite3.connect('spells.db')
cursor1 = connection1.cursor()

connection2 = sqlite3.connect('spellsX.db')
cursor2 = connection1.cursor()

read1 = TR.table_reader("spells.db", "spells")
read2 = TR.table_reader("spellsX.db", "spellsX")