from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


def sanitize_path(path: str) -> str:
    return path.strip("/").replace("/", "_")


class RateLimitBase(SQLModel):
    path: str = Field(..., schema_extra={"example": "users"})
    limit: int = Field(..., schema_extra={"example": 5})
    period: int = Field(..., schema_extra={"example": 60})

    @classmethod
    def validate_path(cls, v: str) -> str:
        return sanitize_path(v)


class RateLimit(RateLimitBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tier_id: int = Field(foreign_key="tier.id")
    name: Optional[str] = Field(default=None, schema_extra={"example": "users:5:60"})
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
    updated_at: Optional[datetime] = None


class RateLimitRead(RateLimitBase):
    id: int
    tier_id: int
    name: str


class RateLimitCreate(RateLimitBase):
    name: Optional[str] = Field(default=None, schema_extra={"example": "api_v1_users:5:60"})


class RateLimitCreateInternal(RateLimitCreate):
    tier_id: int


class RateLimitUpdate(SQLModel):
    path: Optional[str] = Field(default=None)
    limit: Optional[int] = None
    period: Optional[int] = None
    name: Optional[str] = None

    @classmethod
    def validate_path(cls, v: Optional[str]) -> Optional[str]:
        return sanitize_path(v) if v is not None else None


class RateLimitUpdateInternal(RateLimitUpdate):
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class RateLimitDelete(SQLModel):
    pass
