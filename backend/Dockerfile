# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Install the missing library
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the rest of application code to the container
COPY . .

# Export the port that app runs on
EXPOSE 8000

# Command to run the application
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

