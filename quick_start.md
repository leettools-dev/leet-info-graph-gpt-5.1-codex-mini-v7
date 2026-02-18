# Quick Start

## Environment Requirements
- `PYTHON_ENV`: should be set to `development` or `production`.
- `GOOGLE_OAUTH_CLIENT_ID`: client ID for Google OAuth (replace with your credential).
- `GOOGLE_OAUTH_CLIENT_SECRET`: client secret for Google OAuth (replace with your secret).
- `DATABASE_URL`: Postgres connection string, e.g., `postgresql://user:password@localhost:5432/info_graph`.
- `REDIS_URL`: Redis connection string for queues, e.g., `redis://localhost:6379/0`.

Store secrets in a `.env` file or use your orchestration secrets manager. Do not commit `.env`.

## Startup Scripts
1. Start services:
   ```bash
   ./start.sh
   ```
   - Stops any existing backend/frontend recorded in `pids/`.
   - Logs backend output to `logs/backend.log` and frontend output to `logs/frontend.log`.
   - Writes process IDs to `pids/backend.pid` and `pids/frontend.pid`.

2. Stop services:
   ```bash
   ./stop.sh
   ```
   - Terminates processes tracked in `pids/` and removes the PID files.

## Frontend Access
After `start.sh` completes, it prints:
```
Backend running at http://localhost:8000
Frontend running at http://localhost:3000
```

## Docker Setup
- Each component runs inside a dedicated container defined in the `docker-compose.yml` file.
- Build images via:
  ```bash
  docker compose build
  ```
- Launch the platform with:
  ```bash
  docker compose up
  ```
- Container logs stream to the console; see `logs/` for local script logs.

## CLI Intro
A utility CLI will coordinate backend/frontend/service automation in future iterations. For now, use the provided `start.sh`/`stop.sh` to manage services.
