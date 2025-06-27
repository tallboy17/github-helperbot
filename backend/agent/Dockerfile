# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Environment defaults
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir is good for Docker builds to keep image size small
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install google-generativeai

# Copy the rest of the application code into the container at /app
COPY app/ /app/

# Expose port 1717 (where the Flask app will run)
EXPOSE 1717

# Set default command to run the Flask app
CMD ["python", "github_helper_ai.py"]