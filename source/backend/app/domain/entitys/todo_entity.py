from datetime import datetime
from typing import ClassVar
from dataclasses import dataclass
from abc import ABC, abstractmethod
from app.domain.entitys import BaseEntity
from app.domain.exceptions import ValueObjectValidError


class TodoEntity(BaseEntity):
    """
    ToDoのエンティティクラス

    Attributes:
        user_id: ユーザーID
        title: タイトル
        is_done: 完了フラグ
    """

    @dataclass(frozen=True)
    class UserId:
        """
        UserIdのValueObject
        """

        value: str

        def __init__(self, value: str):
            """
            Args:
                value: 値
            """
            if value == 0:
                raise ValueObjectValidError("ユーザーIDが不正です。")

            object.__setattr__(self, "value", value)

    @dataclass(frozen=True)
    class Title:
        """
        タイトルのValueObject
        """

        value: str

        MIN_LENGTH: ClassVar[int] = 1

        def __init__(self, value: str):
            """
            Args:
                value: 値
            """
            length: int = len(value)
            if length < self.MIN_LENGTH:
                raise ValueObjectValidError("タイトルが短すぎます。")

            object.__setattr__(self, "value", value)

    def __init__(
        self,
        id: int = None,
        created_at: datetime = None,
        updated_at: datetime = None,
        user_id: int = 0,
        title: str = "",
        is_done: str = False,
    ):
        """
        Args:
            id: 主キー
            created_at: 作成日時
            updated_at: 更新日時
            user_id: ユーザーID
            title: タイトル
            is_done: 完了フラグ
        """
        BaseEntity.__init__(self, id, created_at, updated_at)
        self.user_id: int = user_id
        self.title: str = title
        self.is_done: bool = is_done

    @staticmethod
    def create(user_id: int, title: str) -> "TodoEntity":
        """
        TodoEntityの作成

        Args:
            user_id: ユーザーID
            title: タイトル
        """
        return TodoEntity(
            user_id=TodoEntity.UserId(user_id).value,
            title=TodoEntity.Title(title).value,
            is_done=False,
        )


class ITodoRepository(ABC):
    """
    Todoのリポジトリインターフェース
    """

    @abstractmethod
    def insert(self, todo_entity: TodoEntity) -> TodoEntity:
        raise NotImplementedError

    @abstractmethod
    def find_all(self, user_id: int) -> list[TodoEntity]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> TodoEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self, todo_entity: TodoEntity) -> TodoEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        raise NotImplementedError
