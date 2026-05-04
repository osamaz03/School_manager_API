from fastapi import APIRouter , HTTPException , status , Depends 
from app.database import get_db 
from sqlalchemy.orm import Session
from schemas import StudentCreate , StudentUpdate , StudentResponse
from app.services.student_service import create_student , update_student , get_student , all_students, delete_student


router = APIRouter()


@router.post("/students",status_code=status.HTTP_201_CREATED)
async def add_student(data : StudentCreate , db: Session = Depends(get_db)):
    return create_student(db , data)



@router.get("/students",status_code=status.HTTP_200_OK,responses=StudentResponse)
async def get_all_students(db : Session = Depends(get_db)):
    students = all_students(db)

    if students == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="still no students")
    
    return students

@router.get("/students/{id}",status_code=status.HTTP_200_OK,responses=StudentResponse)
async def get_student_by_id(student_id : int ,db : Session = Depends(get_db)):
    student = get_student(db,student_id)

    if student == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,detail="Student NOT FOUND!!")
    
    return student



@router.put("/students/{id}", status_code=status.HTTP_200_OK)
async def edit_student(student_id : int , data : StudentUpdate , db : Session = Depends(get_db)):
    student = update_student(db , student_id , data)
    
    if student == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= "Student NOT FOUND!!")
    
    return student


@router.delete("/students/{id}",status_code=status.HTTP_200_OK)
async def del_student(student_id : int , db : Session = Depends(get_db)):
    student = delete_student(db , student_id)

    if student == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="There is no student to delete")
    
    return {"message" : "Deleted"}

    