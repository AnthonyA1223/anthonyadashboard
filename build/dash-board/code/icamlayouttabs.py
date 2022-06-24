from datetime import datetime as dt
from datetime import timedelta

import dash_bootstrap_components as dbc  # #
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from listutils import (analyse_tab_checklist_ICAM, config, icamaffichedaily,
                       icamaffichehist)

df=pd.read_csv("df.zip")
df["Date"]=pd.to_datetime(df["Date"])
# %% ICAM Layout
HistoriquetabIcam = dcc.Tab(
    label="Historique",
    children=[
        html.Div(
            [
                html.Div(
                    [
                        dcc.DatePickerRange(
                            id="ICAM_datepicker",
                            # with_portal=True,
                            min_date_allowed=dt(2021, 3, 10),
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
                dcc.Dropdown(
                    id="historique-sel-icam",
                    options=[{"label": i, "value": i} for i in icamaffichehist],
                    value="Ptot_Ilot_ICAM",
                ),
            ],
            style={
                "width": "20%",
                "display": "inline-block",
                "marginTop": 30,
                "marginBottom": 15,
            },
        ),
        dcc.Graph(id="histo-graph-icam", config=config),
    ],
)

JournalieretabIcam = dcc.Tab(
    label="Journalière",
    children=[
        html.Div(
            [
                dcc.Dropdown(
                    id="daily-sel-icam",
                    options=[{"label": i, "value": i} for i in icamaffichedaily],
                    value=["Ptot_Ilot"],
                    multi=True,
                )
            ],
            style={
                "width": "20%",
                "display": "inline-block",
                "marginTop": 30,
                "marginBottom": 15,
            },
        ),
        dcc.Graph(id="daily-graph-icam", config=config),
    ],
)

Analysehisttabicam = dcc.Tab(
    label="Analyse Historique",
    children=[
        html.Div(
            [
                dcc.DatePickerRange(
                    id="analyse-date-picker-range-icam",
                    # with_portal=True,
                    min_date_allowed=dt(2021, 3, 10),
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
                    id="CheckID_icam",
                    options=analyse_tab_checklist_ICAM,
                    value=[
                        "Ptot_Ilot_ICAM",
                        "Ptot_ICAM_PV",
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
        dcc.Graph(id="analyse-graph-icam", config=config),
    ],
)
del(df)