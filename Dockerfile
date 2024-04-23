# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files and subfolders from the directory where the Dockerfile is located into the container at /app


EXPOSE 5000

# Run python script when the container launches
CMD ["python", "main.py"]
