from app.domain.entitys.user_entity import UserEntity
from app.domain.exceptions import ValueObjectValidError


def test_create_user_entity_ok():
    """
    UserEntityの作成 正常
    """
    try:
        new_user_entity: UserEntity = UserEntity.create(
            name="test user", email="test@example.com", password="testtest"
        )
    except Exception:
        assert False
    assert new_user_entity.id is None
    assert new_user_entity.created_at is None
    assert new_user_entity.updated_at is None
    assert new_user_entity.name == "test user"
    assert new_user_entity.email == "test@example.com"
    assert new_user_entity.verify_password("testtest")


def test_create_user_entity_ng_name_min_length():
    """
    UserEntityの作成 異常 ユーザー名が短い
    """
    try:
        _ = UserEntity.create(name="", email="test@example.com", password="testtest")
        assert False
    except ValueObjectValidError:
        assert True


def test_create_user_entity_ng_name_max_length():
    """
    UserEntityの作成 異常 ユーザー名が長い
    """
    try:
        _ = UserEntity.create(
            name="testtesttesttesttesttesttesttesttesttesttesttesttest",
            email="test@example.com",
            password="testtest",
        )
        assert False
    except ValueObjectValidError:
        assert True


def test_create_user_entity_ng_email_not_valid():
    """
    UserEntityの作成 異常 メールアドレスが不正
    """
    try:
        _ = UserEntity.create(name="test user", email="test", password="testtest")
        assert False
    except ValueObjectValidError:
        assert True


def test_create_user_entity_ng_password_min_length():
    """
    UserEntityの作成 異常 パスワードが短い
    """
    try:
        _ = UserEntity.create(name="test user", email="test@example.com", password="test")
        assert False
    except ValueObjectValidError:
        assert True
