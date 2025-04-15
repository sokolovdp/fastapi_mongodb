import pytest
import pytest_asyncio
from httpx import AsyncClient

from app.core.database import init_db
from app.main import app
from app.models.task import Task

pytestmark = pytest.mark.asyncio  # Set loop_scope to function


@pytest_asyncio.fixture(scope="function", autouse=True)
async def initialize_db():
    """
    Fixture to initialize MongoDB connection once per test session.
    """
    await init_db()
    yield


@pytest_asyncio.fixture(scope="function", autouse=True)
async def setup_and_teardown(initialize_db):
    """
    Fixture to clean the Task collection before and after each test.
    """
    await Task.find_all().delete()
    yield
    await Task.find_all().delete()


@pytest_asyncio.fixture
async def client():
    """
    Fixture to provide an AsyncClient for testing FastAPI endpoints.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
