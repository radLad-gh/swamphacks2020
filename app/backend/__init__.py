import sqlite3


def addUser(userid, password, fullname):
    conn = sqlite3.connect('/home/mahan/Programming/swamphacks2020/app/backend/userDatabase.sqlite')
    cursor = conn.cursor()

    names = fullname.split(" ")

    sqlite_insert_query = """INSERT INTO users (userID, password, firstName, lastName) 
    VALUES ('{}','{}','{}','{}')""".format(userid, password, names[0], names[1])
    count = cursor.execute(sqlite_insert_query)
    conn.commit()
    cursor.close()

def getUser(userid):
    conn = sqlite3.connect('/home/mahan/Programming/swamphacks2020/app/backend/userDatabase.sqlite')
    cursor = conn.cursor()
