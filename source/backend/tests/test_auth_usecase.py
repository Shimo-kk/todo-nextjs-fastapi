from app.service.usecases.auth_usecase import AuthUseCase
from app.service.models.auth_model import SignUpModel, SignInModel
from app.service.models.user_model import UserReadModel
from app.service.exceptions import (
    AlreadyExistsError,
    NotFoundError,
    BadRequestError,
)


def test_sign_up_ok(session):
    """
    サインアップ 正常
    """
    try:
        data: SignUpModel = SignUpModel(name="test user", email="test@example.com", password="testtest")

        usecase: AuthUseCase = AuthUseCase(session)
        _ = usecase.sign_up(data)

    except Exception:
        assert False

    assert True


def test_sign_up_ng_already_exists(session):
    """
    サインアップ 異常 重複
    """
    try:
        data: SignUpModel = SignUpModel(name="test user", email="test1@example.com", password="testtest")

        usecase: AuthUseCase = AuthUseCase(session)
        _ = usecase.sign_up(data)
        assert False

    except AlreadyExistsError:
        assert True
    except Exception:
        assert False


def test_sign_in_ok(session):
    """
    サインイン 正常
    """
    try:
        data: SignInModel = SignInModel(email="test1@example.com", password="testtest")

        usecase: AuthUseCase = AuthUseCase(session)
        result: UserReadModel = usecase.sign_in(data)

    except Exception:
        assert False

    assert result.id is not None
    assert result.name == "test user1"
    assert result.email == "test1@example.com"


def test_sign_in_ng_not_found(session):
    """
    サインイン 異常 存在しない
    """
    try:
        data: SignInModel = SignInModel(email="test@example.com", password="testtest")

        usecase: AuthUseCase = AuthUseCase(session)
        _ = usecase.sign_in(data)
        assert False

    except NotFoundError:
        assert True
    except Exception:
        assert False


def test_sign_in_ng_bad_request(session):
    """
    サインイン 異常 パスワード不一致
    """
    try:
        data: SignInModel = SignInModel(email="test1@example.com", password="testtesttest")

        usecase: AuthUseCase = AuthUseCase(session)
        _ = usecase.sign_in(data)
        assert False

    except BadRequestError:
        assert True
    except Exception:
        assert False
