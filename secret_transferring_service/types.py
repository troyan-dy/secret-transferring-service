from typing import Optional

from pydantic import BaseModel, Field


class CreateSecretRequest(BaseModel):
    expire: int = Field(..., ge=10, le=1000)
    message: str = Field(..., min_length=1, max_length=10000)
    password: int = Field(..., ge=999, lt=100000)


class CreateSecretResponse(BaseModel):
    expire: int
    token: str


class CheckSecretRequest(BaseModel):
    password: int


class CheckSecretResponse(BaseModel):
    message: Optional[str]
    success: bool = True
