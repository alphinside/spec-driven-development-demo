import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from sqlmodel import Session, SQLModel, create_engine, select
import models
from services.transactions import create_transaction


# Setup test database
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})


def setup_test_db():
    """Create all tables in the test database."""
    SQLModel.metadata.create_all(test_engine)


def get_test_session():
    """Get a test database session."""
    with Session(test_engine) as session:
        yield session


def test_create_transaction():
    """Test creating a transaction."""
    setup_test_db()
    
    with Session(test_engine) as session:
        # Create test account and category first
        account = models.Account(name="Test Account")
        category = models.Category(name="Test Category", type="expense")
        session.add(account)
        session.add(category)
        session.commit()
        session.refresh(account)
        session.refresh(category)
        
        # Create transaction
        transaction_data = models.TransactionCreate(
            amount=100.0,
            description="Test transaction",
            date="2025-10-12",
            type="expense",
            category_id=category.id,
            account_id=account.id
        )
        
        result = create_transaction(session, transaction_data)
        
        assert result.id is not None
        assert result.amount == 100.0
        assert result.description == "Test transaction"
        assert result.type == "expense"


def test_transaction_validation():
    """Test transaction data validation."""
    # Test with valid data
    transaction = models.TransactionCreate(
        amount=50.0,
        description="Valid transaction",
        date="2025-10-12",
        type="income",
        category_id=1,
        account_id=1
    )
    assert transaction.amount == 50.0
    assert transaction.type == "income"