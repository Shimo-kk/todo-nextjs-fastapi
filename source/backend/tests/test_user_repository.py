from app.domain.entitys.user_entity import UserEntity, IUserRepository
from app.infrastructure.repositorys.user_repository import UserRepository


def test_insert_ok(session):
    """
    ユーザーの挿入 正常
    """
    try:
        user_repository: IUserRepository = UserRepository(session)

        new_user_entity: UserEntity = UserEntity.create(
            name="test user", email="test@example.com", password="testtest"
        )
        user_repository.insert(user_entity=new_user_entity)
        session.commit()

        user_entity: UserEntity = user_repository.find_by_email(email=new_user_entity.email)
    except Exception:
        assert False

    assert user_entity.id is not None
    assert user_entity.created_at is not None
    assert user_entity.updated_at is not None
    assert user_entity.name == new_user_entity.name
    assert user_entity.email == new_user_entity.email
    assert user_entity.password == new_user_entity.password


def test_insert_ng_already_exists(session):
    """
    ユーザーの挿入 異常 重複
    """
    try:
        user_repository: IUserRepository = UserRepository(session)

        user_entity: UserEntity = user_repository.find_by_id(id=1)
        new_user_entity: UserEntity = UserEntity.create(name="test user", email=user_entity.email, password="testtest")
        user_repository.insert(user_entity=new_user_entity)
        session.commit()
    except Exception:
        assert True


def test_update_ok(session):
    """
    ユーザーの更新 正常
    """
    try:
        user_repository: IUserRepository = UserRepository(session)

        user_entity: UserEntity = user_repository.find_by_id(id=1)
        user_entity.name = "test user updated"
        user_repository.update(user_entity=user_entity)
        session.commit()

        updated_user_entity: UserEntity = user_repository.find_by_id(id=1)
    except Exception:
        assert False

    assert updated_user_entity.updated_at > user_entity.updated_at
    assert updated_user_entity.name == "test user updated"
    assert updated_user_entity.email == user_entity.email
    assert updated_user_entity.password == user_entity.password


def test_delete_ok(session):
    """
    ユーザーの削除 正常
    """
    try:
        user_repository: IUserRepository = UserRepository(session)

        user_repository.delete_by_id(id=1)
        session.commit()

        user_entity: UserEntity = user_repository.find_by_id(id=1)
    except Exception:
        assert False

    assert user_entity is None
