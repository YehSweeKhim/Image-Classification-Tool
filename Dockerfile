# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the FastAPI app
CMD ["/usr/local/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]