"""
Centralized styling configuration for the Expense Tracker application.
"""

# Color scheme
COLORS = {
    'background': '#f8f9fa',
    'card': '#ffffff',
    'primary': '#4f46e5',
    'success': '#10b981',
    'danger': '#ef4444',
    'text': '#1f2937',
    'text-light': '#6b7280',
    'border': '#e5e7eb',
    'hover': '#f3f4f6'
}

# Shared component styles
card_style = {
    'backgroundColor': COLORS['card'],
    'borderRadius': '12px',
    'padding': '32px',
    'boxShadow': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
    'marginBottom': '24px'
}

input_style = {
    'width': '100%',
    'padding': '12px 16px',
    'fontSize': '16px',
    'borderRadius': '8px',
    'border': f'1px solid {COLORS["border"]}',
    'marginBottom': '16px',
    'boxSizing': 'border-box'
}

button_style = {
    'backgroundColor': COLORS['primary'],
    'color': 'white',
    'padding': '12px 24px',
    'fontSize': '16px',
    'fontWeight': '600',
    'border': 'none',
    'borderRadius': '8px',
    'cursor': 'pointer',
    'width': '100%',
    'marginTop': '8px'
}

label_style = {
    'display': 'block',
    'marginBottom': '8px',
    'fontWeight': '600',
    'color': COLORS['text']
}

page_container_style = {
    'padding': '24px'
}

centered_card_style = {
    **card_style,
    'maxWidth': '600px',
    'margin': '0 auto'
}

app_container_style = {
    'backgroundColor': COLORS['background'],
    'minHeight': '100vh',
    'fontFamily': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
}
