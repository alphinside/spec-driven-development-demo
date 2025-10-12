"""
Navigation bar component for the application.
"""
from dash import dcc, html
from styles import COLORS


def get_navbar():
    """Returns the navigation bar component."""
    return html.Div([
        html.Div([
            html.H1("💰 Expense Tracker", style={
                'margin': '0',
                'fontSize': '24px',
                'fontWeight': '700',
                'color': COLORS['text']
            }),
            html.Div([
                dcc.Link('Add Transaction', href='/', style={
                    'padding': '8px 16px',
                    'marginRight': '12px',
                    'textDecoration': 'none',
                    'color': COLORS['text'],
                    'fontWeight': '500',
                    'borderRadius': '6px',
                }),
                dcc.Link('Summary', href='/summary', style={
                    'padding': '8px 16px',
                    'textDecoration': 'none',
                    'color': COLORS['text'],
                    'fontWeight': '500',
                    'borderRadius': '6px',
                })
            ], style={'display': 'flex'})
        ], style={
            'maxWidth': '1200px',
            'margin': '0 auto',
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'center',
            'padding': '0 24px'
        })
    ], style={
        'backgroundColor': COLORS['card'],
        'borderBottom': f'1px solid {COLORS["border"]}',
        'padding': '20px 0',
        'marginBottom': '32px'
    })
