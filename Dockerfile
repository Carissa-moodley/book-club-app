
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app
# Copy the project
COPY . /app/
# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Set up Django
RUN python manage.py migrate

# Run command line to start up server at port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
