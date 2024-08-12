from fastapi import FastAPI

app = FastAPI()


@app.get("/square/{number}")
def square(number: int):
    return {"result": number ** 2}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("tasks:app")
