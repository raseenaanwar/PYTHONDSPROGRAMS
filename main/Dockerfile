#FROM python:3.9
#ENV PYTHONUNBUFFERED 1
#WORKDIR /app
#COPY requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt
#COPY . /app

FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the project code into the container at /code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
