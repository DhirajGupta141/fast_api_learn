
from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getUsers/{user_id}")
def read_user(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}

@app.post("/createUser")
def create_user(name: str, age: int):
    return {"name": name, "age": age}























