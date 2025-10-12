from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional


class Account(SQLModel, table=True):
    """Account model for managing financial accounts."""

    __tablename__ = "accounts"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)

    # Relationships
    transactions: list["Transaction"] = Relationship(back_populates="account")


class Category(SQLModel, table=True):
    """Category model for transaction categorization."""

    __tablename__ = "categories"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    type: str  # "income" or "expense"

    # Relationships
    transactions: list["Transaction"] = Relationship(back_populates="category")


class Transaction(SQLModel, table=True):
    """Transaction model for income and expense tracking."""

    __tablename__ = "transactions"

    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    description: Optional[str] = None
    date: date
    type: str  # "income" or "expense"
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")
    account_id: Optional[int] = Field(default=None, foreign_key="accounts.id")

    # Relationships
    category: Optional[Category] = Relationship(back_populates="transactions")
    account: Optional[Account] = Relationship(back_populates="transactions")


# Schemas for API input/output
class TransactionCreate(SQLModel):
    """Schema for creating a new transaction."""

    amount: float
    description: Optional[str] = None
    date: date
    type: str
    category_id: int
    account_id: int


class TransactionRead(SQLModel):
    """Schema for reading transaction data."""

    id: int
    amount: float
    description: Optional[str] = None
    date: date
    type: str
    category_id: int
    account_id: int
