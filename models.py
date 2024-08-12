from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    hours: float
    is_done: bool = False
    id: int = None


class ChangeTask(Task):
    title: str = None
    description: str = None
    hours: float = None
    is_done: bool = None
    id: int = None
