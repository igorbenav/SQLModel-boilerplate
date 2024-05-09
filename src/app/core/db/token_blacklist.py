from datetime import datetime
from sqlmodel import SQLModel, Field

class TokenBlacklist(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, nullable=False)
    token: str = Field(index=True, nullable=False, unique=True)
    expires_at: datetime = Field(nullable=False)
