import sqlite3
conn = sqlite3.connect('userDatabase.sqlite')
cursor = conn.cursor()
print("Opened database successfully")
for row in cursor.execute("SELECT courses, credits, prereqs, coreqs from courses"):
    if row[0].startswith('CGS'):
        print("Course = ", row[0], "Credits = ", row[1], "Prereqs = ", row[2], "Coreqs = ", row[3])
conn.commit()
conn.close()