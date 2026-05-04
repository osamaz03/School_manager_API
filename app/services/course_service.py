from app.models import Course
from app.schemas import CourseCreate , CourseUpdate
from sqlalchemy.orm import Session


def create_course(db : Session , data : CourseCreate):
    course = Course(
        title = data.title,
        description = data.description
    )

    db.add(course)
    
    db.commit()

    db.refresh(course)

    return course

def update_course(db : Session , course_id : int , data : CourseUpdate):
    course = get_course(db, course_id)

    if not course:
        return None
    
    if data.title:
        course.title = data.title

    if data.description:
        course.description = data.description

    return course

def get_courses(db :Session):
    courses = db.query(Course).all()

    if not courses:
        return None

    return courses

def get_course(db : Session , course_id : int):
    course = db.query(Course).filter(Course.id == course_id).first()

    return course


def delete_course(db : Session , course_id : int):
    course = get_course(db , course_id)

    if course:
        db.delete(course)
        db.commit()
    else:
        return None
    
    return course