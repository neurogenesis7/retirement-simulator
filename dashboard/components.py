"""
Reusable dashboard UI components.
"""

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


def section_header(title: str):
    """Create a standardized section header."""

    return html.H5(
        title,
        className="mt-3 mb-2 text-primary",
    )


def number_input(
    label: str,
    component_id: str,
    value,
    minimum,
    maximum,
    step,
):

    return dbc.Row(

        [

            dbc.Label(
                label,
                width=7,
            ),

            dbc.Col(

                dbc.Input(

                    id=component_id,

                    type="number",

                    value=value,

                    min=minimum,

                    max=maximum,

                    step=step,

                ),

                width=5,

            ),

        ],

        className="mb-2",

    )


def metric_card(title: str, value: str):

    return dbc.Card(

        dbc.CardBody(

            [

                html.Div(

                    title,

                    className="text-muted",

                ),

                html.H3(

                    value,

                    id=f"{title.lower().replace(' ','-')}-value",

                ),

            ]

        )

    )