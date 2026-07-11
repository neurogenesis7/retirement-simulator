"""
dashboard/layout.py

Main application layout for the Retirement Simulation Laboratory.
"""

from dash import html, dcc
import dash_bootstrap_components as dbc

from dashboard.components import (
    section_header,
    number_input,
    metric_card,
)


def input_panel():
    """
    Build the left-hand input panel.
    """

    return dbc.Card(

        [

            dbc.CardHeader(
                html.H4("Simulation Inputs")
            ),

            dbc.CardBody(

                [

                    #
                    # Portfolio
                    #
                    section_header("Portfolio"),

                    number_input(
                        "Initial Portfolio",
                        "initial-portfolio",
                        100000,
                        0,
                        100000000,
                        1000,
                    ),

                    number_input(
                        "Monthly Contribution",
                        "monthly-contribution",
                        1000,
                        0,
                        50000,
                        100,
                    ),

                    number_input(
                        "Annual Contribution Increase (%)",
                        "annual-contribution-growth",
                        3,
                        0,
                        20,
                        0.5,
                    ),

                    html.Hr(),

                    #
                    # Market
                    #
                    section_header("Market"),

                    number_input(
                        "Expected Return (%)",
                        "expected-return",
                        8,
                        -10,
                        30,
                        0.25,
                    ),

                    number_input(
                        "Volatility (%)",
                        "volatility",
                        15,
                        0,
                        100,
                        0.5,
                    ),

                    number_input(
                        "Inflation (%)",
                        "inflation",
                        3,
                        0,
                        20,
                        0.25,
                    ),

                    number_input(
                        "Inflation Volatility (%)",
                        "inflation-volatility",
                        1,
                        0,
                        10,
                        0.25,
                    ),

                    html.Hr(),

                    #
                    # Retirement
                    #
                    section_header("Retirement"),

                    number_input(
                        "Years Until Retirement",
                        "accumulation-years",
                        30,
                        1,
                        60,
                        1,
                    ),

                    number_input(
                        "Years in Retirement",
                        "retirement-years",
                        30,
                        1,
                        60,
                        1,
                    ),

                    number_input(
                        "Withdrawal Rate (%)",
                        "withdrawal-rate",
                        4,
                        1,
                        10,
                        0.25,
                    ),

                    html.Hr(),

                    #
                    # Simulation
                    #
                    section_header("Simulation"),

                    number_input(
                        "Monte Carlo Simulations",
                        "simulation-count",
                        10000,
                        100,
                        100000,
                        100,
                    ),

                    number_input(
                        "Random Seed",
                        "random-seed",
                        42,
                        0,
                        999999,
                        1,
                    ),

                ]

            ),

            dbc.CardFooter(

                dbc.Button(

                    "Run Simulation",

                    id="run-button",

                    color="primary",

                    className="w-100",

                )

            ),

        ]

    )


def create_layout():
    """
    Create the application layout.
    """

    return dbc.Container(

        [

            dbc.Row(

                dbc.Col(

                    html.H1(

                        "Retirement Simulation Laboratory",

                        className="text-center my-4",

                    )

                )

            ),

            dbc.Row(

                [

                    dbc.Col(

                        input_panel(),

                        width=3,

                    ),

                    dbc.Col(

                        [

                            dbc.Row(

                                [

                                    dbc.Col(
                                        metric_card(
                                            "Median",
                                            "--",
                                        )
                                    ),

                                    dbc.Col(
                                        metric_card(
                                            "Success",
                                            "--",
                                        )
                                    ),

                                    dbc.Col(
                                        metric_card(
                                            "Failure",
                                            "--",
                                        )
                                    ),

                                    dbc.Col(
                                        metric_card(
                                            "Monthly Income",
                                            "--",
                                        )
                                    ),

                                ],

                                className="mb-3",

                            ),

                            dbc.Card(

                                dbc.CardBody(

                                    dcc.Graph(
                                        id="fan-chart"
                                    )

                                ),

                                className="mb-3",

                            ),

                            dbc.Card(

                                dbc.CardBody(

                                    dcc.Graph(
                                        id="distribution-chart"
                                    )

                                ),

                                className="mb-3",

                            ),

                            dbc.Card(

                                dbc.CardBody(

                                    dcc.Graph(
                                        id="survival-chart"
                                    )

                                ),

                            ),

                        ],

                        width=9,

                    ),

                ]

            ),

        ],

        fluid=True,

    )