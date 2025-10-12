"""
Callback functions for summary-related interactions.
"""
from dash import html, Input, Output, State
from styles import COLORS
from utils.api import get_monthly_summary


def register_summary_callbacks(app):
    """Register all summary-related callbacks."""
    
    @app.callback(
        Output('summary-output', 'children'),
        Input('get-summary-button', 'n_clicks'),
        State('summary-year', 'value'),
        State('summary-month', 'value'),
        prevent_initial_call=True
    )
    def handle_get_summary(n_clicks, year, month):
        """Handle fetching monthly summary."""
        if n_clicks > 0:
            success, message, data = get_monthly_summary(year, month)
            
            if success:
                return _create_summary_display(data)
            else:
                return _create_error_message(f"✗ {message}")


def _create_summary_display(data):
    """Create the summary display component with income, expenses, and balance."""
    balance = data['total_income'] - data['total_spending']
    balance_color = COLORS['success'] if balance >= 0 else COLORS['danger']
    
    return html.Div([
        html.Div([
            _create_summary_card(
                "Total Income",
                data['total_income'],
                COLORS['success']
            ),
            _create_summary_card(
                "Total Expenses",
                data['total_spending'],
                COLORS['danger']
            ),
            _create_summary_card(
                "Balance",
                balance,
                balance_color
            )
        ], style={'display': 'flex'})
    ])


def _create_summary_card(title, amount, color):
    """Create a single summary card."""
    return html.Div([
        html.Div(title, style={
            'fontSize': '14px',
            'color': COLORS['text-light'],
            'marginBottom': '8px'
        }),
        html.Div(f"IDR {amount:,.2f}", style={
            'fontSize': '32px',
            'fontWeight': '700',
            'color': color
        })
    ], style={
        'flex': '1',
        'padding': '24px',
        'backgroundColor': color + '10',
        'borderRadius': '8px',
        'marginRight': '12px'
    })


def _create_error_message(message):
    """Create an error message component."""
    return html.Div(
        message,
        style={
            'padding': '12px',
            'backgroundColor': COLORS['danger'] + '20',
            'color': COLORS['danger'],
            'border': f'1px solid {COLORS["danger"]}',
            'borderRadius': '8px',
            'textAlign': 'center'
        }
    )
