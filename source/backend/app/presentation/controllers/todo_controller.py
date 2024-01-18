from fastapi import Request, HTTPException, status
from app.service.usecases.todo_usecase import TodoUseCase
from app.service.models.todo_model import TodoCreateModel, TodoUpdateModel, TodoReadModel
from app.service.exceptions import (
    ValidError,
    NotFoundError,
)


class TodoController:
    """
    Todoのコントローラークラス
    """

    @staticmethod
    def create_todo(request: Request, data: TodoCreateModel) -> TodoReadModel:
        """
        Todoの作成

        Args:
            request: リクエスト
            data: Todo作成モデル
        Returns:
            TodoReadModel: 作成したTodoの参照モデル
        """
        try:
            usecase: TodoUseCase = TodoUseCase(db_session=request.state.db_session)
            result: TodoReadModel = usecase.create_todo(data=data)
        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except ValidError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception:
            raise

        return result

    @staticmethod
    def find_all(request: Request, user_id: int) -> list[TodoReadModel]:
        """
        Todoの全件取得

        Args:
            request: リクエスト
            user_id: ユーザーID
        Returns:
            list[TodoReadModel]: 取得したTodoの参照モデルリスト
        """
        try:
            usecase: TodoUseCase = TodoUseCase(db_session=request.state.db_session)
            result: list[TodoReadModel] = usecase.find_all(user_id=user_id)
        except Exception:
            raise

        return result

    @staticmethod
    def update_todo(request: Request, data: TodoUpdateModel) -> TodoReadModel:
        """
        Todoの更新

        Args:
            request: リクエスト
            data: Todo更新モデル
        Returns:
            TodoReadModel: 更新したTodoの参照モデル
        """
        try:
            usecase: TodoUseCase = TodoUseCase(db_session=request.state.db_session)
            result: TodoReadModel = usecase.update_todo(data=data)
        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except Exception:
            raise

        return result

    @staticmethod
    def done_todo(request: Request, id: int) -> TodoReadModel:
        """
        Todoの完了

        Args:
            request: リクエスト
            id: TodoID
        Returns:
            TodoReadModel: 完了したTodoの参照モデル
        """
        try:
            usecase: TodoUseCase = TodoUseCase(db_session=request.state.db_session)
            result: TodoReadModel = usecase.done_todo(id=id)
        except Exception:
            raise

        return result

    @staticmethod
    def delete_todo(request: Request, id: int):
        """
        Todoの削除

        Args:
            request: リクエスト
            id: TodoID
        """
        try:
            usecase: TodoUseCase = TodoUseCase(db_session=request.state.db_session)
            usecase.delete_todo(id=id)
        except Exception:
            raise
