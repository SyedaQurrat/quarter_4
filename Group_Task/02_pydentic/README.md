#  Pydantic Validation

This project demonstrates how to use **Pydantic** for real-time data validation in Python.

##  Files
- [`app.py`](./app.py): Basic Pydantic example with validation.
- [`fastapi_app.py`](./fastapi_app.py): Real-world FastAPI integration example.

---

## 🔧 Setup
```bash
pip install pydantic fastapi uvicorn
```

---

##  Run FastAPI App
```bash
uvicorn fastapi_app:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test API.
'''

# File: .gitignore

'''gitignore
__pycache__/
*.pyc
.env
*.log
'''

# File: LICENSE

'''text
MIT License

Copyright (c) 2025 Syeda Qurrat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
'''

# File: app.py

from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

# Valid data
valid_data = {"name": "Syeda", "email": "syeda@example.com", "age": 22}

# Invalid data
invalid_data = {"name": "Syeda", "email": "not-an-email", "age": "twenty"}

try:
    user = User(**valid_data)
    print("✅ Valid Input:", user)
except ValidationError as e:
    print(e)

try:
    user = User(**invalid_data)
except ValidationError as e:
    print("❌ Validation Error:")
    print(e.json())

# File: fastapi_app.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_available: bool

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item received", "item": item}
