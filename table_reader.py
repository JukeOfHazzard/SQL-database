"""
Table Reader module
Import this using python to get access to helper methods for reading database.db files
Authors: Elijah Harrison and Eli Jukes
"""

import sqlite3
import pandas as pd

class table_reader:
    """ HELPER METHODS: To make this into a class to work with easier. """
    """import this module to access tables within database"""
    def __init__(self, database_filename: str, table_name: str):
        self.database   = database_filename
        self.table      = table_name

        self.connection = sqlite3.connect(database_filename + ".db")
        self.cursor     = self.connection.cursor()

        #acctually make it into a database
        self.load_csv()
    
    
    def load_csv(self):
        # load the data into a Pandas DataFrame
        spell1 = pd.read_csv(self.table)
        # write the data to a sqlite table
        spell1.to_sql(self.database, self.connection, if_exists='replace', index = False)

    """ Base Functions to do for the module"""
    #Eli Jukes
    #display
    def display(self):
        """ Will show all the information in the database. """
        self.cursor.execute(f"SELECT * FROM {self.database}")
        for line in self.cursor.fetchall():
            print(line)
            # for part in line:
            #     print(part)
        print()

    # append
    def add_row(self):
        """ This will ask the user to for information to fill in as many columns that it counts in the 
        database. Then it will add all that information in a new row into the database. """
        values = []
        self.cursor.execute(f"SELECT * FROM {self.database};")
        row = list(self.cursor.description) #Will look at the tables and get info from reach column 
        for column in row: 
            convert = list(column)
            data = input(f"Spell {convert[0]}: ")
            values.append(data)
        convert = tuple(values)
        self.cursor.execute(f"SELECT columns FROM {self.database}")
        q_marks = "?"
        how_many_columns = len(values)
        for i in range(how_many_columns - 1): #makes sure that the tuple of ?'s the exact measure as the input list 
            q_marks += ",?"
        self.cursor.execute(f"INSERT INTO {self.database} VALUES  WHERE values = ({q_marks})", convert)
        self.connection.commit()

    # update
    def update(self):
        """Displays all the types of different data collumns there are and let the user pick.
        Then will ask the user what they want to replace."""

        self.cursor.execute(f"SELECT * FROM {self.database};")
        row = list(self.cursor.description) #Will look at the tables and get info from reach column 
        for column in row: 
            convert = list(column)
            print(convert[0]) 
        variable = input("which part of the spell, shown above, are you trying to update:")
        value = input("What do you want it to be set to?")

        #TODO: figure out how to only update one row, because this looks like this updates the tabel
        #may have to do with the variables I am using.
        self.cursor.execute(f"UPDATE {self.database} SET {variable} WHERE value = (?)", value)
        self.connection.commit()

    # delete
    def delete(self):
        """ delete one row from the table in the database """

        name = input("Spell Name: ")
        values = (name,)
        self.cursor.execute(f"DELETE FROM {self.database} WHERE name = ?", values)
        self.connection.commit()
        
    """ Stretch Challenges"""  
    # sort
    def search(self):
        """ Allows the user to sort through the file data by what is expected 
        in the column they are looking at."""

        data_search = input("What are you searching in a spell: ")
        variable = (input("What data are you expecting it to have: "))
        self.cursor.execute(f"SELECT * FROM {self.database} WHERE {data_search} = {variable};")
        for line in self.cursor.fetchall():
            print(line)
        print()

    """ inner join """
    def inner_join(self):
        new_database = input("What do you want to call you new database file? ")
        file_source = input("What is the csv file that you are extracting the data from?")
        table_2 = table_reader(new_database, file_source)
        self.cursor.execute(f"SELECT * FROM {self.database} ORDER BY column DESC LIMIT 1;")
        last_entry = list(self.cursor.fetchone())
        
        #TODO: join the second table with the first one so you can view them.
        self.cursor.execute(f"SELECT * FROM {self.database} INNER JOIN {table_2.database} ON {self.database}.Name = {table_2.database}.Name WHERE Name = {last_entry[0]};")
    # merge self table and new table
    # return: combined table

    """ USER INTERFACE METHODS """
    def UI(self):
        """
        Defines user interaction methods which call above helper methods.
        Lets the user loop through untill they get all the needed information
        from the data; calls the neccessary functions to reach that
        information.
        """
        while True:
            print("1) Display ")
            print("2) Add ")
            print("3) Update ")
            print("4) Delete ")
            print("5) Search")
            print("6) Merge in another table.")
            print("7) Quit")
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
            #6 = inner join
            elif choice == "6": self.inner_join() 
            #7 =Quit
            else: break
    
    """ EXTRA STUFF: things for later use"""
    def table_init(self):
        """  """
        table_headers = "name" # TODO: construct table_header in ui methods below
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table} (id integer PRIMARY KEY, {table_headers})")

    def add_column(self, column_name: str, data_type: str):
        """ add column """
        self.cursor.execute(f"ALTER TABLE {self.table} ADD {column_name} {data_type}")