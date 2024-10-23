# Use an official Python runtime as a base image
FROM python:3.12.3  
# A lighter version of Python image
# Set the working directory

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the inference script
COPY web_interface.py .

# Run the inference script when the container starts
CMD ["python", "web_interface.py"]


