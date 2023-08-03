# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app files to the container
COPY . .

# Expose the port your back-end is running on (if applicable)
EXPOSE 5000

# Command to start the back-end server
CMD ["python", "app.py"]
