from datetime import datetime, timezone

from beanie import Document, Indexed
from pydantic import Field


class Task(Document):
    id: Indexed(str) = Field(..., alias="_id")  # Use alias for MongoDB's _id
    title: Indexed(str) = Field(..., max_length=100)
    description: str = None
    status: str = "pending"
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))

    class Settings:
        name = "tasks"
