# Task Manager REST API

A RESTful Task Manager API built using Django REST Framework with JWT authentication.

## Features

- User Registration
- JWT Authentication
- Login with Access & Refresh Tokens
- User-specific Tasks
- Create, Read, Update and Delete Tasks
- Task Validation
- MySQL Database
- Django REST Framework

## Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Postman

## API Endpoints

### Authentication

- `POST /api/register/` — Register a new user
- `POST /api/token/` — Login and generate JWT tokens
- `POST /api/token/refresh/` — Refresh access token

### Tasks

- `GET /api/tasks/` — Get user's tasks
- `POST /api/tasks/` — Create a task
- `GET /api/tasks/{id}/` — Get a specific task
- `PUT /api/tasks/{id}/` — Update a task
- `PATCH /api/tasks/{id}/` — Partially update a task
- `DELETE /api/tasks/{id}/` — Delete a task

## Authentication

This API uses JWT Bearer Token authentication.

After login, include the access token in the request:

`Authorization: Bearer <access_token>`

## Database

MySQL is used as the database for this project.

## Testing

API endpoints were tested using Postman.