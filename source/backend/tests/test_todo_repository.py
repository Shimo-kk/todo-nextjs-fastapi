from app.domain.entitys.todo_entity import TodoEntity, ITodoRepository
from app.infrastructure.repositorys.todo_repository import TodoRepository


def test_insert_ok(session):
    """
    Todoの挿入 正常
    """
    try:
        todo_repository: ITodoRepository = TodoRepository(session)

        new_todo_entity: TodoEntity = TodoEntity.create(user_id=1, title="test title")
        todo_repository.insert(todo_entity=new_todo_entity)
        session.commit()

        todo_entity: TodoEntity = todo_repository.find_by_id(id=4)
    except Exception:
        assert False

    assert todo_entity.id == 4
    assert todo_entity.created_at is not None
    assert todo_entity.updated_at is not None
    assert todo_entity.user_id == new_todo_entity.user_id
    assert todo_entity.title == new_todo_entity.title
    assert todo_entity.is_done is False


def test_find_all_ok(session):
    """
    Todoの全件取得 正常
    """
    try:
        todo_repository: ITodoRepository = TodoRepository(session)
        todo_entity_list: list[TodoEntity] = todo_repository.find_all(user_id=1)
    except Exception:
        assert False

    assert len(todo_entity_list) == 3
    assert todo_entity_list[0].id == 1
    assert todo_entity_list[1].id == 2
    assert todo_entity_list[2].id == 3


def test_update_ok(session):
    """
    Todoの更新 正常
    """
    try:
        todo_repository: ITodoRepository = TodoRepository(session)

        todo_entity: TodoEntity = todo_repository.find_by_id(id=1)
        todo_entity.title = "test title updated"
        todo_entity.is_done = True
        todo_repository.update(todo_entity=todo_entity)
        session.commit()

        updated_todo_entity: TodoEntity = todo_repository.find_by_id(id=1)
    except Exception:
        assert False

    assert updated_todo_entity.updated_at > todo_entity.updated_at
    assert updated_todo_entity.title == "test title updated"
    assert updated_todo_entity.is_done is True


def test_delete_ok(session):
    """
    Todoの削除 正常
    """
    try:
        todo_repository: ITodoRepository = TodoRepository(session)

        todo_repository.delete_by_id(id=1)
        session.commit()

        todo_entity: TodoEntity = todo_repository.find_by_id(id=1)
    except Exception:
        assert False

    assert todo_entity is None
