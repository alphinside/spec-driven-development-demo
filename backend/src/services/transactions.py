from sqlmodel import Session
import models


def create_transaction(
    db: Session, transaction: models.TransactionCreate
) -> models.Transaction:
    """Create a new transaction in the database."""
    db_transaction = models.Transaction.model_validate(transaction)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
