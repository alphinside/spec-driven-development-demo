from sqlmodel import Session, select
from database import engine, create_db_and_tables
import models


def init_db():
    """Initialize database with tables and seed data."""
    # Create all tables
    create_db_and_tables()
    
    with Session(engine) as session:
        # Create accounts if they don't exist
        existing_accounts = session.exec(select(models.Account)).first()
        if not existing_accounts:
            session.add(models.Account(name="Cash"))
            session.add(models.Account(name="Bank"))
        
        # Create categories if they don't exist
        existing_categories = session.exec(select(models.Category)).first()
        if not existing_categories:
            # Expense Categories
            session.add(models.Category(name="Food", type="expense"))
            session.add(models.Category(name="Transportation", type="expense"))
            session.add(models.Category(name="Housing", type="expense"))
            session.add(models.Category(name="Utilities", type="expense"))
            session.add(models.Category(name="Entertainment", type="expense"))
            
            # Income Categories
            session.add(models.Category(name="Salary", type="income"))
            session.add(models.Category(name="Gifts", type="income"))
            session.add(models.Category(name="Other", type="income"))
        
        session.commit()