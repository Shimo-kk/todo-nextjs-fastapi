from app.domain.entitys.user_entity import UserEntity
from app.infrastructure.repositorys.user_repository import UserRepository
from app.service.models.auth_model import SignUpModel, SignInModel
from app.service.models.user_model import UserReadModel
from app.domain.exceptions import ValueObjectValidError
from app.service.exceptions import (
    ValidError,
    AlreadyExistsError,
    NotFoundError,
    BadRequestError,
)


class AuthUseCase:
    """
    認証のユースケースクラス

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

    def sign_up(self, data: SignUpModel):
        """
        サインアップ

        Args:
            data: サインアップモデル
        """
        try:
            # E-mailでユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_email(email=data.email)
            if user_entity:
                raise AlreadyExistsError("E-mailアドレスがすでに存在しています。")

            # ユーザーエンティティを作成
            new_user_entity: UserEntity = UserEntity.create(name=data.name, email=data.email, password=data.password)

            # ユーザーの挿入
            self.user_repository.insert(user_entity=new_user_entity)

        except ValueObjectValidError as e:
            raise ValidError(e)
        except Exception:
            raise

    def sign_in(self, data: SignInModel) -> UserReadModel:
        """
        サインイン

        Args:
            data: サインインモデル
        """
        try:
            # E-mailでユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_email(email=data.email)

            # ユーザーが存在しない場合は例外を投げる
            if not user_entity:
                raise NotFoundError("E-mailアドレスが存在しません。")

            # パスワードが正しくない場合は例外を投げる
            if not user_entity.verify_password(plain_pw=data.password):
                raise BadRequestError("パスワードに誤りがあります。")

            # ユーザー参照モデルへ変換
            result: UserReadModel = UserReadModel(
                id=user_entity.id,
                name=user_entity.name,
                email=user_entity.email,
            )

        except Exception:
            raise

        return result

    def get_current_signed_user(self, email: str) -> UserReadModel:
        """
        現在サインインしているユーザーを取得

        Args:
            email: E-Mailアドレス
        """
        try:
            # E-mailでユーザーを取得
            user_entity: UserEntity = self.user_repository.find_by_email(email=email)

            # ユーザーが存在しない場合は例外を投げる
            if not user_entity:
                raise NotFoundError("ユーザーが存在しません。")

            # ユーザー参照モデルへ変換
            result: UserReadModel = UserReadModel(
                id=user_entity.id,
                name=user_entity.name,
                email=user_entity.email,
            )
        except Exception:
            raise

        return result
