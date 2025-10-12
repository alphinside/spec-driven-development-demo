from sqlmodel import Session, select
import models


def get_categories(db: Session, category_type: str) -> list[models.Category]:
    """Get categories by type from the database."""
    return db.exec(select(models.Category).where(models.Category.type == category_type)).all()


def get_accounts(db: Session) -> list[models.Account]:
    """Get all accounts from the database."""
    return db.exec(select(models.Account)).all()
