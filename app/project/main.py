import logging

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from .controllers.user import router as user_ns
from .exceptions.user import (EmailAlreadyRegistered,
                              email_already_exists_exception_handler)
from .middlewares.log import Log

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)
log_middleware = Log(logger)

app = FastAPI(title='First Application')

# include middlewares
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware.log_requests)

# include routers
app.include_router(user_ns)

# importing error handlers
app.add_exception_handler(EmailAlreadyRegistered,
                          email_already_exists_exception_handler)


@app.get('/')
async def root():
    logger.info('logging from the root logger')
    return {'message': 'Hello World!'}
