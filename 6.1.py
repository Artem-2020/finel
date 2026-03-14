from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Инициализация приложения
app = FastAPI(title="Todo API")


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int


tasks_db: List[Task] = []
counter: int = 0


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Получить список всех задач."""
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Получить задачу по ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Создать новую задачу."""
    global counter
    counter += 1
    new_task = Task(id=counter, **task.dict())
    tasks_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated: TaskCreate):
    """Обновить существующую задачу."""
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task = Task(id=task_id, **updated.dict())
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """Удалить задачу."""
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)