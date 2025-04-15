import pytest

from fastapi import status

from app.models.task import Task


@pytest.mark.asyncio
async def test_list_tasks(client):
    """
    Test the GET / endpoint to list tasks.
    """
    # Pre-create a task
    await Task(title="title", description="description", _id="1").insert()

    # Test GET /api endpoint
    response = await client.get("/api/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "title"
    assert data[0]["description"] == "description"
    assert data[0]["_id"] == "1"


@pytest.mark.asyncio
async def test_create_task(client):
    response = await client.post(
        "/api/",
        json={
            "title": "Write tests",
            "description": "Write unit tests for FastAPI router",
            "status": "pending",
            "id": "1",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Write tests"


@pytest.mark.asyncio
async def test_create_task_with_extra(client):
    response = await client.post(
        "/api/",
        json={
            "title": "Write tests",
            "description": "Write unit tests for FastAPI router",
            "status": "pending",
            "id": "1",
            "extra": "forbid",
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text


@pytest.mark.asyncio
async def test_list_tasks_by_status(client):
    # Pre-create a task
    await Task(title="title", description="description", _id="1").insert()
    await Task(title="title", description="description", _id="2").insert()
    await Task(title="title", description="description", _id="3", status="done").insert()

    response = await client.get("/api/?task_status=done")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["status"] == "done"


@pytest.mark.asyncio
async def test_get_task_by_id(client):
    task = await Task(title="title", description="description", _id="1").insert()

    response = await client.get(f"/api/{task.id}")
    assert response.status_code == 200, response.text
    updated = response.json()

    assert updated["_id"] == task.id, str(updated)
    assert updated["title"] == "title"
    assert updated["description"] == "description"


@pytest.mark.asyncio
async def test_put_update_by_task_by_id(client):
    task = await Task(title="title", description="description", _id="1").insert()

    response = await client.put(
        f"/api/{task.id}",
        json={
            "_id": task.id,
            "title": "New Title",
            "description": "Updated",
            "status": "done",
        },
    )
    assert response.status_code == 200, response.text
    updated = response.json()
    assert updated["title"] == "New Title"
    assert updated["status"] == "done"


@pytest.mark.asyncio
async def test_patch_update_by_task_by_id(client):
    task = await Task(title="title", description="description", _id="1").insert()

    response = await client.patch(
        f"/api/{task.id}",
        json={
            "_id": task.id,
            "title": "New Title",
            "description": "Updated",
            "status": "done",
        },
    )
    assert response.status_code == 200, response.text
    updated = response.json()
    assert updated["title"] == "New Title"
    assert updated["status"] == "done"


@pytest.mark.asyncio
async def test_delete_task(client):
    task = await Task(title="title", description="description", _id="1").insert()

    response = await client.delete(f"/api/{task.id}")
    assert response.status_code == 200, response.text
    assert response.json()["message"] == "Task deleted successfully"

    assert await Task.get(task.id) is None


@pytest.mark.asyncio
async def test_get_missing_task_returns_404(client):
    response = await client.get("/api/6627fe259f1704d89c80e144")
    assert response.status_code == 404, response.text


@pytest.mark.asyncio
async def test_update_missing_task_returns_404(client):
    response = await client.put(
        "/api/6627fe259f1704d89c80e144",
        json={"_id": "1", "title": "Oops", "description": "This won't update", "status": "pending"},
    )
    assert response.status_code == 404, response.text
