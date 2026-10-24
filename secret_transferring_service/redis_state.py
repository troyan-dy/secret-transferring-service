from functools import partial
from typing import Awaitable, Callable

from fastapi import FastAPI, Request
from redis.asyncio import Redis

from secret_transferring_service.types import Settings


async def get_redis_from_app(request: Request) -> Redis:
    return request.app.redis  # type: ignore


async def get_cache_backend(config: Settings) -> Redis:
    connection = Redis.from_url(config.redis_dsn, decode_responses=True)
    return connection


async def startup_hook(app: FastAPI) -> None:
    app.redis = await get_cache_backend(app.config)  # type: ignore


async def shutdown_hook(app: FastAPI) -> None:
    if app.redis is not None:  # type: ignore
        await app.redis.aclose()  # type: ignore


def create_redis(app: FastAPI) -> Callable[[], Awaitable[None]]:
    return partial(startup_hook, app)


def shutdown_redis(app: FastAPI) -> Callable[[], Awaitable[None]]:
    return partial(shutdown_hook, app)
