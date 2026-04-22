from pydantic import BaseModel


class CreateStudents(BaseModel):
    name : str
    email : str


