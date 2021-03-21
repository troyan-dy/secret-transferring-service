from aioredis import create_redis_pool
from aioredis.commands import Redis
from fastapi import FastAPI, Request

from secret_transferring_service.types import Settings


async def get_redis_from_app(request: Request) -> Redis:
    return request.app.redis


async def get_cache_backend(config: Settings) -> Redis:
    connection = await create_redis_pool(config.redis_dsn)
    return connection


def create_redis(app: FastAPI):  # type: ignore
    async def startup_hook() -> None:
        app.redis = await get_cache_backend(app.config)  # type: ignore

    return startup_hook


def shutdown_redis(app: FastAPI):  # type: ignore
    async def shutdown_hook() -> None:
        if app.redis is not None:  # type: ignore
            app.redis.close()  # type: ignore
            await app.redis.wait_closed()  # type: ignore

    return shutdown_hook
