from typing import Union
from sqlalchemy import Column, Integer, TEXT, BOOLEAN
from app.infrastructure.dtos import BaseDto
from app.domain.entitys.todo_entity import TodoEntity


class TodoDto(BaseDto):
    """
    ToDoのDTOクラス

    Attributes:
        user_id: ユーザーID
        title: タイトル
        is_done: 完了フラグ
    """

    __tablename__ = "todo"

    user_id: Union[int, Column] = Column(Integer, nullable=False)
    title: Union[str, Column] = Column(TEXT, nullable=False)
    is_done: Union[bool, Column] = Column(BOOLEAN, nullable=False, default=False)

    @staticmethod
    def from_entity(todo_entity: TodoEntity) -> "TodoDto":
        return TodoDto(
            id=todo_entity.id,
            created_at=todo_entity.created_at,
            updated_at=todo_entity.updated_at,
            user_id=todo_entity.user_id,
            title=todo_entity.title,
            is_done=todo_entity.is_done,
        )

    def to_entity(self) -> TodoEntity:
        return TodoEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            user_id=self.user_id,
            title=self.title,
            is_done=self.is_done,
        )
