import dash_bootstrap_components as dbc  # #
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from datetime import  timedelta


fntsize = "1.75vmin"
cardsheight = "11.5vh"

card3 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(
                            [
                                html.B("Irradiation Solaire:"),
                                html.Br(),
                                html.B(children=["75 W/m"], id="solirr_card"),
                                html.Sup(
                                    "2",
                                    style={
                                        "font-weight": "bold",
                                    },
                                ),
                            ]
                        )
                        # html.P("This card has some text content", className="card-text",),
                    ],
                    className="align-self-center",
                    style={
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                    },
                )
            ],
            color="rgb(76, 181, 245)",
            inverse=True,
            style={"font-size": f"{fntsize}", "height": f"{cardsheight}"},
        ),
        dbc.Card(
            dbc.CardImg(
                src="/assets/sun.png",
                style={"display": "flex", "justify-content": "center"},
            ),
            style={
                "maxWidth": 75,
                "display": "flex",
                "justify-content": "center",
                "height": f"{cardsheight}",
            },
            color="rgb(28, 78, 128)",  # "background-color": "rgb(220,220,220)"},
        ),
    ],
    className="mt-4 shadow",
    style={"height": f"{cardsheight}"},
)

card2 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Span(
                        [
                            html.B("Humidité Relative: "),
                            html.Br(),
                            html.B(children=["80%"], id="humidity_card"),
                        ]
                    )
                    # html.P("This card has some text content", className="card-text",),
                ],
                style={
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                },
            ),
            color="rgb(76, 181, 245)",
            inverse=True,
            style={"font-size": f"{fntsize}", "height": f"{cardsheight}"},
        ),
        dbc.Card(
            dbc.CardImg(
                src="/assets/humidity.png",
                style={"display": "flex", "justify-content": "center"},
            ),
            style={
                "maxWidth": 75,
                "display": "flex",
                "justify-content": "center",
                "height": f"{cardsheight}",
            },  # "background-color": "rgb(220,220,220)"},
            color="rgb(28, 78, 128)",
        ),
    ],
    className="mt-4 shadow",
    style={"height": f"{cardsheight}"},
)


card1 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Span(
                        [
                            html.B("Température: "),
                            html.Br(),
                            html.B(children=["12℃"], id="temp_card"),
                        ]
                    )
                    # html.P("This card has some text content", className="card-text",),
                ],
                style={
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                },
            ),
            color="rgb(76, 181, 245)",
            inverse=True,
            style={"font-size": f"{fntsize}", "height": f"{cardsheight}"},
        ),
        dbc.Card(
            dbc.CardImg(
                src="/assets/centigrade.png",
                style={"display": "flex", "justify-content": "center"},
            ),
            style={
                "maxWidth": 75,
                "display": "flex",
                "justify-content": "center",
                "height": f"{cardsheight}",
            },  # "background-color": "rgb(220,220,220)"},
            color="rgb(28, 78, 128)",
        ),
    ],
    className="mt-4 shadow",
    style={"height": f"{cardsheight}"},
)

card4 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Span(
                        [
                            html.B("Pression Atmosphérique: "),
                            html.Br(),
                            html.B(children=["1013.25 hPa"], id="pressure_card"),
                        ]
                    )
                    # html.P("This card has some text content", className="card-text",),
                ],
                style={
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                },
            ),
            color="rgb(76, 181, 245)",
            inverse=True,
            style={"font-size": f"{fntsize}", "height": f"{cardsheight}"},
        ),
        dbc.Card(
            dbc.CardImg(
                src="/assets/atmospheric.png",
                style={"display": "flex", "justify-content": "center"},
            ),
            style={
                "maxWidth": 75,
                "display": "flex",
                "justify-content": "center",
                "height": f"{cardsheight}",
            },  # "background-color": "rgb(220,220,220)"},
            color="rgb(28, 78, 128)",
        ),
    ],
    className="mt-4 shadow",
    style={"height": f"{cardsheight}"},
)

