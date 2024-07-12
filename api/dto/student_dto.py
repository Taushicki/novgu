from pydantic import BaseModel


class Student(BaseModel):
    course: int
    group: str
    form: str
    name: str
    spec: str
