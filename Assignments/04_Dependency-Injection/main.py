from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app : FastAPI = FastAPI()

# 1. Simple Dependency
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}
    
@app.get("/get-simple-goal")
def simple_goal(response :  Annotated[dict, Depends(get_simple_goal)]):
    return response


# 2. Dependency with Parameters
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}
    
@app.get("/get-goal")
def get_my_goal(response :  Annotated[dict, Depends(get_goal)]):
    return response


# 3. Dependency with Query Parameters
def dep_login(username : str = Query(None), password : str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message" : "Login Successful"}
    else:
        return {"message" : "Login Failed"}
    
@app.get("/signin")
def login_api(user :  Annotated[dict,Depends(dep_login)]):
    return user

# 4. Multiple Dependencies
def depfunc1(num:int): 
    num = int(num)
    num += 1
    return num

def depfunc2(num): 
    num = int(num)
    num += 2
    return num

@app.get("/main/{num}")
def get_main(num: int, num1:  Annotated[int,Depends(depfunc1)], num2: Annotated[int,Depends(depfunc2)]):
    # Assuming you want to use num1 and num2 in some way
    #       1      2      3
    total = num + num1 + num2
    return f"Pakistan {total}"


blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

class GetObjectOr404():
    def __init__(self, model)->None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

user_dependency = GetObjectOr404(users)

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name



#----------just for self ------------

# from fastapi import FastAPI, Depends, Header, HTTPException
# from typing import Annotated
# from pydantic import BaseModel, Field

# app = FastAPI()

# # goal-1: Dependency function
# # def get_goal():
# #     return {"goal": "We are building AI Agents Workforce"}


# # goal-2: Dependency function with a parameter
# # def get_goal(username: str):
# #     return {
# #         "goal": "We are building AI Agents Workforce",
# #         "username": username
# #     }


# # goal-3:

# #  Step 1: Pydantic model with username as string and password as int
# class LoginModel(BaseModel):
#     username: str = Field(..., min_length=5, description="Enter your username")
#     password: int = Field(..., ge=5, description="Enter your numeric password")  # at least 5 digits

# #  Step 2: Dependency (no check, just return success if valid)
# def get_goal(credentials: LoginModel):
#     return {
#         "message": "Login accepted",
#         "username": credentials.username,
#         "password": credentials.password
#     }

# # Route where the dependency is injected
# # @app.get("/get-goal")
# @app.post("/get-goal")
# def simple_goal(response: Annotated[dict, Depends(get_goal)]):
#     return response
    


# def verify_token(x_token: str = Header(...)):
#     if x_token != "mysecret":
#         raise HTTPException(status_code=400, detail="Invalid X-Token header")
#     return x_token

# @app.get("/items/")
# def read_items(token: str = Depends(verify_token)):
#     return {"token": token}