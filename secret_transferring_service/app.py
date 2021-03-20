import hashlib
import os
from uuid import uuid4

import uvicorn
from aioredis.commands import Redis
from fastapi import APIRouter, Depends, FastAPI, Request
from pydantic import BaseSettings, RedisDsn
from starlette.responses import PlainTextResponse

from secret_transferring_service.redis_state import create_redis, get_redis_from_app, shutdown_redis
from secret_transferring_service.types import (
    CheckSecretRequest,
    CheckSecretResponse,
    CreateSecretRequest,
    CreateSecretResponse,
)
from secret_transferring_service.utils import create_key

api_router = APIRouter()


class Settings(BaseSettings):
    redis_dsn: RedisDsn


@api_router.get("/ping")
async def ping() -> PlainTextResponse:
    return PlainTextResponse("pong")


@api_router.post("/create_secret", response_model=CreateSecretResponse)
async def create_secret(request: Request, secret_data: CreateSecretRequest, redis: Redis = Depends(get_redis_from_app)):
    token = str(uuid4())
    key = create_key(password=secret_data.password, token=token)
    await redis.set(key=key, value=secret_data.message)
    await redis.expire(key=key, timeout=secret_data.expire)
    return CreateSecretResponse(token=token, expire=secret_data.expire)


@api_router.post("/check_secret/{token}", response_model=CheckSecretResponse)
async def check_secret(
    request: Request, token: str, secret_data: CheckSecretRequest, redis: Redis = Depends(get_redis_from_app)
):
    key = create_key(password=secret_data.password, token=token)
    if message := await redis.get(key=key):
        redis.delete(key=key)
        return CheckSecretResponse(message=message)
    else:
        return CheckSecretResponse(success=False)


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    app.config = Settings()
    app.router.add_event_handler("startup", create_redis(app))
    app.router.add_event_handler("shutdown", shutdown_redis(app))

    return app


app = create_app()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app=app, host="0.0.0.0", port=port)
