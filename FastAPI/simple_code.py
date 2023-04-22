from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, Union
from fastapi import status, HTTPException

app = FastAPI()

@app.get("/")
def index():
    return "hello world"


@app.post("/hello")
def test_post():
    return "hello post"

# path parameters
@app.get("/homepath/{name}/{age}")
def get_name(name, age):
    return name + age

# path parameters, جایی که نیاز داده خودش تبدیل می کنه به چیزی که گفتیم
@app.get("/path/{name}")
def get_name_annot(name: str):
    return name


# query parameter
@app.get("/query/")
def test_query(name:str="ali"):
    return name


# request body
class Person(BaseModel):
    name: Union[str, None] = None
    familt: Optional[str]
    age: Optional[int] #= Query(max_length=2)

@app.post("/add/person")
def get_person(person: Person):
    return person.name



@app.get("/test/{name}")
def test(name: str= Path(title="name")):
    return name


class UserIn(BaseModel):
    username:str
    email:str
    password:str

class UserOut(BaseModel):
    username: str
    email: str

@app.post("/add/user", response_model=UserOut)
def get_new_user(user:UserIn):
    if user.username == "sanaz":
        raise HTTPException(detail="she is sanaz, who are you?" , status_code=status.HTTP_400_BAD_REQUEST)
    return user

