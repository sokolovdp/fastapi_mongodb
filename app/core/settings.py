import os

PROJECT_NAME = "fastapi_mongodb"
VERSION = "0.1.1"

MONGO_DB_HOST = os.environ.get("MONGO_DB_HOST", "localhost")
MONGO_DB_PORT = os.environ.get("MONGO_DB_PORT", 27017)
MONGO_DB_USERNAME = os.environ.get("MONGO_DB_USERNAME", None)
MONGO_DB_PASSWORD = os.environ.get("MONGO_DB_ROOT_PASSWORD", None)
MONGO_DB_DATABASE = os.environ.get("MONGO_DB_ROOT_DATABASE", "task_db")

PAGE_SIZE = os.environ.get("PAGE_SIZE", 20)
MAX_PAGE_SIZE = os.environ.get("PAGE_SIZE", 100)


def create_mongo_url() -> str:
    """Creates the MongoDB connection URL."""
    if MONGO_DB_USERNAME and MONGO_DB_PASSWORD:
        return f"mongodb://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}/{MONGO_DB_DATABASE}"
    else:
        return f"mongodb://{MONGO_DB_HOST}:{MONGO_DB_PORT}/{MONGO_DB_DATABASE}"


MONGO_DB_URL = create_mongo_url()
