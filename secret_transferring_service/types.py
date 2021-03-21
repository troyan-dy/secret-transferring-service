from typing import Optional

from pydantic import BaseModel, BaseSettings, Field, validator


class Settings(BaseSettings):
    redis_dsn: str = Field("redis://redis", env="STACKHERO_REDIS_URL_TLS")


class CreateSecretRequest(BaseModel):
    expire: int = Field(..., ge=10, le=10000)
    message: str = Field(..., min_length=1, max_length=10000)
    password: str

    @validator("password", always=True)
    def validate_password(cls, value: str) -> str:
        if len(value) < 5 or len(value) > 12:
            raise ValueError("Value must be longer then 4 and shorter then 12")
        try:
            [int(v) for v in value]
            return value
        except Exception:
            raise ValueError("Value must be valid sting of ints, like 04123")


class CreateSecretResponse(BaseModel):
    expire: int
    token: str


class CheckSecretRequest(BaseModel):
    password: str

    @validator("password", always=True)
    def validate_password(cls, value: str) -> str:
        if len(value) < 5 or len(value) > 12:
            raise ValueError("Value must be longer then 4 and shorter then 12")
        try:
            [int(v) for v in value]
            return value
        except Exception:
            raise ValueError("Value must be valid sting of ints, like 04123")


class CheckSecretResponse(BaseModel):
    message: Optional[str]
    success: bool = True
