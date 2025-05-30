from fastapi import FastAPI, Path, Query, Body, Header, Cookie, Form, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Body model for student registration ---
class Student(BaseModel):
    name: str
    age: int
    student_class: str

# In-memory data storage ---
students_db = {}

# 1. Path Parameter: Get student by ID ---
@app.get("/students/{student_id}")
async def get_student(
    student_id: int = Path(..., ge=1, description="Student ID should be ≥ 1")
):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "data": student}


#  2. Query Parameter: Filter students ---
@app.get("/students/")
async def filter_students(
    student_class: Optional[str] = Query(None),
    min_age: Optional[int] = Query(None, ge=1)
):
    results = []
    for sid, s in students_db.items():
        if student_class and s['student_class'] != student_class:
            continue
        if min_age and s['age'] < min_age:
            continue
        results.append({"id": sid, "student": s})
    return {"filtered_students": results}


# 3. Body Parameter: Register student ---
@app.post("/students/register")
async def register_student(
    student: Student = Body(..., description="Student registration data"),
    token: str = Header(..., description="Admin token")
):
    if token != "admin123":
        raise HTTPException(status_code=401, detail="Invalid admin token")
    new_id = len(students_db) + 1
    students_db[new_id] = student.dict()
    return {"msg": "Student registered", "student_id": new_id}


# 4. Cookie Parameter: Remember language preference ---
@app.get("/students/langpref")
async def get_language_preference(
    lang: Optional[str] = Cookie(None)
):
    if lang:
        return {"message": f"Language preference is '{lang}'"}
    return {"message": "No language preference set in cookies"}


# 5. Form Parameters: Student feedback submission ---
@app.post("/students/feedback")
async def submit_feedback(
    name: str = Form(...),
    comments: str = Form(...),
    rating: int = Form(..., ge=1, le=5)
):
    return {
        "feedback_from": name,
        "rating": rating,
        "comments": comments
    }


#  6. File Upload: Student document upload ---
@app.post("/students/upload-doc/")
async def upload_document(
    student_id: int = Query(...),
    file: UploadFile = File(...)
):
    content = await file.read()
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return {
        "filename": file.filename,
        "type": file.content_type,
        "size_bytes": len(content),
        "msg": f"Document received for student #{student_id}"
    }
