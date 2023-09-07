# Base image
FROM python:3.9

# Set the current working directory to /app.
WORKDIR /app

# Copy requirements.txt to the working directory
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application code
COPY ./app /app/app

# Set the command to run the uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
