from fastapi import FastAPI

from db_manager import db_manager
from models import Task, ChangeTask

app = FastAPI()


@app.post("/tasks")
async def create(task: Task):
    db_manager.add_task(task)
    return task


@app.get("/tasks")
async def tasks():
    return db_manager.get_all_tasks()


@app.get("/tasks/{task_id}")
async def task(task_id: int):
    return db_manager.get_task(task_id)


# @app.put("/tasks/{task_id}")
# def edit(task_id: int, task: ChangeTask):
#     for task_ in tasks_list:
#         if task_.id == task_id:
#
#             if task.title is not None:
#                 task_.title = task.title
#
#             if task.description is not None:
#                 task_.description = task.description
#
#             if task.is_done is not None:
#                 task_.is_done = task.is_done
#
#             if task.hours is not None:
#                 task_.hours = task.hours
#             return ""


@app.delete("/tasks/{task_id}")
async def delete(task_id: int):
    db_manager.delete_task(task_id)
    return ""


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("todolist:app")
