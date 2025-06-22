# Oil & Gas Parts Project

This repository contains a FastAPI backend and a React frontend for a spare parts catalogue.

## Requirements

* Python 3.10+
* Node.js 20+
* PostgreSQL
* Docker and Docker Compose (optional)

## Local setup without Docker

### 1. Prepare environment variables

Create a `.env` file in the project root (see `.env.example`):

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=oilparts_db
```

### 2. Install backend dependencies

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 3. Initialize database and run backend

```bash
cd backend
python init_db.py          # create database if needed
python create_tables.py    # create tables
uvicorn main:app --reload
```

### 4. Install frontend dependencies and run

```bash
cd ../frontend
npm install
npm start
```

The frontend expects the API at `http://localhost:8000`. You can change this in `frontend/.env`.

## Running with Docker Compose

A ready to use configuration is located in `infra/docker-compose.yml`. It starts a PostgreSQL container and the backend service. Frontend can still be started locally with `npm start`.

```bash
cd infra
docker-compose up --build
```

Docker Compose reads variables from `.env` in the project root. Use `docker-compose down` to stop the containers.
