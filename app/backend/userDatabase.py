#hi i'm michel
import sqlite3
conn = sqlite3.connect('backend/userDatabase.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
for row in cursor.execute("SELECT courses, credits from courses"):
    if row[0].startswith('CGS'):
        print("Course = ", row[0], "Credits = ", row[1])
conn.commit()
conn.close()

x = "name"

sqlite_insert_query = """INSERT INTO SqliteDb_developers
                      (courses, name, email, joining_date, salary) 
                       VALUES 
                      (1,  """ + x + """ ,'james@pynative.com','2019-03-17',8000)"""
conn = sqlite3.connect('userDatabase.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
for row in cursor.execute("SELECT courses, credits from courses"):
    if row[0].startswith('COP'):
        print("Course = ", row[0], "Credits = ", row[1])
conn.commit()
conn.close()
