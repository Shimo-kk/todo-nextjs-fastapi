from fastapi import status

URL = "api/v1/todo"


def test_get_all(client):
    """
    Todoの全件取得 正常
    """
    response = client.get(f"{URL}/list/1")
    assert response.status_code == status.HTTP_200_OK


def test_create_todo_ok(client):
    """
    Todoの作成 正常
    """
    data = {"user_id": 1, "title": "test title"}
    response = client.post(f"{URL}", json=data)
    assert response.status_code == status.HTTP_200_OK


def test_create_todo_ng_title_valid_error(client):
    """
    Todoの作成 異常 タイトルが不正
    """
    data = {"user_id": 1, "title": ""}
    response = client.post(f"{URL}", json=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_todo_ng_user_not_found(client):
    """
    Todoの作成 異常 ユーザーが存在しない
    """
    data = {"user_id": 0, "title": "test title"}
    response = client.post(f"{URL}", json=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_todo_ok(client):
    """
    Todoの更新 正常
    """
    data = {"id": 1, "title": "test title1 updated"}
    response = client.put(f"{URL}", json=data)
    assert response.status_code == status.HTTP_200_OK


def test_done_todo_ok(client):
    """
    Todoの完了 正常
    """
    response = client.put(f"{URL}/done/1")
    assert response.status_code == status.HTTP_200_OK


def test_delete_todo_ok(client):
    """
    Todoの完了 正常
    """
    response = client.delete(f"{URL}/1")
    assert response.status_code == status.HTTP_200_OK