card5 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Span(
                        [
                            html.B("Vitesse du Vent: "),
                            html.Br(),
                            html.B(children=["5 m/s"], id="wind_card"),
                        ]
                    ),
                    # html.P("This card has some text content", className="card-text",),
                ],
                style={
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                },
            ),
            color="rgb(76, 181, 245)",
            inverse=True,
            style={"font-size": f'{fntsize},"height":f"{cardsheight}"'},
        ),
        dbc.Card(
            dbc.CardImg(
                src="/assets/wind.png",
                style={"display": "flex", "justify-content": "center"},
            ),
            style={
                "maxWidth": 75,
                "display": "flex",
                "justify-content": "center",
                "height": f"{cardsheight}",
            },  # "background-color": "rgb(220,220,220)"},
            color="rgb(28, 78, 128)",
        ),
    ],
    className="mt-4 shadow",
    style={"height": f"{cardsheight}"},
)


card6 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(
                            [
                                html.B("Précipitations les dernières"),
                                html.Br(),
                                dcc.Dropdown(
                                    id="rain_dropdown",
                                    options=[
                                        {"label": "60 minutes", "value": "1"},
                                        {"label": "2 heures", "value": "2"},
                                        {"label": "4 heures", "value": "4"},
                                        {"label": "6 heures", "value": "6"},
                                        {"label": "12 heures", "value": "12"},
                                        {"label": "24 heures", "value": "24"},
                                        {"label": "48 heures", "value": "48"},
                                        {"label": "72 heures", "value": "72"},
                                    ],
                                    value="1",
                                    clearable=False,
                                    style={
                                        "color": "black",
                                        "height": "3.9vh",
                                        "display": "inline-block",
                                        "width": "10vw",
                                    },
                                ),
                                html.Br(),
                                html.B(children=["2mm"], id="rain_card"),
                            ]
                        )
                        # html.P("This card has some text content", className="card-text",),
                    ],
                    className="align-self-center",
                    style={
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "height": f"{cardsheight}",
                    },
                )
            ],
            color="rgb(76, 181, 245)",
            inverse=True,
            style={"font-size": f"{fntsize}", "height": f"{cardsheight}"},
        ),
        dbc.Card(
            dbc.CardImg(
                src="/assets/raining.png",
                style={"display": "flex", "justify-content": "center"},
            ),
            style={
                "maxWidth": 75,
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "height": f"{cardsheight}",
            },
            color="rgb(28, 78, 128)",  # "background-color": "rgb(220,220,220)"},
        ),
    ],
    className="mt-4 shadow",
    style={"height": f"{cardsheight}"},
)


meteotab = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [card1, card2, card3],
                    width=3,
                    align="center",
                    style={
                        "vertical-align": "center",
                        "justify-content": "center",
                        "text-align": "center",
                        "font-size": f"{fntsize}",
                        "height": "40vh",
                    },
                ),
                dbc.Col(
                    [card4, card5, card6],
                    md="size",
                    sm="size",
                    width=3,
                    align="center",
                    style={
                        "vertical-align": "center",
                        "justify-content": "center",
                        "text-align": "center",
                        "font-size": f"{fntsize}",
                        "height": "40vh",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            id="wind_direction_graph",
                            style={
                                "width": "30vw",
                                "height": "30vw",
                                "display": "flex",
                                "justify-content": "center",
                                "text-align": "center",
                            },
                        )
                    ],
                    width=2,
                ),
            ],
            style={
                "display": "flex",
                "justify-content": "center",
                "text-align": "center",
            },
            justify="center",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dcc.DatePickerRange(
                        id="meteo_date_picker",
                        # with_portal=True,
                        min_date_allowed=dt(2021, 9, 16),
                        clearable=True,
                        display_format="D/M/YYYY",
                        max_date_allowed=dt.today() + timedelta(days=1),
                        start_date=dt.today().replace(
                            second=0,
                            hour=0,
                            minute=0,
                            microsecond=0,
                        )
                        - timedelta(days=1),
                        end_date=dt.today(),
                        style={
                            "font-family": "Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif",
                            "font-size": f"{fntsize}",
                            "font-weight": "bold",
                        },
                    ),
                    width=3,
                    style={
                        "font-family": "Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif",
                        "font-size": f"{fntsize}",
                        "font-weight": "bold",
                    },
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="temp_graph"), width=6),
                dbc.Col(dcc.Graph(id="IRR_graph"), width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="rain_graph"), width=6),
                dbc.Col(dcc.Graph(id="wind_graph"), width=6),
            ]
        ),
        dcc.Interval(
            id="interval_meteo_2mins",
            interval=60 * 2 * 1000,  # in milliseconds
            n_intervals=0,
        ),
    ],
    fluid=True,
)