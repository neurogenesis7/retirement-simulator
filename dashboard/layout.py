"""
Application layout.

Defines the static Dash layout.
"""

from dash import dcc
from dash import html


def input_card():

    return html.Div(

        [

            html.H2("Simulation Inputs"),

            html.Hr(),

            html.Div(id="input-panel"),

            html.Button(

                "Run Simulation",

                id="run-button",

                n_clicks=0,

                style={

                    "width": "100%",

                    "marginTop": "20px",

                    "height": "45px",

                },

            ),

        ],

        style={

            "padding": "20px",

            "border": "1px solid lightgray",

            "borderRadius": "8px",

            "backgroundColor": "#fafafa",

        },

    )


def results_card():

    return html.Div(

        [

            html.H2("Simulation Results"),

            html.Hr(),

            html.Div(id="summary-cards"),

            dcc.Graph(id="fan-chart"),

            dcc.Graph(id="distribution-chart"),

            dcc.Graph(id="survival-chart"),

        ],

        style={

            "padding": "20px",

            "border": "1px solid lightgray",

            "borderRadius": "8px",

        },

    )


def create_layout():

    return html.Div(

        [

            html.H1(

                "Retirement Simulation Laboratory",

                style={

                    "textAlign": "center",

                    "marginBottom": "30px",

                },

            ),

            html.Div(

                [

                    html.Div(

                        input_card(),

                        style={

                            "width": "28%",

                            "display": "inline-block",

                            "verticalAlign": "top",

                        },

                    ),

                    html.Div(

                        results_card(),

                        style={

                            "width": "70%",

                            "display": "inline-block",

                            "marginLeft": "2%",

                            "verticalAlign": "top",

                        },

                    ),

                ]

            ),

        ],

        style={

            "maxWidth": "1800px",

            "margin": "auto",

            "padding": "30px",

            "fontFamily": "Arial",

        },

    )