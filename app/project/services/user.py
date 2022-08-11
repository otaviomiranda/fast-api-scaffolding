from ..models.user import User
from ..repositories.user import UserRepository
from ..schemas.user import UserCreate
from ..utils.hash_password import get_password_hash


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def create_user(self, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        user_db = User(email=user.email, password=hashed_password,
                       first_name=user.first_name, last_name=user.last_name)

        return self._user_repository.add(user_db)
