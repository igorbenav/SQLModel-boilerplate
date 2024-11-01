from datetime import datetime
from typing import Optional
import uuid as uuid_pkg

from sqlmodel import SQLModel, Field
from pydantic import validator


class UserBase(SQLModel):
    name: str = Field(..., min_length=2, max_length=30, schema_extra={"example": "User Userson"})
    username: str = Field(..., min_length=2, max_length=20, regex="^[a-z0-9]+$", schema_extra={"example": "userson"})
    email: str = Field(..., schema_extra={"example": "user.userson@example.com"})


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    profile_image_url: str = Field("https://www.profileimageurl.com")
    hashed_password: str
    is_superuser: bool = Field(default=False)
    tier_id: Optional[int] = Field(default=None, foreign_key="tier.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
    uuid: uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4, primary_key=True)
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    is_deleted: bool = Field(default=False)


class UserRead(SQLModel):
    id: int
    name: str
    username: str
    email: str
    profile_image_url: str
    tier_id: Optional[int]


class UserCreate(UserBase):
    password: str = Field(..., regex="^.{8,}|[0-9]+|[A-Z]+|[a-z]+|[^a-zA-Z0-9]+$", schema_extra={"example": "Str1ngst!"})

    @validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        return value


class UserCreateInternal(UserBase):
    hashed_password: str


class UserUpdate(SQLModel):
    name: Optional[str] = Field(None, min_length=2, max_length=30)
    username: Optional[str] = Field(None, min_length=2, max_length=20, regex="^[a-z0-9]+$")
    email: Optional[str] = None
    profile_image_url: Optional[str] = None


class UserUpdateInternal(UserUpdate):
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class UserTierUpdate(SQLModel):
    tier_id: int


class UserDelete(SQLModel):
    is_deleted: bool
    deleted_at: datetime


class UserRestoreDeleted(SQLModel):
    is_deleted: bool
