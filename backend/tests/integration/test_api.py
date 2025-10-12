import pytest
from fastapi.testclient import TestClient
from backend.src.main import app

client = TestClient(app)

# This is a placeholder test that will be expanded upon
def test_create_transaction_endpoint():
    response = client.post("/transactions", json={
        "amount": 100,
        "description": "Test transaction",
        "date": "2025-10-12",
        "type": "expense",
        "category_id": 1,
        "account_id": 1
    })
    assert response.status_code == 200

def test_create_income_transaction_endpoint():
    response = client.post("/transactions/", json={
        "amount": 500,
        "description": "Test income",
        "date": "2025-10-12",
        "type": "income",
        "category_id": 6,
        "account_id": 2
    })
    assert response.status_code == 200

def test_get_summary_endpoint():
    response = client.get("/summary/2025/10")
    # We expect a 404 here because the endpoint doesn't exist yet
    assert response.status_code == 404