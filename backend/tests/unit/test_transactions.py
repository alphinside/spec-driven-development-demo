import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.src import models, services, schemas
from backend.src.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

enfine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# This is a placeholder test that will be expanded upon
def test_create_transaction():
    assert True