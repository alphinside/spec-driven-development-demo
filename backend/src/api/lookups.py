from fastapi import APIRouter, Depends
from sqlmodel import Session
from services import lookups as lookups_service
from database import get_session
import models

router = APIRouter()


@router.get("/categories/{category_type}", response_model=list[models.Category])
def get_categories(category_type: str, db: Session = Depends(get_session)):
    """Get categories by type."""
    return lookups_service.get_categories(db=db, category_type=category_type)


@router.get("/accounts", response_model=list[models.Account])
def get_accounts(db: Session = Depends(get_session)):
    """Get all accounts."""
    return lookups_service.get_accounts(db=db)
