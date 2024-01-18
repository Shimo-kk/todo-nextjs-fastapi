from app.service.usecases.todo_usecase import TodoUseCase
from app.service.models.todo_model import TodoCreateModel, TodoUpdateModel, TodoReadModel
from app.service.exceptions import (
    ValidError,
    NotFoundError,
)


def test_create_todo_ok(session):
    """
    Todoの作成 正常
    """
    try:
        data: TodoCreateModel = TodoCreateModel(user_id=1, title="test title")

        usecase: TodoUseCase = TodoUseCase(session)
        todo_read_model: TodoReadModel = usecase.create_todo(data=data)

    except Exception:
        assert False

    assert todo_read_model.id is not None
    assert todo_read_model.created_at is not None
    assert todo_read_model.updated_at is not None
    assert todo_read_model.user_id == 1
    assert todo_read_model.title == "test title"
    assert todo_read_model.is_done is False


def test_create_todo_ng_user_not_found(session):
    """
    Todoの作成 異常 ユーザーが存在しない
    """
    try:
        data: TodoCreateModel = TodoCreateModel(user_id=0, title="test title")

        usecase: TodoUseCase = TodoUseCase(session)
        _ = usecase.create_todo(data=data)
        assert False

    except NotFoundError:
        assert True
    except Exception:
        assert False


def test_create_todo_ng_title_valid_error(session):
    """
    Todoの作成 異常 タイトルが不正
    """
    try:
        data: TodoCreateModel = TodoCreateModel(user_id=1, title="")

        usecase: TodoUseCase = TodoUseCase(session)
        _ = usecase.create_todo(data=data)
        assert False

    except ValidError:
        assert True
    except Exception:
        assert False


def test_find_all_ok(session):
    """
    Todoの全件取得 正常
    """
    try:
        usecase: TodoUseCase = TodoUseCase(session)
        todo_read_model_list: list[TodoReadModel] = usecase.find_all(user_id=1)
    except Exception:
        assert False

    assert len(todo_read_model_list) == 3
    assert todo_read_model_list[0].id == 1
    assert todo_read_model_list[1].id == 2
    assert todo_read_model_list[2].id == 3


def test_update_todo_ok(session):
    """
    Todoの更新 正常
    """
    try:
        data: TodoUpdateModel = TodoUpdateModel(id=1, title="test title1 updated")

        usecase: TodoUseCase = TodoUseCase(session)
        todo_read_model: TodoReadModel = usecase.update_todo(data=data)
    except Exception:
        assert False

    assert todo_read_model.user_id == 1
    assert todo_read_model.title == "test title1 updated"
    assert todo_read_model.is_done is False


def test_done_todo_ok(session):
    """
    Todoの完了 正常
    """
    try:
        usecase: TodoUseCase = TodoUseCase(session)
        todo_read_model: TodoReadModel = usecase.done_todo(id=1)

    except Exception:
        assert False

    assert todo_read_model.user_id == 1
    assert todo_read_model.is_done is True


def test_delete_todo_ok(session):
    """
    Todoの削除 正常
    """
    try:
        usecase: TodoUseCase = TodoUseCase(session)
        usecase.delete_todo(id=1)
        assert True
    except Exception:
        assert False
