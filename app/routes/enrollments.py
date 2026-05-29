from fastapi import APIRouter , status , Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import EnrollmentCreate
from app.services.enrollment_service import enroll_student , get_students_for_course , get_courses_for_student , remove_enrollment


router = APIRouter()

@router.post("/enrollments",status_code=status.HTTP_201_CREATED)
async def enroll(data : EnrollmentCreate , db : Session = Depends(get_db)):
    return enroll_student(db , data)

@router.get("/enrollments/get_course/{course_id}",status_code=status.HTTP_200_OK)
async def get_students_from_course(course_id : int , db : Session = Depends(get_db)):
    return get_students_for_course(db , course_id)

@router.get("/enrollments/get_student/{student_id}",status_code=status.HTTP_200_OK)
async def get_courses_from_student(student_id : int , db : Session = Depends(get_db)):
    return get_courses_for_student(db , student_id)

@router.delete("/enrollments",status_code=status.HTTP_200_OK)
async def delete_enrollment(data : EnrollmentCreate , db : Session = Depends(get_db)):
    return remove_enrollment(db , data)


