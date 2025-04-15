from app.models.task import Task


class TaskSchema(Task):
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "status": "pending",
            },
        },
        "extra": "forbid",
    }
