from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from app.core.settings import MAX_PAGE_SIZE, PAGE_SIZE
from app.models.task import Task
from app.schemas.task import TaskSchema

api_router = APIRouter()


@api_router.post(
    "/",
    response_description="Task data added into the database",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskSchema,
)
async def create_task(task: TaskSchema):
    task_data = task.model_dump()
    return await Task(**task_data).insert()


@api_router.get(
    "/",
    response_description="Tasks retrieved",
    response_model=List[TaskSchema],
)
async def get_tasks(
    task_status: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE),
):
    query = Task.find_all()
    if task_status:
        query = query.find(Task.status == task_status)

    paginated_query = query.skip((page - 1) * page_size).limit(page_size)

    return await paginated_query.to_list()


@api_router.get(
    "/{task_id}",
    response_description="Task data retrieved",
    response_model=TaskSchema,
)
async def retrieve_task(task_id: str):
    task = await Task.get(document_id=task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@api_router.put(
    "/{task_id}",
    response_description="Task data updated in the database",
    response_model=TaskSchema,
)
async def update_task(task_id: str, task_update: TaskSchema):
    task = await Task.get(document_id=task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    update_data = task_update.model_dump(exclude={"id", "created_at"}, exclude_unset=True)
    await task.update({"$set": update_data})

    await task.save()
    return task


@api_router.patch(
    "/{task_id}",
    response_description="Task data updated in the database",
    response_model=TaskSchema,
)
async def partial_update_task(task_id: str, task_update: TaskSchema):
    task = await Task.get(document_id=task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    update_data = task_update.model_dump(exclude={"id", "created_at"}, exclude_unset=True)
    await task.update({"$set": update_data})

    await task.save()
    return task


@api_router.delete(
    "/{task_id}",
    response_description="Task data deleted from the database",
)
async def delete_task(task_id: str):
    deleted_task = await Task.get(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    await deleted_task.delete()
    return {"message": "Task deleted successfully"}
