import sqlite3
import SQL_basics as sql

connection = sqlite3.connect('mine.db')
cursor = connection.cursor()

while True:
    print("1) Display ")
    print("2) Add ")
    print("3) Update ")
    print("4) Delete ")
    print("5) Query")
    print("6) Quit")
    choice = input("> ")

    #1 = Display
    if   choice == "1": sql.display_db_contents()
    #2 = Add
    elif choice == "2": sql.add()
    #3 = Update
    elif choice == "3": sql.update()
    #4 = Delete
    elif choice == "4": sql.delete()
    #5 = Query
    elif choice == "5": sql.querey()
    #6 = Quit
    else: break
