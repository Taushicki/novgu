from pydantic import BaseModel


class Student(BaseModel):
    courсe: int
    group: str
    form: str
    name: str
    spec: str
