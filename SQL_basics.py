"""
CSE 310 SQL Database Workshop
"""

import sqlite3



class table_reader():
    def __init__(self, filename: str, tablename: str):
        self.database = filename
        self.table = tablename

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        table_name = self.table

    def promptfiles(self):
        self.database = input()
        self.table = input()

    # display db contents
    def display_db_contents():
        cursor.execute(f"SELECT * FROM {table_name}")
        for record in cursor.fetchall():
            print(record)
        print()

    # add
    def add():
        """TESTING FOR NOW: only using name, level, casting_time and components, add other fields later"""
        name = input("Name: ")
        level = input("Level: ")
        casting_time = input("Casing time: ")
        components = input("Components: ")
        
        values = (name, level, casting_time, components)
        cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?)", values)
        connection.commit()

    # update
    def update():
        """TESTING FOR NOW: only using name, level, casting_time and components, add other fields later"""
        name = input("Name: ")
        level = input("Level: ")
        casting_time = input("Casing time: ")
        components = input("Components: ")
        
        values = (name, level, casting_time, components)
        # cursor.execute(f"UPDATE {table_name}") # TODO: FIX
        connection.commit()

    # delete
    def delete():
        name  = input("Name: ")
        values = (name,)
        cursor.execute(f"DELETE FROM {table_name} WHERE name = ?", values)
        connection.commit()


    # querey
    def querey():
        pass