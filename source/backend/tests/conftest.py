import alembic
import alembic.config
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.infrastructure.middlewares.http_request_middleware_test import TestHttpRequestMiddleware
from app.infrastructure.database.postgresql_test import SQLALCHEMY_DATABASE_URL, engine, get_db_session
from app.infrastructure.dtos import Base
from app.infrastructure.dtos.user_dto import UserDto
from app.domain.entitys.user_entity import UserEntity
from app.presentation.routers.v1 import api_v1_router

test_app = FastAPI()
test_app.add_middleware(TestHttpRequestMiddleware)
test_app.include_router(api_v1_router, prefix="/api/v1")


def create_test_data(session):
    # user
    test_users: list[UserDto] = [
        UserDto.from_entity(UserEntity.create(name="test user1", email="test1@example.com", password="testtest")),
        UserDto.from_entity(UserEntity.create(name="test user2", email="test2@example.com", password="testtest")),
        UserDto.from_entity(UserEntity.create(name="test user3", email="test3@example.com", password="testtest")),
    ]
    session.add_all(test_users)

    session.commit()
    session.remove()


@pytest.fixture(scope="function")
def session():
    Base.metadata.create_all(bind=engine)

    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
    alembic.command.upgrade(alembic_cfg, "head")
    create_test_data(get_db_session())

    session = get_db_session()
    yield session
    session.remove()

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)

    alembic_cfg = alembic.config.Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)
    alembic.command.upgrade(alembic_cfg, "head")
    create_test_data(get_db_session())

    client = TestClient(test_app)
    yield client

    Base.metadata.drop_all(bind=engine)
