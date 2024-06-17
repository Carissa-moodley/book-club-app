# Online Book Club

This is a simple Django-based web application for an online Book Club. 
Members can log in, view books read by the club and vote for the next month's book.

## Features

- User authentication (login and sign up)
- Display books read by the club with images
- Vote for the next book to be read by the club
- Responsive design using Bootstrap

## Requirements
- Python version 3 or up
- Django version 5 or up
- Docker

## Project Setup

### Clone the Repository

Clone this repository on your local machine by typing the following in your terminal 

`git clone https://github.com/Carissa-moodley/bookclub-app.git`

`cd bookclub-app`

### Create and Activate Virtual Environment

For windows, install the following modules to set up yout virtual environment:

`python -m pip install pip`

`pip install virtualenv`

`pip install virtualenvwrapper-win`

Set up your virtual environment venv and activate it by typing the following:

`mkvirtualenv venv`


### Install Dependencies

`python pip install -r requirements.txt`

### Apply Migrations and Run Server

`python manage.py migrate`
`python manage.py runserver`

### Create Superuser

To access the Django admin panel, you need to create a superuser.

`python manage.py createsuperuser` 

### Access the Application

The application can be accessed at http://127.0.0.1:8000/ in your browser and the admin panel can be accessed at http://127.0.0.1:8000/admin/

## Setup and Run with Docker

### Clone the Repository

`git clone https://github.com/Carissa-moodley/bookclub-app.git`

`cd bookclub-app`

### Build and Run the Docker Container

`docker build -t book-club`
`docker run -p 8000:8000 book-club`

### Access the Application

The application can be accessed at http://<server-ip>:8000

## Documentation
 
### Building Documentation

To build the Sphinx documentation, navigate to the `docs` directory and run:

`make html`

The generated documentation can be found in `docs/build/html`

### Author

Carissa Moodley


