from fastapi import FastAPI
from app.routes import courses , enrollments ,students
from app.database import Base , engine

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)