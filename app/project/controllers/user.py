from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies.db import get_session
from ..repositories.user import UserRepository
from ..schemas.user import User, UserCreate
from ..services.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.post('/', response_model=User)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    return user_service.create_user(user)
