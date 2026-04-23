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
