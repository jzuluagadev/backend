from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # comando para iniciar el server de fastApi en la  terminal "python -m uvicorn users:app --reload"

#class users
class Users(BaseModel):
    name: str
    surname:str 
    github: str
    age: int

users_list = [Users(name = "juan", surname = "dev",  github ="jzuluagadev", age = 42),
              Users(name = "jose", surname = "zulu", github = "jzulu",      age = 42),
              Users(name = "juli", surname = "zuga", github = "julidiseño", age = 19)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"juan", "surname":"dev", "github":"jzuluagadev", "age": 42},
            {"name":"jose", "surname":"zulu", "github":"jzulu","age": 42},
            {"name":"juli", "surname":"zuga", "github":"julidiseño", "age": 19},
            ]  

@app.get("/users")
async def users():
    return users_list #(name = "juan", surname = "dev", github = "jzuluagadev", age= 42),
                      #(name:"jose", surname:"zulu", github:"jzulu", age: 42),
                      #(name:"juli", surname:"zuga", github:"julidiseño", age: 19),|