# Use Python Alpine image for a smaller footprint
FROM python:3.10-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Create the directory /home/output where the result.txt file will be written
RUN mkdir -p /home/output

# Copy the Python script into the container
COPY script.py .

# Command to run the script
CMD ["python", "./script.py"]

