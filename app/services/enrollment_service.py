from app.models import Students , Course
from app.schemas import EnrollmentCreate
from sqlalchemy.orm import Session


def enroll_student(db : Session , data : EnrollmentCreate):

    student = db.query(Students).filter(Students.id == data.student_id).first()

    course = db.query(Course).filter(Course.id == data.course_id).first()


    student.courses.append(course)

    db.commit()

    db.refresh(student)

    return student


def get_students_for_course(db : Session , course_id : int):

    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        return None

    return course.students


def get_courses_for_student(db : Session, student_id : int):
    student = db.query(Students).filter(Students.id == student_id).first()

    if not student:
        return None

    return student.courses


def remove_enrollment(db : Session , data : EnrollmentCreate):
    student = db.query(Students).filter(Students.id == data.student_id).first()

    course = db.query(Course).filter(Course.id == data.course_id).first()

    student.courses.remove(course)

    db.commit()

    return {"message" : "Enrollment removed"}
