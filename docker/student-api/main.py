from fastapi import FastAPI, HTTPException
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

# In-memory datastore (list of dicts)
students = [
    {"roll": 1, "name": "Ravi Kumar", "department": "CSE", "year": 3, "mobile": "9876543210", "city": "Delhi"},
    {"roll": 2, "name": "Anita Sharma", "department": "ECE", "year": 2, "mobile": "9123456780", "city": "Mumbai"},
]

# Index route
@app.get("/")
def index():
    logger.info("Index endpoint accessed")
    return {"message": "Welcome to Student API 🚀"}

# Get all students
@app.get("/students")
def get_students():
    logger.info("Retrieving all students")
    return students

# Get student by roll
@app.get("/students/{roll}")
def get_student(roll: int):
    logger.info(f"Searching for student with roll number: {roll}")
    for student in students:
        if student["roll"] == roll:
            logger.info(f"Student found: {student}")
            return student
    logger.warning(f"Student with roll number {roll} not found")
    raise HTTPException(status_code=404, detail="Student not found")

# Add new student
@app.post("/students")
def add_student(student: dict):
    logger.info(f"Attempting to add new student: {student}")
    # check roll already exists
    for s in students:
        if s["roll"] == student["roll"]:
            logger.warning(f"Roll number {student['roll']} already exists")
            raise HTTPException(status_code=400, detail="Roll number already exists")
    students.append(student)
    logger.info(f"Student added successfully: {student}")
    return {"message": "Student added successfully", "student": student}

# Update student by roll
@app.put("/students/{roll}")
def update_student(roll: int, updated_student: dict):
    logger.info(f"Attempting to update student with roll number: {roll}")
    for idx, student in enumerate(students):
        if student["roll"] == roll:
            students[idx].update(updated_student)
            logger.info(f"Student updated successfully: {students[idx]}")
            return {"message": "Student updated successfully", "student": students[idx]}
    logger.warning(f"Student with roll number {roll} not found")
    raise HTTPException(status_code=404, detail="Student not found")

# Delete student by roll
@app.delete("/students/{roll}")
def delete_student(roll: int):
    logger.info(f"Attempting to delete student with roll number: {roll}")
    for idx, student in enumerate(students):
        if student["roll"] == roll:
            deleted = students.pop(idx)
            logger.info(f"Student deleted successfully: {deleted}")
            return {"message": "Student deleted successfully", "student": deleted}
    logger.warning(f"Student with roll number {roll} not found")
    raise HTTPException(status_code=404, detail="Student not found")
