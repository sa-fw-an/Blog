# Flask Blog Website

## Description

This is a simple blog website built using Flask, a lightweight WSGI web application framework in Python. The application allows users to register, log in, and create posts. It features user authentication, including login and signup functionalities, and uses SQLite as the database for storing user information and blog posts.

### Features
- User authentication (login, signup, logout)
- Create, read, update, and delete blog posts
- Responsive web design for mobile and desktop
- Flash messages for user feedback
- Secure password storage using hashing

## Technologies Used
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug
- HTML/CSS
- Bootstrap (for styling)
- SQLite (for local development)

## Run the Following commands for windows
- cd /to your directory
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- set FLASK_APP=app.py
- flask db init
- flask db migrate
- flask db upgrade
- flask run