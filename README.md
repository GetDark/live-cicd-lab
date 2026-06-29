[English](#english) | [Русский](#русский)

---

<a name="english"></a>
# live-cicd-lab

A FastAPI application with a complete end-to-end CI/CD pipeline on GitHub Actions: lint → test → build → push to GHCR → deploy to VPS via SSH → restart.

## Pipeline

```
push to main
    │
    ├─ lint      ruff check + ruff format + mypy
    │       │
    │       └─ test      pytest
    │               │
    │               └─ build     Docker image (no push on PR)
    │                       │
    │                       └─ push      GHCR (main only)
    │                               │
    │                               └─ deploy    SSH → docker compose pull + up
    │                                       │
    │                                       └─ restart   docker compose restart
```

## Application

FastAPI + Redis. CORS configured for `agent.swiftstream.ru`.

- `GET /health` — health check

## Local Development

```bash
cp .env.example .env
docker compose up -d
```

## GitHub Secrets Required

| Secret | Description |
|--------|-------------|
| `SSH_HOST` | VPS IP address |
| `SSH_USER` | SSH username |
| `SSH_PRIVATE_KEY` | SSH private key |
| `SSH_PORT` | SSH port |

## Tech Stack

- Python 3.12 / FastAPI / Redis
- GitHub Actions CI/CD
- GHCR (GitHub Container Registry)
- ruff, mypy, pytest
- Docker + Docker Compose

---

<a name="русский"></a>
# live-cicd-lab

FastAPI-приложение с полным CI/CD-конвейером на GitHub Actions: lint → test → build → push в GHCR → деплой на VPS по SSH → перезапуск.

## Конвейер

```
push в main
    │
    ├─ lint      ruff check + ruff format + mypy
    │       │
    │       └─ test      pytest
    │               │
    │               └─ build     Docker-образ (без push на PR)
    │                       │
    │                       └─ push      GHCR (только main)
    │                               │
    │                               └─ deploy    SSH → docker compose pull + up
    │                                       │
    │                                       └─ restart   docker compose restart
```

## Приложение

FastAPI + Redis. CORS настроен для `agent.swiftstream.ru`.

- `GET /health` — проверка здоровья

## Локальная разработка

```bash
cp .env.example .env
docker compose up -d
```

## Необходимые GitHub Secrets

| Секрет | Описание |
|--------|----------|
| `SSH_HOST` | IP-адрес VPS |
| `SSH_USER` | SSH-пользователь |
| `SSH_PRIVATE_KEY` | Приватный SSH-ключ |
| `SSH_PORT` | SSH-порт |

## Технологический стек

- Python 3.12 / FastAPI / Redis
- GitHub Actions CI/CD
- GHCR (GitHub Container Registry)
- ruff, mypy, pytest
- Docker + Docker Compose
