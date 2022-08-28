from ast import Str
from optparse import Option
from typing import Optional 
from fastapi import FastAPI,Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="LMS With Fastapi Test",
    description="LMS Mapping for students and courses.",
    version="0.0.1",
    contact={
        "name": "abhi",
        "email": "abhi@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


users = []

class User(BaseModel):
    email: str
    is_active : bool
    bio: Optional[str]

@app.get("/users")
async def get_users():
    return users


@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return "sucess"

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="the id of the users you want to retrive" , gt=2),
    q : str = Query(None , max_length=5)

):
    return {"user": users[id] , "query" : q}