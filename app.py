from fastapi import FastAPI

app = FastAPI()

# GET API
@app.get("/")
def home():
    return {
        "message": "Welcome to my API"
    }


# POST API
@app.post("/user")
def create_user(name: str, age: int):
    return {
        "message": "User created successfully",
        "name": name,
        "age": age
    }
