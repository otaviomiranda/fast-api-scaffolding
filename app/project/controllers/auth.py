from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.get("/token", tags=["Authorization"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    pass