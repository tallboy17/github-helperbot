# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install build-essential package to provide compilers (gcc, g++, make)
# and other build tools required for some Python packages.
# apt-get update is necessary before apt-get install.
# rm -rf /var/lib/apt/lists/* reduces the final image size.
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir is good for Docker builds to keep image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 5000 (where the Flask app will run)
EXPOSE 5000

# Command to run the application with Gunicorn
# 0.0.0.0 makes the server accessible from outside the container
# --workers 4 specifies 4 worker processes
# app:app refers to the 'app' object inside the 'app.py' file
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]