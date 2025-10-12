from sqlmodel import Session, select, func, extract
import models


def get_summary(db: Session, year: int, month: int) -> dict:
    """Get financial summary for a specific month and year."""
    # Calculate total income
    income_stmt = select(func.sum(models.Transaction.amount)).where(
        models.Transaction.type == "income",
        extract("year", models.Transaction.date) == year,
        extract("month", models.Transaction.date) == month,
    )
    total_income = db.exec(income_stmt).one() or 0.0

    # Calculate total spending
    expense_stmt = select(func.sum(models.Transaction.amount)).where(
        models.Transaction.type == "expense",
        extract("year", models.Transaction.date) == year,
        extract("month", models.Transaction.date) == month,
    )
    total_spending = db.exec(expense_stmt).one() or 0.0

    # Get all transactions for the period
    transactions_stmt = select(models.Transaction).where(
        extract("year", models.Transaction.date) == year,
        extract("month", models.Transaction.date) == month,
    )
    transactions = db.exec(transactions_stmt).all()

    return {
        "total_income": total_income,
        "total_spending": total_spending,
        "transactions": transactions,
    }
