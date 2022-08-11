from ..configs.db import SessionLocal
from sqlalchemy.orm import Session


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
