# FastAPI Student Management Application

Containerize an app with Docker
A RESTful API service built with FastAPI for managing student records with logging capabilities.

## Features

- CRUD operations for student management
- Input validation and error handling
- Comprehensive logging system
- Containerized with Docker
- Simple in-memory data storage
- RESTful API endpoints

## Docker Setup

### Pull the Docker Image

```bash
docker pull baapgtech/fastapi-student-app:2.0
```

### Run the Container

```bash
docker run -d -p 8000:8000 baapgtech/fastapi-student-app:2.0
```

This will:
- Run the container in detached mode (-d)
- Map port 8000 on your host to port 8000 in the container
- Use version 2.0 of the application

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /students | List all students |
| GET | /students/{roll} | Get student by roll number |
| POST | /students | Add new student |
| PUT | /students/{roll} | Update student by roll number |
| DELETE | /students/{roll} | Delete student by roll number |

## API Usage Examples

### Get All Students
```bash
curl http://localhost:8000/students
```

### Get Student by Roll Number
```bash
curl http://localhost:8000/students/1
```

### Add New Student
```bash
curl -X POST http://localhost:8000/students \
  -H "Content-Type: application/json" \
  -d '{
    "roll": 3,
    "name": "John Doe",
    "department": "CSE",
    "year": 2,
    "mobile": "9876543210",
    "city": "Bangalore"
  }'
```

### Update Student
```bash
curl -X PUT http://localhost:8000/students/3 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "department": "CSE",
    "year": 3,
    "mobile": "9876543210",
    "city": "Bangalore"
  }'
```

### Delete Student
```bash
curl -X DELETE http://localhost:8000/students/3
```

## Student Data Structure

```json
{
  "roll": "integer",
  "name": "string",
  "department": "string",
  "year": "integer",
  "mobile": "string",
  "city": "string"
}
```

## Logging

The application includes comprehensive logging with:
- Console output for immediate visibility
- File logging to `app.log`
- Timestamp, logger name, log level, and message formatting
- INFO level for successful operations
- WARNING level for errors and not found scenarios

## Development

### Local Setup (without Docker)

1. Clone the repository
2. Install dependencies:
```bash
pip install fastapi uvicorn
```

3. Run the application:
```bash
uvicorn main:app --reload
```

### Access the API Documentation

Once the application is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Monitoring

- Check the application logs in `app.log`
- Monitor Docker container:
```bash
docker logs [container_id]
```

## Version Information

- FastAPI Student App Version: 2.0
- Base Image: Python:3.9-slim
- FastAPI Framework
