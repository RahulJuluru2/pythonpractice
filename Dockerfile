# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
COPY dev-requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt -r dev-requirements.txt

# Install FastAPI and Uvicorn for web app
RUN pip install fastapi uvicorn

# Copy source code
COPY src/ ./src/
COPY tests/ ./tests/

# Expose port for web app (to be used by FastAPI/Flask)
EXPOSE 8000

# Default command to run FastAPI app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
