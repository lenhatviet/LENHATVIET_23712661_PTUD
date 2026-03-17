import sqlite3

conn = sqlite3.connect("students.db")

cur = conn.cursor()

cur.execute("SELECT * FROM students")

rows = cur.fetchall()

print(rows)

conn.close()