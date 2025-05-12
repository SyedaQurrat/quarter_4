


# from fastapi import FastAPI, Path, Query, Body
# from pydantic import BaseModel

# app = FastAPI()

# # Student model
# class Student(BaseModel):
#     name: str
#     roll_number: int
#     class_name: str
#     section: str

# # Dummy database
# students_db = {
#     101: {"name": "Ali", "roll_number": 101, "class_name": "10", "section": "A"},
#     102: {"name": "Sara", "roll_number": 102, "class_name": "9", "section": "B"}
# }

# # GET student by roll number (Path Parameter)
# @app.get("/students/{roll_number}")
# async def get_student(
#     roll_number: int = Path(..., ge=1, title="Roll Number")
# ):
#     student = students_db.get(roll_number)
#     if student:
#         return student
#     return {"error": "Student not found"}

# # GET all students (Query Parameters)
# @app.get("/students/")
# async def list_students(
#     class_name: str | None = Query(None, title="Class"),
#     section: str | None = Query(None, title="Section")
# ):
#     results = list(students_db.values())
#     if class_name:
#         results = [s for s in results if s["class_name"] == class_name]
#     if section:
#         results = [s for s in results if s["section"] == section]
#     return results

# # POST to add/update student (Body Parameter)
# @app.post("/students/")
# async def add_or_update_student(
#     student: Student = Body(...)
# ):
#     students_db[student.roll_number] = student.model_dump()
#     return {"message": "Student added/updated successfully", "data": student}










from fastapi import FastAPI, Path, Query, Body, Header, Cookie, Form, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# --- 1. Body model for student registration ---
class Student(BaseModel):
    name: str
    age: int
    student_class: str

# --- In-memory data storage ---
students_db = {}

# --- 1. Path Parameter: Get student by ID ---
@app.get("/students/{student_id}")
async def get_student(
    student_id: int = Path(..., ge=1, description="Student ID should be ≥ 1")
):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "data": student}


# --- 2. Query Parameter: Filter students ---
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


# --- 3. Body Parameter: Register student ---
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


# --- 4. Cookie Parameter: Remember language preference ---
@app.get("/students/langpref")
async def get_language_preference(
    lang: Optional[str] = Cookie(None)
):
    if lang:
        return {"message": f"Language preference is '{lang}'"}
    return {"message": "No language preference set in cookies"}


# --- 5. Form Parameters: Student feedback submission ---
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


# --- 6. File Upload: Student document upload ---
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
