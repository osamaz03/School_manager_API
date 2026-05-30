from fastapi import APIRouter , status , Depends , HTTPException
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
    course = get_students_for_course(db , course_id)

    if course == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="course not found")

@router.get("/enrollments/get_student/{student_id}",status_code=status.HTTP_200_OK)
async def get_courses_from_student(student_id : int , db : Session = Depends(get_db)):
    student = get_courses_for_student(db , student_id)

    if student == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="student not found")

@router.delete("/enrollments",status_code=status.HTTP_200_OK)
async def delete_enrollment(data : EnrollmentCreate , db : Session = Depends(get_db)):
    return remove_enrollment(db , data)


