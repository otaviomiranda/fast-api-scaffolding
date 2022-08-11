import random
import string
import time

from fastapi import Request


class Log:
    def __init__(self, logger) -> None:
        self._logger = logger

    async def log_requests(self, request: Request, call_next):
        idem = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=6))
        self._logger.info(f"rid={idem} start request path={request.url.path}")
        start_time = time.time()

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)
        self._logger.info(
            f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

        return response
