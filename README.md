# Django Snacks

[Link to Latest PR](https://github.com/ticochuck/django-snacks/pull/1)

## Description
Create web site in Django with 2 pages
- home page
- about page
- create views/urls/templates as needed for home and about pages
- use ancestor template to contain navigation elements
- Should be built the “Django way” aka match the structure of in-class demo

## Usage

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with the following variables and save it into 'snacks_project' directory
    - SECRET_KEY=secret key for the app (typically 50-characters long string)
    - DEBUG=should be set to True in development
    - ALLOWED_HOSTS=localhost,127.0.0.1 (for testing)
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py collectstatic` - to collect apps static files
- `python manage.py runserver` - to run server

## Tests
Use Django’s built in testing tools
- Test that home and about url status codes
- Test home and about url template use, including ancestor template.

## Lab26 - Intro to Django

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160044)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)
