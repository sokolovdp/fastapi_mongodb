from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie

from app.core.settings import MONGO_DB_URL
from app.models.task import Task


async def init_db():
    mongo_client = AsyncIOMotorClient(MONGO_DB_URL)
    await init_beanie(
        database=mongo_client.mydatabase,
        document_models=[Task],
    )
    assert Task.get_settings().name == "tasks"  # to confirm success
    await mongo_client.admin.command("ping")
