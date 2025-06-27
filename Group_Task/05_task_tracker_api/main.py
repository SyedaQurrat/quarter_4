# main.py

from fastapi import FastAPI, HTTPException
from schemas import UserCreate, UserRead, TaskCreate, TaskRead
from models import User, Task
from data import USERS, TASKS, USER_ID_COUNTER, TASK_ID_COUNTER

app = FastAPI()

# ---------------------------
# USER ROUTES
# ---------------------------

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global USER_ID_COUNTER
    new_user = User(user_id=USER_ID_COUNTER, username=user.username, email=user.email)
    USERS[USER_ID_COUNTER] = new_user
    USER_ID_COUNTER += 1
    return UserRead(user_id=new_user.user_id, username=new_user.username, email=new_user.email)


@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead(user_id=user.user_id, username=user.username, email=user.email)


# ---------------------------
# TASK ROUTES
# ---------------------------

@app.post("/tasks/", response_model=TaskRead)
def create_task(task: TaskCreate):
    global TASK_ID_COUNTER
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    new_task = Task(
        task_id=TASK_ID_COUNTER,
        title=task.title,
        description=task.description,
        status=task.status,
        due_date=task.due_date,
        user_id=task.user_id
    )
    TASKS[TASK_ID_COUNTER] = new_task
    TASK_ID_COUNTER += 1
    return TaskRead(**new_task.__dict__)


@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead(**task.__dict__)


@app.put("/tasks/{task_id}", response_model=TaskRead)
def update_task_status(task_id: int, status: str):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    allowed_statuses = ["pending", "in progress", "completed"]
    if status not in allowed_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    task.status = status
    return TaskRead(**task.__dict__)


@app.get("/users/{user_id}/tasks", response_model=list[TaskRead])
def list_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_tasks = [TaskRead(**task.__dict__) for task in TASKS.values() if task.user_id == user_id]
    return user_tasks
