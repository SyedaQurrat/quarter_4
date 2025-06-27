# data.py

from models import User, Task

# In-memory storage
USERS: dict[int, User] = {}
TASKS: dict[int, Task] = {}

# Auto-increment IDs
USER_ID_COUNTER = 1
TASK_ID_COUNTER = 1
