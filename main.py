from typing import Union

import fastapi
from fastapi import FastAPI
from pydantic import BaseModel

from check_pswd import check_pswd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


names = [
    "Roman",
    "John"
]


@app.get("/hello/{name}")
def hello_python(name):
    if name in names:
        return {"Hello": name}

    raise fastapi.HTTPException(404, "User not found")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/create")
def create():
    return "Created"


@app.get("/add")
def add(a: int, b: int):
    return a + b


@app.get("/sub")
def sub(a: int, b):
    return a - b


@app.get("/check_password")
def check_password(password: str):
    """
    не менше 8 символів
    має бути 1 велика та 1 мала літера
    має бути цифра
    має бути символ $_@!


    поганий
    слабкий
    нормальний
    гарний

    bad
    weak
    good
    very good
    """
    return check_pswd(password)


@app.get("/square/{number}")
def square(number: int):
    pass


class User(BaseModel):
    name: str
    age: int
    password: str


@app.post("/register", status_code=201)
def register(user: User):
    return {"message": "User created", "data": {"name": user.name, "age": user.age}}


class Age(BaseModel):
    age: int

@app.post("/info/{city}")
def info(city: str, name: str, age: Age):
    return {"city": city, "name": name, "age": age.age}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app")
