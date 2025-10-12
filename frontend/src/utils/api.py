"""
API utilities for making requests to the backend.
"""
import requests

API_BASE_URL = "http://127.0.0.1:8000"


def create_transaction(transaction_data):
    """
    Create a new transaction.
    
    Args:
        transaction_data (dict): Transaction data including amount, description, date, type, category_id, account_id
        
    Returns:
        tuple: (success: bool, message: str, data: dict)
    """
    try:
        response = requests.post(
            f"{API_BASE_URL}/transactions/", 
            json=transaction_data
        )
        if response.status_code == 200:
            return True, "Transaction added successfully!", response.json()
        else:
            return False, f"Error: {response.text}", None
    except Exception as e:
        return False, f"Connection error: {str(e)}", None


def get_monthly_summary(year, month):
    """
    Get monthly financial summary.
    
    Args:
        year (int): Year
        month (int): Month (1-12)
        
    Returns:
        tuple: (success: bool, message: str, data: dict)
    """
    try:
        response = requests.get(f"{API_BASE_URL}/summary/{year}/{month}")
        if response.status_code == 200:
            return True, "Success", response.json()
        else:
            return False, f"Error: {response.text}", None
    except Exception as e:
        return False, f"Connection error: {str(e)}", None
