from fastapi import APIRouter, Depends
from sqlmodel import Session
from services import summary as summary_service
from database import get_session

router = APIRouter()


@router.get("/summary/{year}/{month}")
def get_summary(
    year: int, 
    month: int, 
    db: Session = Depends(get_session)
):
    """Get financial summary for a specific month and year."""
    return summary_service.get_summary(db=db, year=year, month=month)