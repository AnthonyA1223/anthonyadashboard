import dash_bootstrap_components as dbc  # #
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
from listutils import config,dailylabel,analyse_tab_checklist,Tablelist
import dash_table

df=pd.read_csv("df.zip")
df["Date"]=pd.to_datetime(df["Date"])

df2=pd.read_csv("df2.zip")
df2["Date"]=pd.to_datetime(df2["Date"])

available_indicators = df.keys().unique().drop("Date")

Historiquetab = dcc.Tab(
    label="Historique",
    children=[
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.DatePickerRange(
                                    id="my-date-picker-range-ga-category",
                                    # with_portal=True,
                                    min_date_allowed=dt(2019, 2, 17),
                                    display_format="D/M/YYYY",
                                    persistence=True,
                                    clearable=True,
                                    max_date_allowed=df["Date"].max().to_pydatetime()
                                    + timedelta(days=1),
                                    initial_visible_month=dt(
                                        df["Date"].max().to_pydatetime().year,
                                        df["Date"].max().to_pydatetime().month,
                                        1,
                                    ),
                                    start_date=dt.today().replace(
                                        second=0,
                                        hour=0,
                                        minute=0,
                                        microsecond=0,
                                    )
                                    - timedelta(days=7),
                                    end_date=dt.strptime(
                                        df["Date"]
                                        .max()
                                        .to_pydatetime()
                                        .strftime("%Y-%m-%d"),
                                        "%Y-%m-%d",
                                    )
                                    + timedelta(days=1),
                                )
                            ],
                            style={
                                "marginTop": 30,
                                "marginBottom": 15,
                            },
                        ),
                        dcc.RadioItems(
                            id="ConsoOrPV",
                            options=[
                                {
                                    "label": "Consommation",
                                    "value": "CONS",
                                },
                                {
                                    "label": "Production PV",
                                    "value": "PV",
                                },
                            ],
                            value="CONS",
                            labelStyle={"display": "inline-block"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    dcc.Dropdown(
                                        id="yaxis-column",
                                        options=[
                                            {
                                                "label": i,
                                                "value": i,
                                            }
                                            for i in available_indicators
                                        ],
                                        value="Ptot_Ilot",
                                    ),
                                    style={
                                        "width": "30%",
                                        "display": "inline-block",
                                    },
                                )
                            ]
                        ),
                    ],
                    style={
                        "width": "65%",
                        "display": "inline-block",
                    },
                ),
            ]
        ),
        dcc.Graph(id="indicator-graphic", config=config),
    ],
)

Journalieretab = dcc.Tab(
    label="Journalière",
    children=[
        html.Div(
            [
                dcc.Dropdown(
                    id="daily-sel",
                    options=[{"label": i, "value": i} for i in dailylabel],
                    value="Ilot_Consommation",
                )
            ],
            style={
                "width": "20%",
                "display": "inline-block",
                "marginTop": 30,
                "marginBottom": 15,
            },
        ),
        dcc.Graph(id="daily-graph", config=config),
    ],
)

Prevhisttab = dcc.Tab(
    label="Prévision Historique",
    children=[
        html.Div(
            [
                dcc.DatePickerRange(
                    id="weeklyprev-date-picker-range",
                    # with_portal=True,
                    min_date_allowed=dt(2018, 9, 16),
                    clearable=True,
                    display_format="D/M/YYYY",
                    max_date_allowed=df["Date"].max().to_pydatetime()
                    + timedelta(days=1),
                    initial_visible_month=dt(
                        df["Date"].max().to_pydatetime().year,
                        df["Date"].max().to_pydatetime().month,
                        1,
                    ),
                    start_date=dt.today().replace(
                        second=0,
                        hour=0,
                        minute=0,
                        microsecond=0,
                    )
                    - timedelta(days=7),
                    end_date=dt.strptime(
                        df["Date"].max().to_pydatetime().strftime("%Y-%m-%d"),
                        "%Y-%m-%d",
                    )
                    + timedelta(days=1),
                )
            ],
            style={"marginTop": 30, "marginBottom": 15},
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="weeklySelect",
                    options=[{"label": i, "value": i} for i in dailylabel],
                    value="Ilot_Consommation",
                )
            ],
            style={
                "width": "20%",
                "display": "inline-block",
            },
        ),
        dcc.Graph(id="weekly-prev", config=config),
    ],
)

