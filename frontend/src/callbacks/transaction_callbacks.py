"""
Callback functions for transaction-related interactions.
"""
from dash import html, Input, Output, State
from styles import COLORS
from utils.api import create_transaction


def register_transaction_callbacks(app):
    """Register all transaction-related callbacks."""
    
    @app.callback(
        Output('transaction-output', 'children'),
        Input('add-transaction-button', 'n_clicks'),
        State('transaction-type', 'value'),
        State('transaction-amount', 'value'),
        State('transaction-description', 'value'),
        State('transaction-date', 'date'),
        State('transaction-category', 'value'),
        State('transaction-account', 'value'),
        prevent_initial_call=True
    )
    def handle_add_transaction(n_clicks, trans_type, amount, description, date, category_id, account_id):
        """Handle adding a new transaction."""
        if n_clicks > 0:
            transaction_data = {
                "amount": amount,
                "description": description,
                "date": date,
                "type": trans_type,
                "category_id": category_id,
                "account_id": account_id
            }
            
            success, message, data = create_transaction(transaction_data)
            
            if success:
                return _create_success_message(f"✓ {trans_type.capitalize()} added successfully!")
            else:
                return _create_error_message(f"✗ {message}")


def _create_success_message(message):
    """Create a success message component."""
    return html.Div(
        message,
        style={
            'backgroundColor': COLORS['success'] + '20',
            'color': COLORS['success'],
            'border': f'1px solid {COLORS["success"]}'
        }
    )


def _create_error_message(message):
    """Create an error message component."""
    return html.Div(
        message,
        style={
            'backgroundColor': COLORS['danger'] + '20',
            'color': COLORS['danger'],
            'border': f'1px solid {COLORS["danger"]}'
        }
    )
