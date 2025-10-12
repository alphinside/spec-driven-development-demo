from fastapi import APIRouter, Depends
from sqlmodel import Session
import models
from services import transactions as transaction_service
from database import get_session

router = APIRouter()


@router.post("/transactions/", response_model=models.TransactionRead)
def create_transaction(
    transaction: models.TransactionCreate, 
    db: Session = Depends(get_session)
):
    """Create a new transaction (income or expense)."""
    return transaction_service.create_transaction(db=db, transaction=transaction)