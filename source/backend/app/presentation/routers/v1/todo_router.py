from fastapi import APIRouter, Request
from app.presentation.controllers.todo_controller import TodoController
from app.service.models.todo_model import TodoCreateModel, TodoUpdateModel, TodoReadModel

router = APIRouter()


@router.get("/list/{user_id}", response_model=list[TodoReadModel])
async def get_list(request: Request, user_id: int):
    return TodoController.find_all(request=request, user_id=user_id)


@router.post("", response_model=TodoReadModel)
async def create(request: Request, data: TodoCreateModel):
    return TodoController.create_todo(request=request, data=data)


@router.put("", response_model=TodoReadModel)
async def update(request: Request, data: TodoUpdateModel):
    return TodoController.update_todo(request=request, data=data)


@router.put("/done/{id}", response_model=TodoReadModel)
async def done(request: Request, id: int):
    return TodoController.done_todo(request=request, id=id)


@router.delete("/{id}")
async def delete(request: Request, id: int):
    return TodoController.delete_todo(request=request, id=id)
