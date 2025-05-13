# schemas.py

from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
from typing import Optional, Annotated


# ---------- USER MODELS ----------

class UserCreate(BaseModel):
   username: Annotated[str, constr(min_length=3, max_length=20)]
   email: EmailStr


class UserRead(BaseModel):
    user_id: int
    username: str
    email: EmailStr


# ---------- TASK MODELS ----------

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
    due_date: date
    user_id: int

    @validator("due_date")
    def check_due_date(cls, v):
        from datetime import date
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v


class TaskRead(BaseModel):
    task_id: int
    title: str
    description: Optional[str] = None
    status: str
    due_date: date
    user_id: int
