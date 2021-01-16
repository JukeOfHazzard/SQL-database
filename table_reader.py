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
        values = []
        column_names = ["Name,Level,Type,Ritual,Casting Time,Range,Components,Duration,Bard,Barbarian,Cleric,Druid,Fighter/Rogue,Monk,Paladin,Ranger,Sorcerer,Warlock,Wizard"]
        for i in column_names:
            data = input(f"Spell {i}: ")
            values.append(data)
        convert = tuple(values)
        self.cursor.execute(f"SELECT columns FROM {self.table}")
        self.cursor.execute(f"INSERT INTO {self.table} VALUES  WHERE values = (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", convert)
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
        data_search = input("What are you searching in a spell: ")
        variable = (input("What data are you expecting it to have: "))
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE {data_search} = {variable};")
        for line in self.cursor.fetchall():
            print(line)
        print()

        
    #display
    def display(self):
        self.cursor.execute(f"SELECT * FROM {self.table}")
        for line in self.cursor.fetchall():
            for part in line:
                print(part)
            print()
        print()

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
