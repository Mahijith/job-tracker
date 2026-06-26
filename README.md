# Job Tracker API

![CI](https://github.com/Mahijith/job-tracker/actions/workflows/ci.yml/badge.svg)

A production-grade REST API for tracking job applications.
Built with FastAPI, PostgreSQL, SQLAlchemy, and Alembic.

## Features
- Full CRUD for job applications
- Filter by status and company name
- Pagination with skip/limit
- Input validation with Pydantic
- Alembic database migrations
- pytest suite with SQLite test DB
- GitHub Actions CI

## Tech stack
- FastAPI + uvicorn
- PostgreSQL + SQLAlchemy ORM
- Alembic migrations
- Pydantic v2
- pytest + httpx
- Docker Compose

## Running locally

```bash
# Start Postgres
docker-compose up -d

# Install dependencies
uv pip install -e .

# Run migrations
uv run alembic upgrade head

# Start API
uv run uvicorn app.main:app --reload
```

## API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /jobs | Create a job application |
| GET | /jobs | List all jobs (filterable) |
| GET | /jobs/{id} | Get one job |
| PATCH | /jobs/{id} | Update a job |
| DELETE | /jobs/{id} | Delete a job |

## Filtering