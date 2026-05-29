from fastapi import APIRouter , HTTPException , status , Depends 
from app.database import get_db 
from sqlalchemy.orm import Session
from app.schemas import CourseCreate, CourseUpdate, CourseResponse
from app.services.course_service import create_course, update_course, get_course, all_courses, delete_course


router = APIRouter()

@router.post("/courses", status_code=status.HTTP_201_CREATED, response_model=CourseResponse)
async def add_courses(data: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db, data)



@router.get("/courses", status_code=status.HTTP_200_OK, response_model=list[CourseResponse])
async def show_courses(db: Session = Depends(get_db)):
    courses = all_courses(db)

    if not courses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="still no courses!!")

    return courses


@router.get("/courses/{course_id}", status_code=status.HTTP_200_OK, response_model=CourseResponse)
async def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    course = get_course(db , course_id)


    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= "course NOT FOUND !!")
    
    return course

@router.put("/courses/{id}", status_code=status.HTTP_200_OK, response_model=CourseResponse)
async def edit_course(course_id: int, new_data: CourseUpdate | CourseCreate, db: Session = Depends(get_db)):
    new_course = update_course(db, course_id, new_data)


    if new_course == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="There is no course to edit!!")
    
    return new_course


@router.delete("/courses/{id}",status_code=status.HTTP_200_OK)
async def del_course(course_id : int , db : Session = Depends(get_db)):
    deleted_course = delete_course(db , course_id)

    if deleted_course == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="There is no course to delete!!")
    
    return deleted_course