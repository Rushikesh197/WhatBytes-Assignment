# WhatBytes Django Application

This is a Django web application for user authentication, including functionalities for login, signup, password reset, profile management, and more. The project is structured to follow best practices and utilize Django's built-in authentication system.

## Table of Contents

- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

## Features

- User authentication with email or username and password.
- Pages for login, signup, forgot password, change password, dashboard, and profile.
- Password reset functionality via email.
- User feedback through messages for actions like registration, login, and password changes.

## Folder Structure

```
whatbytes_project/
│
├── whatbytes_project/                # Main Django project settings and configuration files
│   ├── __init__.py                   # Python package marker
│   ├── asgi.py                       # ASGI config
│   ├── settings.py                   # Main settings file
│   ├── urls.py                       # Project-level URL configuration
│   ├── wsgi.py                       # WSGI config
│
├── user_auth/                        # Django app for user authentication
│   ├── migrations/                   # Auto-generated migration files
│   │   └── __init__.py               # Python package marker for migrations
│   ├── static/                       # Static files (CSS, JS, images)
│   │   └── user_auth/                # App-specific static files
│   │       └── style.css             # CSS for the app's visual styling
│   ├── templates/                    # HTML templates for the app
│   │   └── user_auth/                # App-specific templates
│   │       ├── base.html             # Base layout for other pages
│   │       ├── login.html            # Login page
│   │       ├── signup.html           # Signup page
│   │       ├── forgot_password.html  # Forgot password page
│   │       ├── dashboard.html        # Dashboard for logged-in users
│   │       ├── profile.html          # Profile page
│   │       └── registration/         # Directory for password reset templates
│   │           ├── password_reset_complete.html
│   │           ├── password_reset_done.html
│   │           └── password_reset_form.html
│   ├── admin.py                      # Django admin settings for the app
│   ├── apps.py                       # Configuration for the app
│   ├── forms.py                      # Custom Django forms if needed
│   ├── models.py                     # Database models (not needed for default user auth)
│   ├── views.py                      # Views to handle HTTP requests
│   ├── urls.py                       # URL routing specific to user authentication app
│   ├── tests.py                      # Test cases (optional)
│   ├── __init__.py                   # Python package marker
│
├── db.sqlite3                        # SQLite database file (auto-generated)
├── manage.py                         # Django command-line utility
└── README.md                         # Documentation for your project
```

## Installation and Setup

To set up this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/whatbytes_project.git
   cd whatbytes_project
   ```

2. **Create a Virtual Environment**:
   It is recommended to create a virtual environment to manage your project dependencies.
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**:
   Ensure that you have Django installed. If you have a `requirements.txt` file, install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations**:
   Initialize the database with required tables.
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Admin)**:
   You need a superuser account to access the Django admin interface.
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

To run the development server, use the following command:

```bash
python manage.py runserver
```

You can then access the application by visiting:

```
http://127.0.0.1:8000/
```

## How to Use

1. **Access the Application**:
   - Go to `http://127.0.0.1:8000/login/` to log in.
   - Use `http://127.0.0.1:8000/signup/` to create a new account.
   - If you forget your password, go to `http://127.0.0.1:8000/password-reset/` to reset it.

2. **User Management**:
   - After logging in, you can navigate to your dashboard and profile.
   - Change your password from the profile section.

3. **Django Admin**:
   - Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser account you created to manage users and other models.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions, suggestions, and feedback are always welcome!
