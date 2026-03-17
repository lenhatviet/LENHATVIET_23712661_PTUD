import sqlite3
import random

DB = "students.db"

conn = sqlite3.connect(DB)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id TEXT,
    name TEXT,
    birth_year INT,
    major TEXT,
    gpa REAL
)
""")

names = ["An","Binh","Cuong","Dung","Lan","Hoa"]
majors = ["IT","AI","SE","DS"]

for i in range(10):

    student_id = str(i)

    name = random.choice(names)

    birth = random.randint(1999,2004)

    major = random.choice(majors)

    gpa = round(random.random()*4,2)

    cur.execute(
        "INSERT INTO students VALUES(?,?,?,?,?)",
        (student_id,name,birth,major,gpa)
    )

conn.commit()
conn.close()

print("DONE")