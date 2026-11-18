from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# GET API

class User(BaseModel):
    name: str
    age: int
    userid: int


users = []
@app.get("/")
def home():
    return {
        "message": "Welcome to my API"
    }


# POST API
@app.post("/user")
def create_user(user : User):
    users.append(user)
    return {
        "message": "User created successfully",
        "name": user.name,
        "age": user.age,
        "userid": user.userid
    }


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.userid == user_id:
            users.remove(user)
            return {
                "message": f"User with id {user_id} deleted successfully"
            }
    return {
        "message": f"User with id {user_id} not found"
    }


@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user.userid == user_id:
            user.name = updated_user.name
            user.age = updated_user.age
            return {
                "message": f"User with id {user_id} updated successfully",
                "name": user.name,
                "age": user.age,
                "userid": user.userid
            }
    return {
        "message": f"User with id {user_id} not found"
    }