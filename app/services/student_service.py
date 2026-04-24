from app.models import Students
from app.schemas import StudentCreate , StudentUpdate
from sqlalchemy.orm import Session


def create_students(db : Session , data : StudentCreate):
    student = Students(
        name = data.name,
        email = data.email
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

def update_students(db : Session,student_id : int, data : StudentUpdate):
    student = get_student(db,student_id)

    if not student:
        return None
    
    if data.name:
        student.name = data.name
    
    if data.email:
        student.email = data.email

    return student
    

def get_student(db : Session , student_id : int):
    student = db.query(Students).filter(Students.id == student_id).first()

    return student




