from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_db
from app.services.redis import get_redis

router = APIRouter(prefix="/api/v1")

PIPELINE_STAGES = ["lint", "test", "build", "push", "deploy", "restart"]


@router.get("/ping")
async def ping() -> dict[str, str]:
    return {"message": "pong"}


@router.get("/db-check")
async def db_check(db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as exc:
        return {"status": "error", "database": str(exc)}


@router.get("/redis-check")
async def redis_check() -> dict[str, str]:
    try:
        redis = await get_redis()
        await redis.ping()
        return {"status": "ok", "redis": "connected"}
    except Exception as exc:
        return {"status": "error", "redis": str(exc)}


@router.get("/status")
async def status(db: AsyncSession = Depends(get_db)) -> dict:
    pg_status = "connected"
    try:
        await db.execute(text("SELECT 1"))
    except Exception:
        pg_status = "error"

    redis_status = "connected"
    try:
        redis = await get_redis()
        await redis.ping()
    except Exception:
        redis_status = "error"

    return {
        "api": "online",
        "postgresql": pg_status,
        "redis": redis_status,
        "nginx": settings.nginx_status,
        "last_deploy": settings.last_deploy,
        "current_image": settings.current_image,
        "git_sha": settings.git_sha,
        "pipeline": [{"stage": s, "status": "success"} for s in PIPELINE_STAGES],
    }
