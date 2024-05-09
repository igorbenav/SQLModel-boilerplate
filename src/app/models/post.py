from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from uuid import uuid4


class PostBase(SQLModel):
    title: str = Field(..., min_length=2, max_length=30, schema_extra={"example": "This is my post"})
    text: str = Field(..., min_length=1, max_length=63206, schema_extra={"example": "This is the content of my post."})


class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_by_user_id: int = Field(foreign_key="user.id")
    media_url: Optional[str] = Field(default=None, regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", schema_extra={"example": "https://www.postimageurl.com"})
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    is_deleted: bool = Field(default=False)


class PostRead(PostBase):
    id: int
    created_by_user_id: int
    media_url: Optional[str]
    created_at: datetime


class PostCreate(PostBase):
    media_url: Optional[str] = Field(default=None, regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", schema_extra={"example": "https://www.postimageurl.com"})


class PostCreateInternal(PostCreate):
    created_by_user_id: int


class PostUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=2, max_length=30)
    text: Optional[str] = Field(default=None, min_length=1, max_length=63206)
    media_url: Optional[str] = Field(default=None, regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$")


class PostUpdateInternal(PostUpdate):
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class PostDelete(SQLModel):
    is_deleted: bool
    deleted_at: datetime
