import sqlite3
import random

DB = "students.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()


# table class

cur.execute("""
CREATE TABLE IF NOT EXISTS class(
    class_id TEXT,
    class_name TEXT,
    advisor TEXT
)
""")


# table students

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id TEXT,
    name TEXT,
    birth_year INT,
    major TEXT,
    gpa REAL,
    class_id TEXT
)
""")


# insert class

classes = [
    ("C1","SE1","Mr A"),
    ("C2","SE2","Mr B"),
    ("C3","AI1","Mr C")
]

cur.execute("DELETE FROM class")

for c in classes:
    cur.execute(
        "INSERT INTO class VALUES(?,?,?)", c
    )


names = ["An","Binh","Cuong","Dung","Lan","Hoa"]
majors = ["IT","AI","SE"]

cur.execute("DELETE FROM students")

for i in range(20):

    sid = str(i)

    name = random.choice(names)

    birth = random.randint(1999,2004)

    major = random.choice(majors)

    gpa = round(random.random()*4,2)

    cid = random.choice(["C1","C2","C3"])

    cur.execute(
        "INSERT INTO students VALUES(?,?,?,?,?,?)",
        (sid,name,birth,major,gpa,cid)
    )

conn.commit()
conn.close()

print("DONE")