# tempsreeltab=dcc.Tab(
#     label="Temps réel",
#     children=[dcc.Graph(id="kafka-graph", config=config)],
# ),

semainetab = dcc.Tab(
    label="Semaine",
    children=[
        html.Div(
            [
                dcc.Dropdown(
                    id="7day-sel",
                    options=[
                        {"label": i, "value": i}
                        for i in df2.keys()
                        .unique()
                        .drop("Date")
                        .drop("AirTemp")
                        .drop("CloudOpacity")
                        .drop("Dni")
                        .drop("Ghi")
                    ],
                    value="Ptot_Ilot_PV",
                )
            ],
            style={
                "width": "20%",
                "display": "inline-block",
                "marginTop": 30,
                "marginBottom": 15,
            },
        ),
        dcc.Graph(id="7day-graph", config=config),
    ],
)

Analysehisttab = dcc.Tab(
    label="Analyse Historique",
    children=[
        html.Div(
            [
                dcc.DatePickerRange(
                    id="analyse-date-picker-range",
                    # with_portal=True,
                    min_date_allowed=dt(2018, 9, 16),
                    clearable=True,
                    display_format="D/M/YYYY",
                    max_date_allowed=df["Date"].max().to_pydatetime()
                    + timedelta(days=1),
                    initial_visible_month=dt(
                        df["Date"].max().to_pydatetime().year,
                        df["Date"].max().to_pydatetime().month,
                        1,
                    ),
                    start_date=dt.today().replace(
                        second=0,
                        hour=0,
                        minute=0,
                        microsecond=0,
                    )
                    - timedelta(days=7),
                    end_date=dt.strptime(
                        df["Date"].max().to_pydatetime().strftime("%Y-%m-%d"),
                        "%Y-%m-%d",
                    )
                    + timedelta(days=1),
                )
            ],
            style={"marginTop": 30, "marginBottom": 15},
        ),
        html.Div(
            [
                dcc.Checklist(
                    id="CheckID",
                    options=analyse_tab_checklist,
                    value=[
                        "Ilot_Consommation",
                        "Ilot_PV",
                    ],
                    inputStyle={
                        "margin-left": "20px",
                        "margin-right": "5px",
                    },
                    labelStyle={"display": "inline-block"},
                )
            ],
            style={
                "width": "50%",
                "display": "inline-block",
            },
        ),
        dcc.Graph(id="analyse-graph", config=config),
    ],
)

