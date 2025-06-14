from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional
from uuid import uuid4
import logging
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------- Schemas ------------------------- #
class Address(BaseModel):
    street: str
    city: str
    pin: int
    home_contact: str

class Student(BaseModel):
    id: int = Field(..., example=1)
    name: str
    age: int
    moble: int
    email: EmailStr
    course: str
    address: Address

# ------------------------- In-memory DB ------------------------- #
students_db: Dict[int, Student] = {}

# ------------------------- Routes ------------------------- #
@app.get("/", tags=["Root"])
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Student API"}


@app.get("/students", response_model=List[Student])
def get_all_students():
    try:
        logger.info("Fetching all students")
        return list(students_db.values())
    except Exception as e:
        logger.error(f"Error in get_all_students: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int = Path(..., gt=0)):
    try:
        logger.info(f"Fetching student with id {student_id}")
        if student_id not in students_db:
            raise HTTPException(status_code=404, detail="Student not found")
        return students_db[student_id]
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error in get_student: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/students", response_model=Student, status_code=201)
def create_student(student: Student):
    try:
        logger.info(f"Creating student with id {student.id}")
        if student.id in students_db:
            raise HTTPException(status_code=400, detail="Student ID already exists")
        students_db[student.id] = student
        return student
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error in create_student: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    try:
        logger.info(f"Updating student with id {student_id}")
        if student_id != student.id:
            raise HTTPException(status_code=400, detail="ID in path and body must match")
        if student_id not in students_db:
            raise HTTPException(status_code=404, detail="Student not found")
        students_db[student_id] = student
        return student
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error in update_student: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    try:
        logger.info(f"Deleting student with id {student_id}")
        if student_id not in students_db:
            raise HTTPException(status_code=404, detail="Student not found")
        del students_db[student_id]
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error in delete_student: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
