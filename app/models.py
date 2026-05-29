from sqlalchemy import Column, Integer , ForeignKey , Table , String
from sqlalchemy.orm import relationship
from app.database import Base

enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer , primary_key=True)
    name = Column(String)
    email = Column(String)

    courses = relationship(
        "Course",
        secondary=enrollments,
        back_populates="students"
    )

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)

    students = relationship(
        "Students",
        secondary=enrollments,
        back_populates="courses"
    )

