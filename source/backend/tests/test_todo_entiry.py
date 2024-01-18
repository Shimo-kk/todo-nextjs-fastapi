from app.domain.entitys.todo_entity import TodoEntity
from app.domain.exceptions import ValueObjectValidError


def test_create_todo_entity_ok():
    """
    TodoEntityの作成 正常
    """
    try:
        new_todo_entity: TodoEntity = TodoEntity.create(user_id=1, title="test title")
    except Exception:
        assert False

    assert new_todo_entity.id is None
    assert new_todo_entity.created_at is None
    assert new_todo_entity.updated_at is None
    assert new_todo_entity.user_id == 1
    assert new_todo_entity.title == "test title"
    assert new_todo_entity.is_done is False


def test_create_todo_entity_ng_user_id_not_valid():
    """
    TodoEntityの作成 異常 ユーザーIDが不正
    """
    try:
        _ = TodoEntity.create(user_id=0, title="test title")
        assert False
    except ValueObjectValidError:
        assert True


def test_create_todo_entity_ng_title_not_valid():
    """
    TodoEntityの作成 異常 タイトルが不正
    """
    try:
        _ = TodoEntity.create(user_id=1, title="")
        assert False
    except ValueObjectValidError:
        assert True
