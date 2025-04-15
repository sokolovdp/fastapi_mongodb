# FastAPI & MongoDB demo implementation

This is a demo FastAPI & MongoDB  project to provide APIs for managing user tasks with pytest test cases, and online OpenAPI/Swagger documentation

## Features

- **CRUD operations for tasks:** Create, read, update, and delete tasks.
- **Data validation:** Uses Pydantic schemas for data validation.
- **MongoDB integration:** Uses Beanie ODM for asynchronous interaction with MongoDB.
- **Pagination:** Supports paginated retrieval of tasks.
- **Filtering:** Allows filtering tasks by status.
- **Dockerized:** Includes Dockerfile and docker-compose for easy deployment.
- **Testing:** Includes pytest tests with coverage reporting.

## API Endpoints

- **POST `/api/`**: Create a new task.
- **GET `/api/`**: Retrieve a list of tasks (with optional filtering and pagination).
- **GET `/api/{task_id}`**: Retrieve a single task by ID.
- **PUT `/api/{task_id}`**: Update a task (full update).
- **PATCH `/api/{task_id}`**: Partially update a task.
- **DELETE `/api/{task_id}`**: Delete a task.

## OpenAPI/Swagger Endpoint

- **GET `/docs/`**: OpenAPI
- **GET `/redoc/`**: ReDoc

## Prerequisites

- Docker and Docker Compose
- Make (optional, for testing & development commands)

## Quick Start

1. Clone the repository from GitHub:
```bash
git clone https://github.com/sokolovdp/fastapi_mongodb
cd fastapi_mongodb
```
3. Start the services:
```bash
docker-compose up -d
```
4. Open a web browser and navigate to http://localhost:8000/api/docs/


## Environment Variables

All variables have default values, but can be customized through `.env` file:

- `MONGO_DB_HOST`: Database host (default: mongodb)
- `MONGO_DB_DATABASE`: Database name (default: task_db)


## Development

The project includes development tools (to run tests you install tests dependencies):

```bash
# Format code
make pretty

# Run linting
make lint
```

## Project Structure

```
.
├── app/                 # Main application
│   ├── api/             # Routers
│   │   └── routers.py           # API views
│   ├── core/             # Database models
│   │   └── routers.py           # API views
│   ├── serializers.py     # DRF serializers
│   └── tasks.py           # Celery tasks
├── tests/                 # Folder with unittests
│   ├── conftest.py        # Pytest config
│   └── test_routes.py     # Tests
├── docker-compose.yml     # Docker services configuration
├── Dockerfile             # Service build instructions
├── requirements.txt       # Application dependencies
├── requirements_prod.txt  # Python dependencies, required in production
├── requirements_test.txt  # Python dependencies, required for testing
├── requirements_lint.txt  # Python dependencies, required for linting
└── Makefile               # Development commands
```

## Testing

The project uses pytest framework. Run tests with:

```bash
make test
```
