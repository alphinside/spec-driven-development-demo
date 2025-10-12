"""
Expense Tracker Application

A modular Dash application for tracking income and expenses.
"""
import dash
from dash import dcc, html, Input, Output

from components.navbar import get_navbar
from pages.transaction import get_transaction_page
from pages.summary import get_summary_page
from callbacks.transaction_callbacks import register_transaction_callbacks
from callbacks.summary_callbacks import register_summary_callbacks
from styles import app_container_style


# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    get_navbar(),
    html.Div(id='page-content')
], style=app_container_style)


# Page routing callback
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    """Route to the appropriate page based on URL pathname."""
    if pathname == '/summary':
        return get_summary_page()
    else:
        return get_transaction_page()


# Register all callbacks
register_transaction_callbacks(app)
register_summary_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)