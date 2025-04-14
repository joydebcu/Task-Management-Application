# Task Management API

A RESTful API built with Django and Django REST Framework that enables task management functionality, including task creation, assignment, and retrieval.

## Features

- Create tasks with name, description, and other attributes
- Assign tasks to one or multiple users
- Retrieve all tasks assigned to a specific user
- Complete user and task management

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/tasks/create/` | POST | Create a new task |
| `/api/tasks/assign/` | POST | Assign a task to one or more users |
| `/api/users/<user_id>/tasks/` | GET | Get all tasks assigned to a specific user |

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-management-api.git
   cd task-management-api
   ```

2. Create and activate a virtual environment:
   ```bash 
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root based on `.env.dev`:
   ```bash
   cp .env.dev .env
   ```
   Edit `.env` with your own secret key and other configuration settings.

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

## Sample API Requests and Responses

### Create a Task

**Request:**
```http
POST /api/tasks/create/
Content-Type: application/json
Authorization: Basic <credentials>

{
    "name": "Update documentation",
    "description": "Update API documentation for the project",
    "task_type": "WORK",
    "status": "PENDING"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Update documentation",
    "description": "Update API documentation for the project",
    "task_type": "WORK",
    "status": "PENDING"
}
```

### Assign a Task to Users

**Request:**
```http
POST /api/tasks/assign/
Content-Type: application/json
Authorization: Basic <credentials>

{
    "task_id": 1,
    "user_ids": [1, 2]
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Update documentation",
    "description": "Update API documentation for the project",
    "created_at": "2025-04-14T10:00:00Z",
    "task_type": "WORK",
    "completed_at": null,
    "status": "PENDING",
    "assigned_users": [
        {
            "id": 1,
            "name": "User One",
            "email": "user1@example.com",
            "mobile": "1234567890"
        },
        {
            "id": 2,
            "name": "User Two",
            "email": "user2@example.com",
            "mobile": "0987654321"
        }
    ]
}
```

### Get Tasks for a User

**Request:**
```http
GET /api/users/1/tasks/
Authorization: Basic <credentials>
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "Update documentation",
        "description": "Update API documentation for the project",
        "created_at": "2025-04-14T10:00:00Z",
        "task_type": "WORK",
        "completed_at": null,
        "status": "PENDING",
        "assigned_users": [
            {
                "id": 1,
                "name": "User One",
                "email": "user1@example.com",
                "mobile": "1234567890"
            },
            {
                "id": 2,
                "name": "User Two",
                "email": "user2@example.com",
                "mobile": "0987654321"
            }
        ]
    }
]
```

## Test Credentials

After setting up the project and creating a superuser, you can use those credentials for testing the API endpoints, or create additional regular users through the Django admin interface at `/admin/`.

## Deploying to Production

1. Update the `.env` file with production settings:
   - Set `DEBUG=False`
   - Set `ALLOWED_HOSTS` to your domain
   - Generate a strong `SECRET_KEY`
   - Configure your database connection string

2. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

3. Run with Gunicorn:
   ```bash
   gunicorn task_management.wsgi:application --bind 0.0.0.0:8000
   ```

4. Set up a reverse proxy like Nginx to serve the application.

## Requirements File

Create a `requirements.txt` file with the following dependencies:

```
django==4.2.7
djangorestframework==3.14.0
python-dotenv==1.0.0
gunicorn==21.2.0
```

## Git Setup and Push Instructions

1. Initialize Git repository (if not already done):
   ```bash
   git init
   ```

2. Add files to Git:
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

3. Create a repository on GitHub, GitLab, or your preferred Git hosting service

4. Add the remote repository:
   ```bash
   git remote add origin https://github.com/yourusername/task-management-api.git
   ```

5. Push the code:
   ```bash
   git push -u origin master
   ```

Remember to add `.env` to your `.gitignore` file to avoid pushing sensitive information to your repository.
