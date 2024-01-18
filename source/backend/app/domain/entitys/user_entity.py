from datetime import datetime
from typing import ClassVar
from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError
from passlib.context import CryptContext
from abc import ABC, abstractmethod

from app.domain.entitys import BaseEntity
from app.domain.exceptions import ValueObjectValidError


class UserEntity(BaseEntity):
    """
    ユーザーのエンティティクラス

    Attributes:
        name: 名称
        email: E-mailアドレス
        password: パスワード（ハッシュ済み）
    """

    @dataclass(frozen=True)
    class Name:
        """
        ユーザー名のValueObject
        """

        value: str

        MIN_LENGTH: ClassVar[int] = 1
        MAX_LENGTH: ClassVar[int] = 50

        def __init__(self, value: str):
            """
            Args:
                value: 値
            """
            length: int = len(value)
            if length < self.MIN_LENGTH:
                raise ValueObjectValidError("ユーザー名が短すぎます。")
            if length > self.MAX_LENGTH:
                raise ValueObjectValidError("ユーザー名の長すぎます。")

            object.__setattr__(self, "value", value)

    @dataclass(frozen=True)
    class Email:
        """
        E-mailのValueObject
        """

        value: str

        MAX_LENGTH: ClassVar[int] = 255

        def __init__(self, value: str):
            """
            Args:
                value: 値
            """
            length: int = len(value)
            if length > self.MAX_LENGTH:
                raise ValueObjectValidError("メールアドレスが長すぎます。")

            try:
                emailinfo = validate_email(value, check_deliverability=False)
                email = emailinfo.normalized
            except EmailNotValidError:
                raise ValueObjectValidError("メールアドレスが不正です。")

            object.__setattr__(self, "value", email)

    @dataclass(frozen=True)
    class Password:
        """
        パスワードのValueObject
        """

        value: str
        pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

        MIN_LENGTH: ClassVar[int] = 6
        MAX_LENGTH: ClassVar[int] = 128

        def __init__(self, value: str):
            """
            Args:
                value: 値
            """
            length: int = len(value)
            if length < self.MIN_LENGTH:
                raise ValueObjectValidError("パスワードが短すぎます。")
            if length > self.MAX_LENGTH:
                raise ValueObjectValidError("パスワードが長すぎます。")

            hashed = self.pwd_ctx.hash(value)
            object.__setattr__(self, "value", hashed)

        @classmethod
        def verify_password(cls, plain_pw: str, hashed_pw: str) -> bool:
            return cls.pwd_ctx.verify(plain_pw, hashed_pw)

    def __init__(
        self,
        id: int = None,
        created_at: datetime = None,
        updated_at: datetime = None,
        name: str = "",
        email: str = "",
        password: str = "",
    ):
        """
        Args:
            id: 主キー
            created_at: 作成日時
            updated_at: 更新日時
            name: 名称
            email: E-mailアドレス
            password: パスワード
        """
        BaseEntity.__init__(self, id, created_at, updated_at)
        self.name: str = name
        self.email: str = email
        self.password: str = password

    def __eq__(self, o: object) -> bool:
        return BaseEntity.__eq__(o)

    @staticmethod
    def create(name: str, email: str, password: str) -> "UserEntity":
        """
        UserEntityの作成

        Args:
            name: 名称
            email: E-mailアドレス
            password: パスワード
        """
        return UserEntity(
            name=UserEntity.Name(name).value,
            email=UserEntity.Email(email).value,
            password=UserEntity.Password(password).value,
        )

    def verify_password(self, plain_pw: str) -> bool:
        """
        パスワードの検証

        Args:
            plain_pw: ハッシュ化前のパスワード
        """
        return UserEntity.Password.verify_password(plain_pw, self.password)


class IUserRepository(ABC):
    """
    ユーザーのリポジトリインターフェース
    """

    @abstractmethod
    def insert(self, user_entity: UserEntity) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self, user_entity: UserEntity) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        raise NotImplementedError
