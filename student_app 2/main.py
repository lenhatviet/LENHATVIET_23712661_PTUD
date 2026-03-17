from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse

import sqlite3
import csv


app = FastAPI()

DB = "students.db"


# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# model

class Student(BaseModel):

    student_id: str
    name: str
    birth_year: int
    major: str
    gpa: float
    class_id: str


# get all

@app.get("/students")
def get_students():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    conn.close()

    return rows


# add

@app.post("/add2")
def add2(s: Student):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students VALUES(?,?,?,?,?,?)",
        (s.student_id, s.name, s.birth_year, s.major, s.gpa, s.class_id)
    )

    conn.commit()
    conn.close()

    return {"ok": True}


# delete

@app.delete("/delete2/{sid}")
def delete2(sid: str):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM students WHERE student_id=?",
        (sid,)
    )

    conn.commit()
    conn.close()

    return {"ok": True}


# search

@app.get("/search/{name}")
def search(name: str):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ("%" + name + "%",)
    )

    rows = cur.fetchall()

    conn.close()

    return rows


# stats

@app.get("/stats")
def stats():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]

    cur.execute("SELECT AVG(gpa) FROM students")
    avg = cur.fetchone()[0]

    cur.execute(
        "SELECT major,COUNT(*) FROM students GROUP BY major"
    )

    major = cur.fetchall()

    conn.close()

    return {
        "total": total,
        "avg": avg,
        "major": major
    }


# export csv

@app.get("/export")
def export():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    file = "students.csv"

    with open(file, "w", newline="") as f:

        w = csv.writer(f)

        w.writerow(
            ["id", "name", "birth", "major", "gpa", "class"]
        )

        w.writerows(rows)

    conn.close()

    return FileResponse(file)