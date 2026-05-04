from app.models import Students
from app.schemas import StudentCreate , StudentUpdate
from sqlalchemy.orm import Session


def create_student(db : Session , data : StudentCreate):
    student = Students(
        name = data.name,
        email = data.email
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

def update_student(db : Session,student_id : int, data : StudentUpdate):
    student = get_student(db,student_id)

    if not student:
        return None
    
    if data.name:
        student.name = data.name
    
    if data.email:
        student.email = data.email

    db.commit()
    db.refresh(student)

    return student


def all_students(db : Session):
    students =db.query(Students).all()

    if not students:
        return None

    return students
    

def get_student(db : Session , student_id : int):
    student = db.query(Students).filter(Students.id == student_id).first()

    if not student:
        return None

    return student

def delete_student(db : Session, student_id : int):
    student = get_student(db,student_id)

    if student:
        db.delete(student)
        db.commit()
    else:
        return None
    
    return student




