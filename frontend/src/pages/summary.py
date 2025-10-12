"""
Summary page layout for viewing monthly financial summaries.
"""

from dash import dcc, html
from datetime import datetime
from styles import (
    card_style,
    page_container_style,
    input_style,
    button_style,
    label_style,
    COLORS,
)


def get_summary_page():
    """Returns the summary page layout."""
    return html.Div(
        [
            html.Div(
                [
                    html.H2(
                        "Monthly Summary",
                        style={
                            "marginTop": "0",
                            "marginBottom": "24px",
                            "color": COLORS["text"],
                            "fontSize": "28px",
                            "fontWeight": "700",
                        },
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Label("Year", style=label_style),
                                    dcc.Input(
                                        id="summary-year",
                                        type="number",
                                        placeholder="Year",
                                        value=datetime.now().year,
                                        style={**input_style, "marginBottom": "0"},
                                    ),
                                ],
                                style={"flex": "1", "marginRight": "12px"},
                            ),
                            html.Div(
                                [
                                    html.Label("Month", style=label_style),
                                    dcc.Input(
                                        id="summary-month",
                                        type="number",
                                        placeholder="Month",
                                        value=datetime.now().month,
                                        min=1,
                                        max=12,
                                        style={**input_style, "marginBottom": "0"},
                                    ),
                                ],
                                style={"flex": "1"},
                            ),
                        ],
                        style={"display": "flex", "marginBottom": "16px"},
                    ),
                    html.Button(
                        "Get Summary",
                        id="get-summary-button",
                        n_clicks=0,
                        style=button_style,
                    ),
                    html.Div(id="summary-output", style={"marginTop": "24px"}),
                ],
                style={**card_style, "maxWidth": "800px", "margin": "0 auto"},
            )
        ],
        style=page_container_style,
    )
