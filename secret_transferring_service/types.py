from typing import Optional

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings

MAX_EXPIRE = 10000
MAX_MESSAGE_LENGTH = 10000
MIN_PASSWORD_LENGTH = 5
MAX_PASSWORD_LENGTH = 12


class Settings(BaseSettings):
    redis_dsn: str = Field("redis://redis", validation_alias="STACKHERO_REDIS_URL_TLS")


class CreateSecretRequest(BaseModel):
    expire: int = Field(..., ge=10, le=MAX_EXPIRE)
    message: str = Field(..., min_length=1, max_length=MAX_MESSAGE_LENGTH)
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
            raise ValueError("Value must be longer then 4 and shorter then 12")
        try:
            [int(digit) for digit in password]
        except Exception:
            raise ValueError("Value must be valid sting of ints, like 04123")
        return password


class CreateSecretResponse(BaseModel):
    expire: int
    token: str


class CheckSecretRequest(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
            raise ValueError("Value must be longer then 4 and shorter then 12")
        try:
            [int(digit) for digit in password]
        except Exception:
            raise ValueError("Value must be valid sting of ints, like 04123")
        return password


class CheckSecretResponse(BaseModel):
    message: Optional[str] = None
    success: bool = True
