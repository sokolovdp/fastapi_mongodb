from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import api_router
from app.core import settings
from app.core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup
    await init_db()
    print("✅ Beanie started")
    yield
    # On shutdown
    print("🛑 Beanie stopped")


app = FastAPI(lifespan=lifespan, title=settings.PROJECT_NAME, version=settings.VERSION)

# Mount API routes
app.include_router(api_router, prefix="/api")
