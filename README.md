# Library Management System

This project contains two separate applications:

- `cli/`: the original command-line library management system
- `backend/`: the FastAPI backend and SQLAlchemy database models

## Project Structure

```text
library_management_system/
|-- backend/
|   |-- models/
|   |-- __init__.py
|   |-- database.py
|   `-- main.py
|-- cli/
|   |-- database/
|   |-- modules/
|   |-- __init__.py
|   `-- main.py
|-- .gitignore
|-- README.md
`-- requirements.txt
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run CLI

Run this command from the project root:

```powershell
python -m cli.main
```

## Run Backend

Run this command from the project root:

```powershell
uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to view the API documentation.

The backend creates the local SQLite database file `library.db`.

## User Endpoints

The Swagger page contains these user endpoints:

```text
POST   /users/           Create a user
GET    /users/           View all users
GET    /users/{user_id}  View one user
PUT    /users/{user_id}  Update a user
DELETE /users/{user_id}  Deactivate a user
```

Example body for `POST /users/`:

```json
{
  "name": "Sri Raja",
  "email": "sri@example.com",
  "phone": "9876543210",
  "address": "Chennai",
  "age": 20,
  "role": "member",
  "membership_type": "basic"
}
```
