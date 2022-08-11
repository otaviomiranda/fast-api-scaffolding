from sqlalchemy.orm import Session
from ..models.user import User
from sqlalchemy.exc import IntegrityError
from ..exceptions.user import EmailAlreadyRegistered

class UserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, user: User) -> User:

        try:
            self._session.add(user)
            self._session.commit()
            self._session.refresh(user)

            return user
        except IntegrityError:
            raise EmailAlreadyRegistered()


