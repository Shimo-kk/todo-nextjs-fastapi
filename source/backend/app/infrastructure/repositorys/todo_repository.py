from app.infrastructure.dtos.todo_dto import TodoDto
from app.domain.entitys.todo_entity import TodoEntity, ITodoRepository


class TodoRepository(ITodoRepository):
    """
    Todoのリポジトリクラス

    Attributes:
        db_session: DBセッション
    """

    def __init__(self, db_session):
        """
        Args:
            db_session: DBセッション
        """
        self.db_session = db_session

    def insert(self, todo_entity: TodoEntity) -> TodoEntity:
        """
        Todoの挿入

        Args:
            todo_entity: 挿入するTodoのエンティティ
        Returns:
            TodoEntity: 挿入したTodoのエンティティ
        """
        todo_dto: TodoDto = TodoDto.from_entity(todo_entity)
        self.db_session.add(todo_dto)
        self.db_session.flush()
        self.db_session.refresh(todo_dto)

        result: TodoEntity = todo_dto.to_entity()
        return result

    def find_all(self, user_id: int) -> list[TodoEntity]:
        """
        ユーザーIDでの全件取得

        Args:
            user_id: ユーザーID
        Returns:
            list[TodoEntity]: 取得したTodoのエンティティのリスト
        """
        todo_dto_list: list[TodoDto] = self.db_session.query(TodoDto).filter_by(user_id=user_id).order_by(TodoDto.id)

        result: list[TodoEntity] = []
        for todo_dto in todo_dto_list:
            result.append(todo_dto.to_entity())

        return result

    def find_by_id(self, id: int) -> TodoEntity:
        """
        主キーでの取得

        Args:
            id: 主キー
        Returns:
            TodoEntity: 取得したTodoのエンティティ
        """
        todo_dto: TodoDto = self.db_session.query(TodoDto).filter_by(id=id).first()
        if not todo_dto:
            return None

        result: TodoEntity = todo_dto.to_entity()
        return result

    def update(self, todo_entity: TodoEntity) -> TodoEntity:
        """
        Todoの更新

        Args:
            todo_entity: 更新するTodoのエンティティ
        Returns:
            TodoEntity: 更新したTodoのエンティティ
        """
        todo_dto: TodoDto = TodoDto.from_entity(todo_entity)
        _todo: TodoDto = self.db_session.query(TodoDto).filter_by(id=todo_dto.id).first()
        _todo.user_id = todo_dto.user_id
        _todo.title = todo_dto.title
        _todo.is_done = todo_dto.is_done
        self.db_session.flush()

        result: TodoEntity = _todo.to_entity()
        return result

    def delete_by_id(self, id: int) -> None:
        """
        主キーでの削除

        Args:
            id: 主キー
        """
        self.db_session.query(TodoDto).filter_by(id=id).delete()

        return None
