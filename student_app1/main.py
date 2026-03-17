from pydantic import BaseModel

class Student(BaseModel):
    student_id:str
    name:str
    birth_year:int
    major:str
    gpa:float


@app.post("/add2")
def add2(s:Student):

    conn=sqlite3.connect(DB)
    cur=conn.cursor()

    cur.execute(
        "INSERT INTO students VALUES(?,?,?,?,?)",
        (s.student_id,s.name,s.birth_year,s.major,s.gpa)
    )

    conn.commit()
    conn.close()

    return {"ok":True}


@app.delete("/delete2/{sid}")
def delete2(sid:str):

    conn=sqlite3.connect(DB)
    cur=conn.cursor()

    cur.execute(
        "DELETE FROM students WHERE student_id=?",
        (sid,)
    )

    conn.commit()
    conn.close()

    return {"ok":True}