SScomphistorique = dcc.Tab(
    label="Comparaison Historique",
    children=[
        html.Div(
            [
                html.Div(
                    [
                        dcc.DatePickerRange(
                            id="SteadySun-date-picker-range",
                            # with_portal=True,
                            min_date_allowed=dt(
                                2020,
                                9,
                                15,
                            ),
                            clearable=True,
                            display_format="D/M/YYYY",
                            max_date_allowed=df["Date"].max().to_pydatetime()
                            + timedelta(days=1),
                            initial_visible_month=dt(
                                df["Date"].max().to_pydatetime().year,
                                df["Date"].max().to_pydatetime().month,
                                1,
                            ),
                            start_date=dt.today().replace(
                                second=0,
                                hour=0,
                                minute=0,
                                microsecond=0,
                            )
                            - timedelta(days=7),
                            end_date=dt.strptime(
                                df["Date"].max().to_pydatetime().strftime("%Y-%m-%d"),
                                "%Y-%m-%d",
                            )
                            + timedelta(days=1),
                        )
                    ],
                    style={
                        "marginTop": 30,
                        "marginBottom": 15,
                    },
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="SSHist_HEI_Rizo",
                                        options=[
                                            {
                                                "label": "Rizomm_PV",
                                                "value": "RIZOMM",
                                            },
                                            {
                                                "label": "HEI_PV",
                                                "value": "HEI",
                                            },
                                        ],
                                        value="RIZOMM",
                                        multi=True,
                                    )
                                ],
                                style={
                                    "marginTop": 30,
                                    "marginBottom": 15,
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="SSHist_Mod",
                                        options=[
                                            {
                                                "label": "Réseau Neurones",
                                                "value": "_Forecast_",
                                            },
                                            {
                                                "label": "Steady_Sat",
                                                "value": "_ForecastSS_",
                                            },
                                            {
                                                "label": "Steady_Eye",
                                                "value": "_ForecastSE_",
                                            },
                                        ],
                                        value="_ForecastSE_",
                                        multi=True,
                                    )
                                ],
                                style={
                                    "marginTop": 30,
                                    "marginBottom": 15,
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="SSHist_MinMax",
                                        options=[
                                            {
                                                "label": "Maximum",
                                                "value": "Max",
                                            },
                                            {
                                                "label": "Moyenne",
                                                "value": "Moy",
                                            },
                                            {
                                                "label": "Minimum",
                                                "value": "Min",
                                            },
                                        ],
                                        value="Moy",
                                        multi=True,
                                    )
                                ],
                                style={
                                    "marginTop": 30,
                                    "marginBottom": 15,
                                },
                            ),
                            width="auto",
                        ),
                    ],
                    justify="center",
                ),
                dcc.Graph(
                    id="SS_hist_graph",
                    config=config,
                    style={"overflow-x": "hidden"},
                ),
                dash_table.DataTable(
                    style_cell={
                        "whiteSpace": "normal",
                        "height": "auto",
                        "width": "auto",
                        "textAlign": "center",
                        "margin-top": 30,
                        "margin-bottom": 30,
                        "backgroundColor": "lavender",
                    },
                    style_header={
                        "backgroundColor": "white",
                        "fontWeight": "bold",
                    },
                    # style_table={'align-items':"center"},
                    fill_width=False,
                    id="tableSS",
                    columns=[
                        {
                            "name": i,
                            "id": i,
                        }
                        for i in Tablelist
                    ],
                    css=[
                        {
                            "selector": ".row",
                            "rule": "margin: 0; display: block",
                        }
                    ],
                ),
            ]
        )
    ],
    style={
        "overflow-x": "hidden",
    },
)


SScompjournaliere = dcc.Tab(
    label="Comparaison Journalière",
    children=[
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="SSJour_HEI_Rizo",
                                        options=[
                                            {
                                                "label": "Rizomm_PV",
                                                "value": "RIZOMM",
                                            },
                                            {
                                                "label": "HEI_PV",
                                                "value": "HEI",
                                            },
                                        ],
                                        value="RIZOMM",
                                        multi=True,
                                    )
                                ],
                                style={
                                    "marginTop": 30,
                                    "marginBottom": 15,
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="SSJour_Mod",
                                        options=[
                                            {
                                                "label": "Réseau Neurones",
                                                "value": "_Forecast_",
                                            },
                                            {
                                                "label": "Steady_Sat",
                                                "value": "_ForecastSS_",
                                            },
                                            {
                                                "label": "Steady_Eye",
                                                "value": "_ForecastSE_",
                                            },
                                        ],
                                        value="_ForecastSE_",
                                        multi=True,
                                    )
                                ],
                                style={
                                    "marginTop": 30,
                                    "marginBottom": 15,
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="SSJour_MinMax",
                                        options=[
                                            {
                                                "label": "Maximum",
                                                "value": "Max",
                                            },
                                            {
                                                "label": "Moyenne",
                                                "value": "Moy",
                                            },
                                            {
                                                "label": "Minimum",
                                                "value": "Min",
                                            },
                                        ],
                                        value="Moy",
                                        multi=True,
                                    )
                                ],
                                style={
                                    "marginTop": 30,
                                    "marginBottom": 15,
                                },
                            ),
                            width="auto",
                        ),
                    ],
                    justify="center",
                ),
                dcc.Graph(
                    id="SS_Journ_graph",
                    config=config,
                ),
            ]
        )
    ],
)

SteadySunTab = dcc.Tab(
    label="Comparaison SteadySun",
    children=[
        dcc.Tabs(
            [
                SScomphistorique,
                SScompjournaliere,
            ]
        )
    ],
)
del(df)
del(df2)