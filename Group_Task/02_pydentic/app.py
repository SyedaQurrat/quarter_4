from pydantic import BaseModel, EmailStr, ValidationError

# Define a model class
class User(BaseModel):
    name: str
    email: EmailStr
    age: int

# Sample valid input
data_valid = {
    "name": "Syeda",
    "email": "syeda@example.com",
    "age": 22
}

# Sample invalid input
data_invalid = {
    "name": "Syeda",
    "email": "not-an-email",
    "age": "twenty"
}

# Valid data parsing
try:
    user = User(**data_valid)
    print("Valid Input:", user)
except ValidationError as e:
    print(" Validation Error:", e)

# Invalid data parsing
try:
    user = User(**data_invalid)
except ValidationError as e:
    print(" Validation Error on Invalid Data:")
    print(e.json())