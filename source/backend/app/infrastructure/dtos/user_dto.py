from sqlalchemy import Column, VARCHAR
from typing import Union

from app.infrastructure.dtos import BaseDto
from app.domain.entitys.user_entity import UserEntity


class UserDto(BaseDto):
    """
    ユーザーのDTOクラス

    Attributes:
        name: 名称
        email: E-mailアドレス
        password: パスワード（ハッシュ済み）
    """

    __tablename__ = "user"

    name: Union[str, Column] = Column(VARCHAR(50), nullable=False, comment="名称")
    email: Union[str, Column] = Column(VARCHAR(255), unique=True, nullable=False, comment="E-mailアドレス")
    password: Union[str, Column] = Column(VARCHAR(128), nullable=False, comment="パスワード")

    @staticmethod
    def from_entity(user_entity: UserEntity) -> "UserDto":
        return UserDto(
            id=user_entity.id,
            created_at=user_entity.created_at,
            updated_at=user_entity.updated_at,
            name=user_entity.name,
            email=user_entity.email,
            password=user_entity.password,
        )

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            name=self.name,
            email=self.email,
            password=self.password,
        )
