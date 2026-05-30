import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.schemas import (
    StudentCreate,
    StudentUpdate,
    CourseCreate,
    CourseUpdate,
    EnrollmentCreate,
)
from app.services.student_service import (
    create_student,
    all_students,
    get_student,
    update_student,
    delete_student,
)
from app.services.course_service import (
    create_course,
    all_courses,
    get_course,
    update_course,
    delete_course,
)

from app.services.enrollment_service import (
    enroll_student,
    get_students_for_course,
    get_courses_for_student,
    remove_enrollment,
)



# TEST DATABASE


@pytest.fixture
def db():

    engine = create_engine("sqlite:///:memory:")

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session

    finally:
        session.close()



# STUDENT TESTS


def test_create_student(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    assert student.id is not None
    assert student.name == "Osama"
    assert student.email == "osama@gmail.com"


def test_get_all_students(db):

    create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    students = all_students(db)

    assert len(students) == 1
    assert students[0].name == "Osama"


def test_get_student_by_id(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    found_student = get_student(db, student.id)

    assert found_student is not None
    assert found_student.id == student.id


def test_update_student(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    updated_student = update_student(
        db,
        student.id,
        StudentUpdate(
            name="Ali",
            email="ali@gmail.com"
        )
    )

    assert updated_student.name == "Ali"
    assert updated_student.email == "ali@gmail.com"


def test_delete_student(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    delete_student(db, student.id)

    deleted_student = get_student(db, student.id)

    assert deleted_student is None



# COURSE TESTS


def test_create_course(db):

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    assert course.id is not None
    assert course.title == "Python"


def test_get_all_courses(db):

    create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    courses = all_courses(db)

    assert len(courses) == 1
    assert courses[0].title == "Python"


def test_get_course_by_id(db):

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    found_course = get_course(db, course.id)

    assert found_course is not None
    assert found_course.id == course.id


def test_update_course(db):

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    updated_course = update_course(
        db,
        course.id,
        CourseUpdate(
            title="FastAPI",
            description="Backend Course"
        )
    )

    assert updated_course.title == "FastAPI"
    assert updated_course.description == "Backend Course"


def test_delete_course(db):

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    delete_course(db, course.id)

    deleted_course = get_course(db, course.id)

    assert deleted_course is None



# ENROLLMENT TESTS


def test_enroll_student(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    enrolled_student = enroll_student(
        db,
        EnrollmentCreate(
            student_id=student.id,
            course_id=course.id
        )
    )

    assert len(enrolled_student.courses) == 1
    assert enrolled_student.courses[0].title == "Python"


def test_get_students_for_course(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    enroll_student(
        db,
        EnrollmentCreate(
            student_id=student.id,
            course_id=course.id
        )
    )

    students = get_students_for_course(db, course.id)

    assert len(students) == 1
    assert students[0].name == "Osama"


def test_get_courses_for_student(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    enroll_student(
        db,
        EnrollmentCreate(
            student_id=student.id,
            course_id=course.id
        )
    )

    courses = get_courses_for_student(db, student.id)

    assert len(courses) == 1
    assert courses[0].title == "Python"


def test_remove_enrollment(db):

    student = create_student(
        db,
        StudentCreate(
            name="Osama",
            email="osama@gmail.com"
        )
    )

    course = create_course(
        db,
        CourseCreate(
            title="Python",
            description="Programming Course"
        )
    )

    enroll_student(
        db,
        EnrollmentCreate(
            student_id=student.id,
            course_id=course.id
        )
    )

    remove_enrollment(
        db,
        EnrollmentCreate(
            student_id=student.id,
            course_id=course.id
        )
    )

    courses = get_courses_for_student(db, student.id)

    assert courses == []