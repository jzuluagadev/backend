from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # comando para iniciar el server de fastApi en la  terminal "python -m uvicorn users:app --reload"

#class users
class Users(BaseModel):
    id : int
    name: str
    surname:str 
    github: str
    age: int

users_list = [Users(id = 1, name = "juan", surname = "dev",  github ="jzuluagadev", age = 42),
              Users(id = 2, name = "jose", surname = "zulu", github = "jzulu",      age = 42),
              Users(id = 3, name = "juli", surname = "zuga", github = "julidiseño", age = 19)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"juan", "surname":"dev", "github":"jzuluagadev", "age": 42},
            {"name":"jose", "surname":"zulu", "github":"jzulu","age": 42},
            {"name":"juli", "surname":"zuga", "github":"julidiseño", "age": 19},
            ]  

@app.get("/users")
async def users():
    return users_list 

@app.get("/users/{id}")
async def user(id: int):
    user = filter(lambda user: user.id = id, users_list)
    return list(users)