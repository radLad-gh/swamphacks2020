import sqlite3

class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect("userDatabase.sqlite")
        self.cursor = self.conn.cursor()
        self.count = None

    def addUser(self, userID, password, fullname):
        conn = sqlite3.connect("userDatabase.sqlite")
        cursor = self.conn.cursor()
        count = None
        names = fullname.split(" ")
        
        sqlite_insert_query = """INSERT INTO users (userID, password, firstName, lastName) VALUES ({}, {}, {}, {})""".format(userID, password, names[0],names[1])
        self.cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()

def addUser(userID, password, fullname):
        conn = sqlite3.connect("userDatabase.sqlite")
        cursor = conn.cursor()
        count = None
        names = fullname.split(" ")
        
        sqlite_insert_query = """INSERT INTO users (userID, password, firstName, lastName) VALUES ({}, {}, {}, {})""".format(userID, password, names[0],names[1])
        cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()