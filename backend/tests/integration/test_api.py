from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlalchemy.pool import StaticPool
from database import get_session
import models
from api import transactions, summary, lookups

TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Use StaticPool to ensure same connection is reused
)


def setup_test_db():
    """Create all tables and seed data for testing."""
    SQLModel.metadata.create_all(test_engine)

    with Session(test_engine) as session:
        # Add test accounts
        account1 = models.Account(name="Test Cash")
        account2 = models.Account(name="Test Bank")
        session.add(account1)
        session.add(account2)

        # Add test categories
        expense_cat = models.Category(name="Test Food", type="expense")
        income_cat = models.Category(name="Test Salary", type="income")
        session.add(expense_cat)
        session.add(income_cat)

        session.commit()


def override_get_session():
    """Override the database session for testing."""
    with Session(test_engine) as session:
        yield session


# Setup test database tables before any tests
setup_test_db()


# Create the app without importing from main to avoid lifespan issues
app = FastAPI()
app.include_router(transactions.router)
app.include_router(summary.router)
app.include_router(lookups.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}


# Override the dependency
app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Expense Tracker API"}


def test_create_transaction_endpoint():
    """Test creating an expense transaction."""
    response = client.post(
        "/transactions/",
        json={
            "amount": 100,
            "description": "Test transaction",
            "date": "2025-10-12",
            "type": "expense",
            "category_id": 1,
            "account_id": 1,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 100
    assert data["type"] == "expense"


def test_create_income_transaction_endpoint():
    """Test creating an income transaction."""
    response = client.post(
        "/transactions/",
        json={
            "amount": 500,
            "description": "Test income",
            "date": "2025-10-12",
            "type": "income",
            "category_id": 2,
            "account_id": 2,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 500
    assert data["type"] == "income"


def test_get_summary_endpoint():
    """Test getting monthly summary."""
    response = client.get("/summary/2025/10")
    assert response.status_code == 200
    data = response.json()
    assert "total_income" in data
    assert "total_spending" in data


def test_get_categories_endpoint():
    """Test getting categories by type."""
    response = client.get("/categories/expense")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_accounts_endpoint():
    """Test getting all accounts."""
    response = client.get("/accounts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
