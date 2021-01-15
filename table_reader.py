"""
Table Reader module
Import this using python to get access to helper methods for reading database.db files
Authors: Elijah Harrison and Eli Jukes
"""

import sqlite3

class table_reader:
    """import this module to access tables within database"""
    def __init__(self, database_filename: str, table_name: str):
        self.database   = database_filename
        self.table      = table_name

        self.connection = sqlite3.connect(database_filename)
        self.cursor     = self.connection.cursor()

        # set self.connection and self.cursor
        self.table_init()
        

    """ HELPER METHODS """
    def load_csv(self):
        # TODO: transfer from main.py after Eli has edited this
        pass

    def table_init(self):
        """  """
        table_headers = "name" # TODO: construct table_header in ui methods below
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table} (id integer PRIMARY KEY, {table_headers})")

    # read
    def read(self):
        """ display all table contents """
        # TODO: get this to work
        self.cursor.execute(f"SELECT * FROM {self.table}")
        for record in self.cursor.fetchall(): print(record)
        print()

    def add_column(self, column_name: str, data_type: str):
        """ add column """
        self.cursor.execute(f"ALTER TABLE {self.table} ADD {column_name} {data_type}")


    # TODO: Eli Jukes
    # append
    def add_row(self):
        s_name = input("Name the spell: ")
        level = input("What level does this spell need to be cast at?") 
        s_type = input("What scchool type of spell is it.") 
        ritual = bool(input("Is this a ritual spell [True/False]"))
        casting_time = input("How long does it take to cast the spell?") 
        components = input("Which componets does it use [V, S, M]")
        duration = input("What is the duration of the spell? ") 
        bard  = bool(input("Can this spell be used by Bards [True/False]"))
        barbarian = bool(input("Can this spell be used by Barbarians [True/False]"))
        cleric = bool(input("Can this spell be used by Clerics [True/False]"))
        druid = bool(input("Can this spell be used by Druids [True/False]"))
        figher_rogue  = bool(input("Can this spell be used by Fighters or Rogues [True/False]"))
        monk  = bool(input("Can this spell be used by Monks [True/False]"))
        paladin   = bool(input("Can this spell be used by Paladins [True/False]"))
        ranger = bool(input("Can this spell be used by Rangers [True/False]"))
        sorcerer  = bool(input("Can this spell be used by Sorcerers [True/False]"))
        warlock   = bool(input("Can this spell be used by Warlocks [True/False]"))
        wizard = bool(input("Can this spell be used by Wizards [True/False]"))
        values = (s_name, level, s_type, ritual, casting_time, components, duration, bard, barbarian, cleric, druid,
                figher_rogue, monk, paladin, ranger, sorcerer, warlock, wizard)
        self.cursor.execute(f"INSERT INTO {self.table} VALUES  WHERE values = (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
        self.connection.commit()

    # delete
    def delete(self):
        """ delete one row from the table in the database """
        name = input("Spell Name: ")
        values = (name,)
        self.cursor.execute(f"DELETE FROM {self.table} WHERE name = ?", values)
        self.connection.commit()

    # update
    def update(self):
        #TODO: figure out how t display all the types of different data collumns there are and let the user pick.
        # use the table_maker file to read the database and then print off the collumn names.
        # Do to also get lines 48 - 65 also in there   
        variable = input("which part of the spell are you trying to update:")
        value = input("What do you want it to be set to?")
        self.cursor.execute(f"UPDATE {self.table} SET {variable} WHERE value = (?)", value)
        self.connection.commit()
    # sort
    def search(self):
        variable = input("What type of spell are you looking for? ")
        value = input("What do you want it to be set to? ")
        self.cursor.execute(f"UPDATE {self.table} SET {variable} WHERE value = (?)", value)
        self.connection.commit()
        
    #display
    def display(self):
        self.cursor.execute(f"SELECT * FROM {self.table}")
        self.connection.commit()

    """ inner join """
    # parameter: new table
    # merge self table and new table
    # return: combined table

    """ USER INTERFACE METHODS """
    # TODO: define user interaction methods which call above helper methods
    def UI(self):
        while True:
            print("1) Display ")
            print("2) Add ")
            print("3) Update ")
            print("4) Delete ")
            print("5) Query")
            print("6) Quit")
            choice = input("> ")

            #1 = Display
            if   choice == "1": self.display()
            #2 = Add
            elif choice == "2": self.add_row()
            #3 = Update
            elif choice == "3": self.update()
            #4 = Delete
            elif choice == "4": self.delete()
            #5 = Query
            elif choice == "5": self.search()
            #6 = Quit
            else: break


# example of main module
# data is in excel file, exported to two .csv files
spells1 = table_reader("spells1.db", "spells")
# in table_reader object, import .csv data into .db file under table name spells
spells2 = table_reader("spells2.db", "spells")
# in table_reader object, import .csv data into .db file under table name spells
