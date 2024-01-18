from app.domain.entitys.user_entity import UserEntity
from app.domain.entitys.todo_entity import TodoEntity
from app.infrastructure.repositorys.user_repository import UserRepository
from app.infrastructure.repositorys.todo_repository import TodoRepository
from app.service.models.todo_model import TodoCreateModel, TodoUpdateModel, TodoReadModel
from app.domain.exceptions import ValueObjectValidError
from app.service.exceptions import (
    ValidError,
    NotFoundError,
)


class TodoUseCase:
    """
    Todoのユースケースクラス

    Attributes:
        db_session: DBセッション
    """

    def __init__(self, db_session):
        """
        Args:
            db_session: DBセッション
        """
        self.db_session = db_session
        self.user_repository = UserRepository(db_session=self.db_session)
        self.todo_repository = TodoRepository(db_session=self.db_session)

    def create_todo(self, data: TodoCreateModel) -> TodoReadModel:
        """
        Todoの作成

        Args:
            data: Todo作成モデル
        Returns:
            TodoReadModel: 作成したTodoの参照モデル
        """
        try:
            # ユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_id(id=data.user_id)
            if not user_entity:
                raise NotFoundError("ユーザーが存在しません。")

            # Todoエンティティを作成
            new_todo_entity: TodoEntity = TodoEntity.create(user_id=user_entity.id, title=data.title)

            # Todoの挿入
            created_todo_entity: TodoEntity = self.todo_repository.insert(todo_entity=new_todo_entity)

            # Todo参照モデルへ変換
            result: TodoReadModel = TodoReadModel(
                id=created_todo_entity.id,
                created_at=created_todo_entity.created_at,
                updated_at=created_todo_entity.updated_at,
                user_id=created_todo_entity.user_id,
                title=created_todo_entity.title,
                is_done=created_todo_entity.is_done,
            )

        except ValueObjectValidError as e:
            raise ValidError(e)
        except Exception:
            raise

        return result

    def find_all(self, user_id: int) -> list[TodoReadModel]:
        """
        Todoの全件取得

        Args:
            user_id: ユーザーID
        Returns:
            list[TodoReadModel]: 取得したTodoの参照モデルリスト
        """
        try:
            # ユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_id(id=user_id)
            if not user_entity:
                raise NotFoundError("ユーザーが存在しません。")

            # Todoを全件取得
            todo_entity_list: list[TodoEntity] = self.todo_repository.find_all(user_id=user_entity.id)

            # Todo参照モデルへ変換
            result: list[TodoEntity] = []
            for todo_entity in todo_entity_list:
                todo_read_model: TodoReadModel = TodoReadModel(
                    id=todo_entity.id,
                    created_at=todo_entity.created_at,
                    updated_at=todo_entity.updated_at,
                    user_id=todo_entity.user_id,
                    title=todo_entity.title,
                    is_done=todo_entity.is_done,
                )
                result.append(todo_read_model)
        except Exception:
            raise

        return result

    def update_todo(self, data: TodoUpdateModel) -> TodoReadModel:
        """
        Todoの更新

        Args:
            data: Todo更新モデル
        Returns:
            TodoReadModel: 更新したTodoの参照モデル
        """
        try:
            # 対象のTodoを取得
            todo_entity: TodoEntity = self.todo_repository.find_by_id(id=data.id)
            if not todo_entity:
                raise NotFoundError("Todoが存在しません。")

            # Todoの更新
            todo_entity.title = data.title
            updated_todo_entity: TodoEntity = self.todo_repository.update(todo_entity=todo_entity)

            # Todo参照モデルへ変換
            result: TodoReadModel = TodoReadModel(
                id=updated_todo_entity.id,
                created_at=updated_todo_entity.created_at,
                updated_at=updated_todo_entity.updated_at,
                user_id=updated_todo_entity.user_id,
                title=updated_todo_entity.title,
                is_done=updated_todo_entity.is_done,
            )

        except Exception:
            raise

        return result

    def done_todo(self, id: int) -> TodoReadModel:
        """
        Todoの完了

        Args:
            id: TodoID
        Returns:
            TodoReadModel: 完了したTodoの参照モデル
        """
        try:
            # 対象のTodoを取得
            todo_entity: TodoEntity = self.todo_repository.find_by_id(id=id)
            if not todo_entity:
                raise NotFoundError("Todoが存在しません。")

            # Todoの完了
            todo_entity.is_done = True
            updated_todo_entity: TodoEntity = self.todo_repository.update(todo_entity=todo_entity)

            # Todo参照モデルへ変換
            result: TodoReadModel = TodoReadModel(
                id=updated_todo_entity.id,
                created_at=updated_todo_entity.created_at,
                updated_at=updated_todo_entity.updated_at,
                user_id=updated_todo_entity.user_id,
                title=updated_todo_entity.title,
                is_done=updated_todo_entity.is_done,
            )

        except Exception:
            raise

        return result

    def delete_todo(self, id: int):
        """
        Todoの削除

        Args:
            id: TodoID
        """
        try:
            # Todoの削除
            self.todo_repository.delete_by_id(id=id)

        except Exception:
            raise
