"""
Transaction page layout for adding income and expenses.
"""

from dash import dcc, html
from datetime import datetime
from styles import (
    centered_card_style,
    page_container_style,
    input_style,
    button_style,
    label_style,
    COLORS,
)


def get_transaction_page():
    """Returns the transaction page layout."""
    return html.Div(
        [
            html.Div(
                [
                    html.H2(
                        "Add Transaction",
                        style={
                            "marginTop": "0",
                            "marginBottom": "24px",
                            "color": COLORS["text"],
                            "fontSize": "28px",
                            "fontWeight": "700",
                        },
                    ),
                    # Transaction type selector
                    html.Label("Transaction Type", style=label_style),
                    dcc.RadioItems(
                        id="transaction-type",
                        options=[
                            {"label": " Income", "value": "income"},
                            {"label": " Expense", "value": "expense"},
                        ],
                        value="expense",
                        inline=True,
                        style={"marginBottom": "24px"},
                        labelStyle={
                            "marginRight": "24px",
                            "fontSize": "16px",
                            "cursor": "pointer",
                        },
                    ),
                    # Amount
                    html.Label("Amount", style=label_style),
                    dcc.Input(
                        id="transaction-amount",
                        type="number",
                        placeholder="Enter amount",
                        style=input_style,
                    ),
                    # Description
                    html.Label("Description", style=label_style),
                    dcc.Input(
                        id="transaction-description",
                        type="text",
                        placeholder="Enter description",
                        style=input_style,
                    ),
                    # Date
                    html.Label("Date", style=label_style),
                    dcc.DatePickerSingle(
                        id="transaction-date",
                        date=datetime.now().date(),
                        display_format="YYYY-MM-DD",
                        style={"width": "100%", "marginBottom": "16px"},
                    ),
                    # Category
                    html.Label("Category", style=label_style),
                    dcc.Dropdown(
                        id="transaction-category",
                        placeholder="Select category",
                        style={"marginBottom": "16px"},
                    ),
                    # Account
                    html.Label("Account", style=label_style),
                    dcc.Dropdown(
                        id="transaction-account",
                        placeholder="Select account",
                        style={"marginBottom": "16px"},
                    ),
                    # Submit button
                    html.Button(
                        "Add Transaction",
                        id="add-transaction-button",
                        n_clicks=0,
                        style=button_style,
                    ),
                    # Output message
                    html.Div(
                        id="transaction-output",
                        style={
                            "marginTop": "16px",
                            "padding": "12px",
                            "borderRadius": "8px",
                            "textAlign": "center",
                            "fontWeight": "500",
                        },
                    ),
                ],
                style=centered_card_style,
            )
        ],
        style=page_container_style,
    )
