# models.py

from datetime import date

class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email

class Task:
    def __init__(self, task_id: int, title: str, description: str, status: str, due_date: date, user_id: int):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.user_id = user_id
