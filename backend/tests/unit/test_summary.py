import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool
import models
from services.summary import get_summary
from datetime import date


# Setup test database
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Use StaticPool to ensure same connection is reused
)


def setup_test_db():
    """Create all tables in the test database."""
    SQLModel.metadata.create_all(test_engine)


def test_get_summary():
    """Test getting financial summary."""
    setup_test_db()

    with Session(test_engine) as session:
        # Create test data
        account = models.Account(name="Test Account")
        category_expense = models.Category(name="Test Expense", type="expense")
        category_income = models.Category(name="Test Income", type="income")

        session.add(account)
        session.add(category_expense)
        session.add(category_income)
        session.commit()
        session.refresh(account)
        session.refresh(category_expense)
        session.refresh(category_income)

        # Add transactions
        expense = models.Transaction(
            amount=100.0,
            description="Test expense",
            date=date(2025, 10, 12),
            type="expense",
            category_id=category_expense.id,
            account_id=account.id,
        )
        income = models.Transaction(
            amount=500.0,
            description="Test income",
            date=date(2025, 10, 15),
            type="income",
            category_id=category_income.id,
            account_id=account.id,
        )

        session.add(expense)
        session.add(income)
        session.commit()

        # Get summary
        result = get_summary(session, 2025, 10)

        assert result["total_income"] == 500.0
        assert result["total_spending"] == 100.0
        assert len(result["transactions"]) == 2


def test_get_summary_empty():
    """Test getting summary for a month with no transactions."""
    setup_test_db()

    with Session(test_engine) as session:
        result = get_summary(session, 2025, 12)

        assert result["total_income"] == 0.0
        assert result["total_spending"] == 0.0
        assert len(result["transactions"]) == 0
