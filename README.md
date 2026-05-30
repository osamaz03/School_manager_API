# School Manager API

A simple FastAPI project for managing students, courses, and enrollments in a school system.

The API uses:

- `FastAPI` for the web framework
- `SQLAlchemy` for database access
- `SQLite` for local storage
- `Pydantic` for request and response validation
- `pytest` for tests

## Features

- Create, read, update, and delete students
- Create, read, update, and delete courses
- Enroll a student in a course
- View students in a course
- View courses for a student
- Remove an enrollment

## Project Structure

```text
School_Manager_API/
├── app/
│   ├── routes/
│   │   ├── students.py
│   │   ├── courses.py
│   │   └── enrollments.py
│   ├── services/
│   │   ├── student_service.py
│   │   ├── course_service.py
│   │   └── enrollment_service.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── tests/
│   └── test_school.py
├── requirements.txt
└── school.db
```

## Setup

1. Create and activate a virtual environment.

```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Install the dependencies from `requirements.txt`.

```powershell
pip install -r requirements.txt
```

## Run the API

Start the development server with:

```powershell
uvicorn app.main:app --reload
```

The API will usually be available at:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

When the app starts, it automatically creates the database tables in `school.db`.

## API Endpoints

### Students

- `POST /students` - Create a student
- `GET /students` - Get all students
- `GET /students/{student_id}` - Get one student by ID
- `PUT /students/{student_id}` - Update a student
- `DELETE /students/{student_id}` - Delete a student

Example request body:

```json
{
  "name": "Osama",
  "email": "osama@gmail.com"
}
```

### Courses

- `POST /courses` - Create a course
- `GET /courses` - Get all courses
- `GET /courses/{course_id}` - Get one course by ID
- `PUT /courses/{id}` - Update a course
- `DELETE /courses/{id}` - Delete a course

Example request body:

```json
{
  "title": "Python",
  "description": "Programming Course"
}
```

### Enrollments

- `POST /enrollments` - Enroll a student in a course
- `GET /enrollments/get_course/{course_id}` - Get students in a course
- `GET /enrollments/get_student/{student_id}` - Get courses for a student
- `DELETE /enrollments` - Remove an enrollment

Example request body:

```json
{
  "student_id": 1,
  "course_id": 1
}
```

## Example Workflow

1. Create a student with `POST /students`
2. Create a course with `POST /courses`
3. Enroll the student with `POST /enrollments`
4. Check enrolled courses with `GET /enrollments/get_student/{student_id}`

## Run Tests

Run the test suite with:

```powershell
pytest
```

The tests use an in-memory SQLite database, so they do not modify `school.db`.

## Notes

- The project follows a simple layered structure using `routes`, `services`, `models`, and `schemas`.
- Project dependencies are listed in [requirements.txt](<C:/Users/HP Gaming/Desktop/python projects/School_Manager_API/requirements.txt>).
- SQLite is configured in [app/database.py](<C:/Users/HP Gaming/Desktop/python projects/School_Manager_API/app/database.py>), currently using `sqlite:///./school.db`.
- SQLAlchemy logging is enabled with `echo=True`, so SQL queries are printed in the console while the app runs.
