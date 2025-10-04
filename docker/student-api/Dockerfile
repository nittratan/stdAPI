# Base image
FROM python:3.10-slim

# Install bash
RUN apt-get update && apt-get install -y bash

# Set working directory inside container
WORKDIR /app

# Install FastAPI + Uvicorn
RUN pip install fastapi uvicorn

# Copy current folder files into container
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI app with reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
