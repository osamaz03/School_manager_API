from pydantic import BaseModel


#--------Students--------

class StudentCreate(BaseModel):
    name : str
    email : str

class StudentUpdate(BaseModel):
    name : str = None
    email : str = None

class StudentResponse(BaseModel):
    id : int
    name : str
    email : str

    class config: # to let pydantic to read objects
        from_attributes = True


#--------Course--------

class CourseCreate(BaseModel):
    title : str
    description : str

class CourseUpdate(BaseModel):
    title : str = None
    description : str = None

class CourseResponse(BaseModel):
    id : int
    title : str
    description : str

    class config: # to let pydantic to read objects
        from_attributes = True

class EnrollmentCreate(BaseModel):
    student_id : int
    course_id : int


