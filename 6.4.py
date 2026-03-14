import pytest
from fastapi.testclient import TestClient
from todo_api import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Test Task", "description": "Test desc"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test desc"
    assert data["completed"] is False
    assert "id" in data
    return data["id"]

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_get_task():
    create_resp = client.post("/tasks", json={"title": "Get Test"})
    task_id = create_resp.json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Get Test"

def test_get_task_not_found():
    response = client.get("/tasks/99999")
    assert response.status_code == 404

def test_update_task():
    create_resp = client.post("/tasks", json={"title": "Update Me"})
    task_id = create_resp.json()["id"]
    update_data = {"title": "Updated", "description": "New desc", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated"
    assert data["description"] == "New desc"
    assert data["completed"] is True

def test_delete_task():
    create_resp = client.post("/tasks", json={"title": "Delete Me"})
    task_id = create_resp.json()["id"]
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 204
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404