# Little Lemon Restaurant

Little Lemon is a fictional restaurant's backend API built with Django and Django REST Framework. It provides a basic homepage and API endpoints for browsing menu items, managing table bookings, and user authentication.


## Project Structure

```
littlelemon/
├── littlelemon/          # Project config (settings, urls, wsgi, asgi)
├── restaurant/           # Menu and booking models, views, serializers
├── LittleLemonAPI/       # Additional API views for menu items
├── templates/            # HTML templates (index page)
├── tests/                # Project-level test stubs
├── manage.py
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Progesh/Capstone-project.git
cd Capstone-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
python3 -m venv .venv            # If using python version 3+

source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

The project uses MySQL. Create a database named `littlelemon` and update the credentials in `littlelemon/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "littlelemon",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The server starts at `http://127.0.0.1:8000/`



## Running Tests

```bash
python manage.py test restaurant

```
# Littlelemon API Documentation

This document lists all API endpoints currently configured in the project.

## Base URL

- Local: `http://127.0.0.1:8000/`

## Authentication

This project uses token authentication (`rest_framework.authtoken`) and Djoser auth routes.

### Obtain Token

- `POST /api/api-token-auth/`

## API Endpoints

### LittleLemonAPI (`/api/`)

- `GET, POST /api/menu-items/` (requires authentication)
- `GET, PUT, PATCH, DELETE /api/menu-items/<int:pk>/` (requires authentication)
- `GET /api/message/` (requires authentication)


### Restaurant API (`/restaurant/`)

- `GET /restaurant/` (index page)
- `GET /restaurant/menu/`
- `GET /restaurant/menu/<int:pk>/`
- `POST /restaurant/menu/` (requires authentication)
- `PUT, PATCH, DELETE /restaurant/menu/<int:pk>/` (requires authentication)

### Booking API (DRF Router under `/restaurant/booking/`)

Router prefix is currently `tables`, so routes are:

- `GET, POST /restaurant/booking/tables/` (requires authentication)
- `GET, PUT, PATCH, DELETE /restaurant/booking/tables/<pk>/` (requires authentication)

## Djoser Auth Endpoints (`/auth/`)

- `POST /auth/token/login/`
- `POST /auth/token/logout/`
- `GET, POST /auth/users/`
- `GET /auth/users/<username>/`
- `GET /auth/users/me/`
- `POST /auth/users/activation/`
- `POST /auth/users/resend_activation/`
- `POST /auth/users/reset_password/`
- `POST /auth/users/reset_password_confirm/`
- `POST /auth/users/set_password/`
- `POST /auth/users/reset_username/`
- `POST /auth/users/reset_username_confirm/`
- `POST /auth/users/set_username/`

Djoser also exposes format-suffix variants (for example: `.json`) for several endpoints.
