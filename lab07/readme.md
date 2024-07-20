# Flask Application Lab 07

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Hosting on PythonAnywhere](#hosting-on-pythonanywhere)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Introduction

This Flask application, developed for Lab 07, implements a user registration and login system using Flask and SQLite. The application allows users to register, log in, view a secret page, and log out. Passwords are securely hashed, and the application includes validation checks and informative flash messages.

## Features

- User Registration
- User Login
- Password Hashing
- Session Management
- Flash Messages
- Bootstrap Styling
- Responsive Design

## Requirements

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy
- Werkzeug
- Bootstrap (for styling)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ShahariarRabby/adv_web/
   cd lab07
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install Flask Flask-SQLAlchemy Werkzeug
   ```

## Running the Application

1. Ensure you are in the project directory.
2. Activate the virtual environment.
3. Run the application using:
   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000`.

## File Structure

```
lab07/
│
├── app.py
├── users.db
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── secret_page.html
│   └── thankyou.html
└── instance/
    └── db/
```

- `app.py`: Main application file containing routes and logic.
- `users.db`: SQLite database file.
- `templates/`: Directory containing HTML templates.
- `instance/`: Directory for instance-specific files (auto-created).

## Usage

### Registration

1. Navigate to the registration page by clicking "Register here" on the home page.
2. Fill in the required fields: First Name, Last Name, Email, Password, and Confirm Password.
3. Ensure your password meets the criteria:
   - Must contain a lowercase letter
   - Must contain an uppercase letter
   - Must end in a number
   - Must be at least 8 characters long
4. Click "Register". If successful, you will be redirected to the thank you page. If not, appropriate error messages will be shown.

### Login

1. On the home page, enter your registered email and password.
2. Click "Submit". If the credentials are correct, you will be redirected to the secret page. If not, an error message will be displayed.

### Secret Page

- After logging in, you will see a personalized welcome message.
- You can log out by clicking the "Logout" button, which will redirect you to the home page with a logout confirmation message.

## Hosting on PythonAnywhere

1. **Upload Your Code**:
   - Ensure your Flask application files (`app.py`, templates, etc.) are uploaded to the correct directory on PythonAnywhere.
   - You can use the file manager in PythonAnywhere's dashboard or an SFTP client to upload your files.

2. **Set Up Virtual Environment**:
   - Navigate to your home directory in the PythonAnywhere console.
   - Create a virtual environment if you haven't already:
     ```bash
     mkvirtualenv my-venv --python=python3.9
     ```
   - Install the necessary packages:
     ```bash
     pip install Flask Flask-SQLAlchemy Werkzeug
     ```

3. **Configure WSGI File**:
   - Edit the WSGI file (`/var/www/your_username_pythonanywhere_com_wsgi.py`) to point to your Flask application. Example:
     ```python
     import sys
     import os

     # Add your project directory to the sys.path
     project_home = '/home/your_username/mysite'
     if project_home not in sys.path:
         sys.path.append(project_home)

     # Set the virtual environment
     activate_this = os.path.expanduser("~/my-venv/bin/activate_this.py")
     exec(open(activate_this).read(), {'__file__': activate_this})

     # Import your Flask app
     from app import app as application
     ```

4. **Reload Your Web App**:
   - Go to the "Web" tab on PythonAnywhere dashboard.
   - Click "Reload" to restart your web application with the new configuration.

## Troubleshooting

### Common Issues

1. **Invalid credentials**:
   - Ensure that you have registered before trying to log in.
   - Double-check your email and password for any typos.

2. **Email already registered**:
   - Use a different email address to register.
   - If you have forgotten your password, consider adding a password recovery feature (not implemented in this lab).

3. **Application errors**:
   - Ensure all dependencies are installed correctly.
   - Check the terminal/command prompt for any error messages and tracebacks.

## Credits

Developed as part of the CS421/621 Lab 07 exercise.
