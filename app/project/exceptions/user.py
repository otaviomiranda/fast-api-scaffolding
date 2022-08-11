from fastapi import Request
from fastapi.responses import JSONResponse


class EmailAlreadyRegistered(Exception):
    """Raised when try to create an user but email already exists"""

    def __init__(self, message='email already registered'):
        self.message = message
        super().__init__(self.message)


async def email_already_exists_exception_handler(request: Request, exc: EmailAlreadyRegistered):
    return JSONResponse(
        status_code=400,
        content={'message': exc.message},
    )
