# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for student data
class Student(BaseModel):
    name: str
    roll_number: int

# In-memory storage for students
students = {}

# Create multiple students
@app.post("/students/")
def create_students(student_list: List[Student]):
    added_students = []
    for student in student_list:
        if student.roll_number in students:
            raise HTTPException(status_code=400, detail=f"Student with roll number {student.roll_number} already exists.")
        students[student.roll_number] = student
        added_students.append(student)
    return {"message": "Students added successfully.", "students": added_students}

# Read a specific student by roll number
@app.get("/students/{roll_number}")
def read_student(roll_number: int):
    if roll_number not in students:
        raise HTTPException(status_code=404, detail="Student not found.")
    return students[roll_number]

# Read all students
@app.get("/students/")
def read_all_students():
    return list(students.values())

# Update a student's info
@app.put("/students/{roll_number}")
def update_student(roll_number: int, student: Student):
    if roll_number not in students:
        raise HTTPException(status_code=404, detail="Student not found.")
    students[roll_number] = student
    return {"message": "Student updated successfully.", "student": student}

# Delete a student
@app.delete("/students/{roll_number}")
def delete_student(roll_number: int):
    if roll_number not in students:
        raise HTTPException(status_code=404, detail="Student not found.")
    deleted_student = students.pop(roll_number)
    return {"message": "Student deleted successfully.", "student": deleted_student}