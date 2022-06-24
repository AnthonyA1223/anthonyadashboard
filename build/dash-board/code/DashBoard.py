# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:57:28 2020

@author: anthony.aouad
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:58:43 2020

@author: anthony.aouad
"""
import base64
from datetime import datetime as dt
from datetime import timedelta
from time import perf_counter

import dash
import dash_bootstrap_components as dbc  # #
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import pytz
# import urllib3
# import xlsxwriter
# from apscheduler.schedulers.background import BackgroundScheduler
from dash.dependencies import Input, Output #,State
from dash_extensions.snippets import send_data_frame
from flask import send_file
from plotly.subplots import make_subplots
from sklearn.metrics import explained_variance_score  # #
from sklearn.metrics import mean_absolute_error, mean_squared_error


df=pd.read_csv("df.zip")
df["Date"]=pd.to_datetime(df["Date"])

df2=pd.read_csv("df2.zip")
df2["Date"]=pd.to_datetime(df2["Date"])

dfpvprev2=pd.read_csv("dfpvprev2.zip")
dfpvprev2["Date"]=pd.to_datetime(dfpvprev2["Date"])

df_merged=pd.read_csv("df_merged.zip")
df_merged["Date"]=pd.to_datetime(df_merged["Date"])

dfmeteoinst=pd.read_pickle("dfmeteoinst")

dfmeteo=pd.read_csv("dfmeteo.zip")
dfmeteo["Date"]=pd.to_datetime(dfmeteo["Date"])

dficam=pd.read_csv("dficam.zip")
dficam["Date"]=pd.to_datetime(dficam["Date"])

df_mergedtot=pd.read_csv("df_mergedtot.zip")
df_mergedtot["Date"]=pd.to_datetime(df_mergedtot["Date"])

df_mergedtot2=pd.read_csv("df_mergedtot2.zip")
df_mergedtot2["Date"]=pd.to_datetime(df_mergedtot2["Date"])

dfjourIC=pd.read_csv("dfjourIC.zip")
dfjourIC["Date"]=pd.to_datetime(dfjourIC["Date"])




from icamlayouttabs import (Analysehisttabicam, HistoriquetabIcam,
                            JournalieretabIcam)
from ilotlayouttabs import (Analysehisttab, Historiquetab, Journalieretab,
                            Prevhisttab, SScompjournaliere, SteadySunTab,
                            semainetab)
from listutils import (SSlist, affiche, affiche2, afficheicam, afficheirr,
                       affichetemp, dailylabel, icamlabel, irradlabel,
                       line_dash_mapSS, tab_style_div1)
from meteolayouttabs import meteotab

VALID_USERNAME_PASSWORD_PAIRS = {
}

# urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)

tz = pytz.timezone("Europe/Paris")
external_stylesheets = [
    "assets//DatTable.css",
    # "https://codepen.io/chriddyp/pen/bWLwgP.css",
    dbc.themes.BOOTSTRAP,
]
external_scripts = [
    "https://raw.githack.com/eKoopmans/html2pdf/master/dist/html2pdf.bundle.js"
]


app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
    title="DashBoard LiveTree",
)

## for basic auth

# auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)


server = app.server


# %% Database Init


# %% backend






# scheduler = BackgroundScheduler()
# scheduler.configure(timezone=pytz.timezone("Europe/Paris"))
# scheduler.add_job(CassOInput, "interval", seconds=59)

# # scheduler.add_job(kafkaget, 'interval',seconds=10)
# scheduler.start()





# %% Meteo layout
with open("./assets/boussole.webp", "rb") as image_file:
    encoded_string_meteo_image = base64.b64encode(image_file.read()).decode("utf-8")




# %% Layout
reallayout = html.Div(
    style={
        "overflow-x": "hidden",
        "font-size": "1.35vmin",
        "margin-left": "20px",
        "margin-right": "20px",
    },
    children=[
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Îlot Junia/ICL",
                    children=[
                        dcc.Tabs(
                            [
                                Historiquetab,
                                Journalieretab,
                                Prevhisttab,
                                semainetab,
                                Analysehisttab,
                                SteadySunTab,
                            ]
                        )
                    ],
                ),
                dcc.Tab(
                    label="ICAM",
                    children=[
                        dcc.Tabs(
                            [HistoriquetabIcam, JournalieretabIcam, Analysehisttabicam]
                        )
                    ],
                ),
                dcc.Tab(label="Station Météo", children=[meteotab]),
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=1 * 10000,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component2",
            interval=1000 * 21600,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component3",
            interval=1 * 60000,  # in milliseconds
            n_intervals=0,
        ),
    ],
)
# %% ENEDIS LAYOUT

layoutENEDIS = html.Div(
    id="alltabsid",
    style={"overflow-x": "hidden", "font-size": "1.35vmin"},
    children=[
        dcc.Tabs(
            [
                semainetab,
                SScompjournaliere,
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=1 * 10000,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component2",
            interval=1000 * 21600,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component3",
            interval=1 * 60000,  # in milliseconds
            n_intervals=0,
        ),
        html.Div(id="hiddendiv", style=tab_style_div1, children=[]),
    ],
)

layoutIlot = html.Div(
    id="alltabsid",
    style={"overflow-x": "hidden", "font-size": "1.35vmin"},
    children=[
        dcc.Tabs(
            [
                Historiquetab,
                Journalieretab,
                Prevhisttab,
                semainetab,
                Analysehisttab,
                SteadySunTab,
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=1 * 10000,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component2",
            interval=1000 * 21600,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component3",
            interval=1 * 60000,  # in milliseconds
            n_intervals=0,
        ),
        html.Div(id="hiddendiv", style=tab_style_div1, children=[]),
    ],
)

layoutICAM = html.Div(
    id="alltabsid",
    style={"overflow-x": "hidden", "font-size": "1.35vmin"},
    children=[
        dcc.Tabs(
            [
                HistoriquetabIcam, JournalieretabIcam, Analysehisttabicam
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=1 * 10000,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component2",
            interval=1000 * 21600,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component3",
            interval=1 * 60000,  # in milliseconds
            n_intervals=0,
        ),
        html.Div(id="hiddendiv", style=tab_style_div1, children=[]),
    ],
)

layoutMeteo = html.Div(
    id="alltabsid",
    style={"overflow-x": "hidden", "font-size": "1.35vmin"},
    children=[
        dcc.Tabs(
            [
                meteotab
            ]
        ),
        dcc.Interval(
            id="interval-component",
            interval=1 * 10000,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component2",
            interval=1000 * 21600,  # in milliseconds
            n_intervals=0,
        ),
        dcc.Interval(
            id="interval-component3",
            interval=1 * 60000,  # in milliseconds
            n_intervals=0,
        ),
        html.Div(id="hiddendiv", style=tab_style_div1, children=[]),
    ],
)
# %% Layout function

## Specific layouts per username
# def get_layout():
#     try:
#         username = request.authorization["username"]
#         if username == "Enedis":
#             return layoutENEDIS
#         elif username == "Ilot":
#             return layoutIlot
#         elif username == "ICAM":
#             return layoutICAM
#         elif username == "Meteo":
#             return layoutMeteo                
#         else:
#             return reallayout
#     except Exception:
#         return reallayout


# app.layout = get_layout
app.layout=reallayout

# %% Common Callbacks for Datepicker ranges


@app.callback(
    [
        Output("my-date-picker-range-ga-category", "max_date_allowed"),
        Output("my-date-picker-range-ga-category", "end_date"),
        Output("weeklyprev-date-picker-range", "max_date_allowed"),
        Output("weeklyprev-date-picker-range", "end_date"),
        Output("analyse-date-picker-range", "max_date_allowed"),
        Output("analyse-date-picker-range", "end_date"),
        Output("my-date-picker-range-ga-category", "initial_visible_month"),
        Output("weeklyprev-date-picker-range", "initial_visible_month"),
        Output("analyse-date-picker-range", "initial_visible_month"),
        Output("meteo_date_picker", "max_date_allowed"),
        Output("meteo_date_picker", "end_date"),
        Output("meteo_date_picker", "initial_visible_month"),
        Output("SteadySun-date-picker-range", "max_date_allowed"),
        Output("SteadySun-date-picker-range", "end_date"),
        Output("SteadySun-date-picker-range", "initial_visible_month"),
        Output("ICAM_datepicker", "max_date_allowed"),
        Output("ICAM_datepicker", "end_date"),
        Output("ICAM_datepicker", "initial_visible_month"),
        Output("analyse-date-picker-range-icam", "max_date_allowed"),
        Output("analyse-date-picker-range-icam", "end_date"),
        Output("analyse-date-picker-range-icam", "initial_visible_month"),
    ],
    [Input("interval-component2", "n_intervals")],
)
def update_metrics2(n):
    global df
    maxd = df["Date"].max().to_pydatetime() + timedelta(days=1)
    inim = dt(
        df["Date"].max().to_pydatetime().year, df["Date"].max().to_pydatetime().month, 1
    )
    return (
        maxd,
        maxd,
        maxd,
        maxd,
        maxd,
        maxd,
        inim,
        inim,
        inim,
        maxd + timedelta(days=1),  ## meteo date picker.
        maxd + timedelta(days=1),  ## meteo date picker.
        inim,
        maxd,
        maxd,
        inim,
        maxd,
        maxd,
        inim,
        maxd,
        maxd,
        inim,
    )


# %%  Callbacks for Tab "Historique"

## Datepicker range minimum date per DataSet
@app.callback(
    [
        Output("my-date-picker-range-ga-category", "min_date_allowed"),
        # Output("my-date-picker-range-ga-category", "start_date"),
    ],
    [
        Input("ConsoOrPV", "value"),
        Input("yaxis-column", "value"),
    ],
)
def update_Datepicker(sel, yaxis):
    if sel == "CONS":
        min_date_allowed = (dt(2019, 2, 17),)
        # start_date = dt(2019, 2, 17)
    if sel == "PV":
        if yaxis == "Ptot_RIZOMM_PV":
            min_date_allowed = (dt(2018, 9, 16),)
            # start_date = dt(2018, 9, 16)
        else:
            min_date_allowed = (dt(2019, 7, 1),)
            # start_date = dt(2019, 7, 1)
    return min_date_allowed  # , start_date


## Dropdown options per Dataset
@app.callback(
    [Output("yaxis-column", "options"), Output("yaxis-column", "value")],
    [Input("ConsoOrPV", "value")],
)
def update_Dropdown(sel):
    if sel == "CONS":
        available_indicators = (
            df.keys().unique().drop("Date")
        )
        options = [{"label": i, "value": i} for i in available_indicators]
        value = "Ptot_Ilot"
    if sel == "PV":
        available_indicators = (
            df2.keys()
            .unique()
            
            .drop("Date")
            
            .drop("AirTemp")
            .drop("CloudOpacity")
            .drop("Dni")
            .drop("Ghi")
        )
        options = [{"label": i, "value": i} for i in available_indicators]
        value = "Ptot_Ilot_PV"
    return options, value


## Graph per Dataset
@app.callback(
    Output("indicator-graphic", "figure"),
    [
        Input("yaxis-column", "value"),
        Input("my-date-picker-range-ga-category", "start_date"),
        Input("my-date-picker-range-ga-category", "end_date"),
        Input("ConsoOrPV", "value"),
    ],
)
def update_graph(yaxis_column_name, start_date, end_date, sel):
    if sel == "CONS":
        dff = pd.concat([df[yaxis_column_name], df["Date"]], axis=1)
        dff = dff[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
        fig = px.line(
            dff,
            x="Date",
            y=yaxis_column_name,
            render_mode="webgl",
            labels={
                f"{yaxis_column_name}": "Puissance (W)",
            },
            hover_name=dff[yaxis_column_name],
        )
    if sel == "PV":
        dff = dff = pd.concat([df2[yaxis_column_name], df2["Date"]], axis=1)
        dff = dff[(df2["Date"] >= start_date) & (df2["Date"] <= end_date)]
        fig = px.line(
            dff,
            x="Date",
            y=yaxis_column_name,
            render_mode="webgl",
            labels={
                f"{yaxis_column_name}": "Puissance (W)",
            },
            hover_name=dff[yaxis_column_name],
        )
    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")
    return fig




# %%  Callbacks for Tab "Journaliere"

## Graph
@app.callback(
    Output("daily-graph", "figure"),
    [
        Input("interval-component3", "n_intervals"),
        Input("daily-sel", "value"),
    ],
)
def update_metrics3(n, dlsel):
    global dlsel123
    if dlsel:
        dlsel123 = dlsel
    else:
        dlsel = dlsel123
    test12 = affiche[dlsel]
    dfaffiche = None
    global df_merged
    df_mergeddate = None
    df_mergeddate = pd.DataFrame.copy(df_merged)
    if (
        df_mergeddate["Date"][df_mergeddate["Ptot_HA"].last_valid_index()]
        .to_pydatetime()
        .hour
        != pytz.utc.localize(dt.utcnow()).astimezone(tz).hour
    ):
        df_mergeddate["Date"] = df_merged["Date"].apply(
            lambda x: pytz.utc.localize(x).astimezone(tz).replace(tzinfo=None)
        )
    if dlsel == "RIZOMM_PV" or dlsel == "HEI_PV" or dlsel == "Ilot_PV":
        line_dash_map = {
            f"Ptot_{dlsel}": "solid",
            f"Ptot_{test12}_Forecast_Max": "dash",
            f"Ptot_{test12}_Forecast_Min": "dash",
            f"Ptot_{test12}_Forecast_Moy": "dot",
        }
        color_discrete_map = {
            f"Ptot_{dlsel}": "rgb(99,110,250)",
            f"Ptot_{test12}_Forecast_Max": "rgb(239,85,59)",
            f"Ptot_{test12}_Forecast_Min": "rgb(0,204,150)",
            f"Ptot_{test12}_Forecast_Moy": "rgb(171,99,250)",
        }
        dfaffiche = pd.melt(
            df_mergeddate[
                [
                    "Date",
                    f"Ptot_{dlsel}",
                    f"Ptot_{test12}_Forecast_Max",
                    f"Ptot_{test12}_Forecast_Min",
                    f"Ptot_{test12}_Forecast_Moy",
                ]
            ],
            id_vars=["Date"],
        )
        fig = px.line(
            dfaffiche.dropna().sort_values("Date"),
            x="Date",
            y="value",
            color="variable",
            color_discrete_map=color_discrete_map,
            labels={"value": "Puissance (W)"},
            range_y=[0, 1.2 * max(dfaffiche["value"].dropna())],
            line_dash="variable",
            line_dash_map=line_dash_map,
        )
    else:
        if dlsel == "Rizomm_Consommation":
            color_discrete_map = {
                f"Ptot_{test12}": "rgb(99,110,250)",
                f"Ptot_{test12.upper()}_Forecast": "rgb(239,85,59)",
            }
            dfaffiche = pd.melt(
                df_mergeddate[
                    ["Date", f"Ptot_{test12}", f"Ptot_{test12.upper()}_Forecast"]
                ],
                id_vars=["Date"],
            )
            fig = px.line(
                dfaffiche.dropna().sort_values("Date"),
                x="Date",
                y="value",
                color="variable",
                color_discrete_map=color_discrete_map,
                labels={"value": "Puissance (W)"},
                range_y=[0, 1.2 * max(dfaffiche["value"].dropna())],
            )
        else:
            color_discrete_map = {
                f"Ptot_{test12}": "rgb(99,110,250)",
                f"Ptot_{test12}_Forecast": "rgb(239,85,59)",
            }
            dfaffiche = pd.melt(
                df_mergeddate[["Date", f"Ptot_{test12}", f"Ptot_{test12}_Forecast"]],
                id_vars=["Date"],
            )
            fig = px.line(
                dfaffiche.dropna().sort_values("Date"),
                x="Date",
                y="value",
                color="variable",
                color_discrete_map=color_discrete_map,
                labels={"value": "Puissance (W)"},
                range_y=[0, 1.2 * max(dfaffiche["value"].dropna())],
            )

    fig.update_layout(
        uirevision="constant",
        margin={"l": 40, "b": 40, "t": 40, "r": 40},
        hovermode="closest",
    )
    return fig

# %%  Callbacks for Tab "Prevision Historique"

## Graph


@app.callback(
    Output("weekly-prev", "figure"),
    [
        Input("weeklySelect", "value"),
        Input("weeklyprev-date-picker-range", "start_date"),
        Input("weeklyprev-date-picker-range", "end_date"),
    ],
)
def update_graphweekly(dlsel, start_date, end_date):
    test12 = affiche[dlsel]
    dfaffiche = None
    global df_mergedtot
    df_mergedtotdate = pd.DataFrame.copy(df_mergedtot)
    # df_mergedtotdate['Date']=df_mergedtotdate['Date'].apply(lambda x: pytz.utc.localize(x).astimezone(tz).replace(tzinfo=None))
    df_mergedtotdate = df_mergedtotdate[
        (df_mergedtotdate["Date"] >= start_date)
        & (df_mergedtotdate["Date"] <= end_date)
    ]
    if dlsel == "RIZOMM_PV" or dlsel == "HEI_PV" or dlsel == "Ilot_PV":
        line_dash_map = {
            f"Ptot_{dlsel}": "solid",
            f"Ptot_{test12}_Forecast_Max": "dash",
            f"Ptot_{test12}_Forecast_Min": "dash",
            f"Ptot_{test12}_Forecast_Moy": "dot",
        }
        color_discrete_map = {
            f"Ptot_{dlsel}": "rgb(99,110,250)",
            f"Ptot_{test12}_Forecast_Max": "rgb(239,85,59)",
            f"Ptot_{test12}_Forecast_Min": "rgb(0,204,150)",
            f"Ptot_{test12}_Forecast_Moy": "rgb(171,99,250)",
        }
        dfaffiche = pd.melt(
            df_mergedtotdate[
                [
                    "Date",
                    f"Ptot_{dlsel}",
                    f"Ptot_{test12}_Forecast_Max",
                    f"Ptot_{test12}_Forecast_Min",
                    f"Ptot_{test12}_Forecast_Moy",
                ]
            ],
            id_vars=["Date"],
        )
        fig = px.line(
            dfaffiche.dropna().sort_values("Date"),
            x="Date",
            y="value",
            color="variable",
            color_discrete_map=color_discrete_map,
            labels={"value": "Puissance (W)"},
            range_y=[1.2 * min(dfaffiche["value"].dropna()), 1.2 * max(dfaffiche["value"].dropna())],
            line_dash="variable",
            line_dash_map=line_dash_map,
        )
    else:
        if dlsel == "Rizomm_Consommation":
            color_discrete_map = {
                f"Ptot_{test12.upper()}": "rgb(99,110,250)",
                f"Ptot_{test12.upper()}_Forecast": "rgb(239,85,59)",
            }
            dfaffiche = pd.melt(
                df_mergedtotdate[
                    [
                        "Date",
                        f"Ptot_{test12.upper()}",
                        f"Ptot_{test12.upper()}_Forecast",
                    ]
                ],
                id_vars=["Date"],
            )
            fig = px.line(
                dfaffiche.dropna().sort_values("Date"),
                x="Date",
                y="value",
                color="variable",
                color_discrete_map=color_discrete_map,
                labels={"value": "Puissance (W)"},
                range_y=[1.2 * min(dfaffiche["value"].dropna()), 1.2 * max(dfaffiche["value"].dropna())],
            )
        else:
            color_discrete_map = {
                f"Ptot_{test12}": "rgb(99,110,250)",
                f"Ptot_{test12}_Forecast": "rgb(239,85,59)",
            }
            dfaffiche = pd.melt(
                df_mergedtotdate[["Date", f"Ptot_{test12}", f"Ptot_{test12}_Forecast"]],
                id_vars=["Date"],
            )
            fig = px.line(
                dfaffiche.dropna().sort_values("Date"),
                x="Date",
                y="value",
                color="variable",
                color_discrete_map=color_discrete_map,
                labels={"value": "Puissance (W)"},
                range_y=[1.2 * min(dfaffiche["value"].dropna()), 1.2 * max(dfaffiche["value"].dropna())],
            )

    fig.update_layout(margin={"l": 40, "b": 40, "t": 40, "r": 40}, hovermode="closest")
    return fig



# %%  Callbacks for Tab "Semaine"

## Graph


@app.callback(
    Output("7day-graph", "figure"),
    [Input("7day-sel", "value"), Input("interval-component3", "n_intervals")],
)
def update_graph7week(yaxis_column_name, n):
    if yaxis_column_name == "Ptot_HEI_PV":
        dfaffiche2 = pd.melt(
            dfpvprev2[
                [
                    "Date",
                    "Ptot_HEI_5RNS_Forecast_Min",
                    "Ptot_HEI_5RNS_Forecast_Moy",
                    "Ptot_HEI_5RNS_Forecast_Max",
                ]
            ],
            id_vars=["Date"],
        )
    elif yaxis_column_name == "Ptot_RIZOMM_PV":
        dfaffiche2 = pd.melt(
            dfpvprev2[
                [
                    "Date",
                    "Ptot_RIZOMM_PV_Forecast_Min",
                    "Ptot_RIZOMM_PV_Forecast_Moy",
                    "Ptot_RIZOMM_PV_Forecast_Max",
                ]
            ],
            id_vars=["Date"],
        )
    elif yaxis_column_name == "Ptot_Ilot_PV":
        dfaffiche2 = pd.melt(
            dfpvprev2[
                [
                    "Date",
                    "Ptot_Ilot_PV_Forecast_Min",
                    "Ptot_Ilot_PV_Forecast_Moy",
                    "Ptot_Ilot_PV_Forecast_Max",
                ]
            ],
            id_vars=["Date"],
        )
    fig = px.line(
        dfaffiche2.dropna().sort_values("Date"),
        x="Date",
        y="value",
        color="variable",
        labels={"value": "Puissance (W)"},
        range_y=[0, 1.2 * max(dfaffiche2["value"].dropna())],
    )
    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")
    return fig




# %%  Callbacks for Tab "Analyse Historique"

## Graph


@app.callback(
    Output("analyse-graph", "figure"),
    # Output("analyse-graph-reports", "figure"),
    [
        Input("CheckID", "value"),
        Input("analyse-date-picker-range", "start_date"),
        Input("analyse-date-picker-range", "end_date"),
    ],
)
def update_graph1(chckl, start_date, end_date):
    fig = go.Figure()
    global df_mergedtot2
    global affiche
    global affiche2
    df_mergedtotdate2 = None
    df_mergedtotdate2 = pd.DataFrame.copy(df_mergedtot2)
    df_mergedtotdate2 = df_mergedtotdate2[
        (df_mergedtotdate2["Date"] >= start_date)
        & (df_mergedtotdate2["Date"] <= end_date)
    ]
    dateasnumpy=np.datetime_as_string(df_mergedtotdate2["Date"].to_numpy())
    for data in chckl:
        if data in dailylabel:
            if data == "Rizomm_Consommation":
                fig.add_trace(
                    go.Scattergl(
                        x=dateasnumpy,
                        y=df_mergedtotdate2[f"Ptot_{affiche[data].upper()}"].to_numpy(),
                        name=f"{affiche[data]}",
                    ),
                    # secondary_y=False,
                )
            elif data == "HEI_PV":
                fig.add_trace(
                    go.Scattergl(
                        x=dateasnumpy,
                        y=df_mergedtotdate2[f"Ptot_{data}"].to_numpy(),
                        name=f"{data}",
                    ),
                    # secondary_y=False,
                )
            else:
                fig.add_trace(
                    go.Scattergl(
                        x=dateasnumpy,
                        y=df_mergedtotdate2[f"Ptot_{affiche[data]}"].to_numpy(),
                        name=f"{affiche[data]}",
                    ),
                    # secondary_y=False,
                )
        elif data == "ICL_conso" or data == "Junia_conso":
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{affiche2[data]}",
                ),
                # secondary_y=False,
            )
        elif data == "temp" or data == "AirTemp":
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{affichetemp[data]}",
                    yaxis="y4",
                ),
            )
            fig.update_layout(
                yaxis4=dict(
                    title="Température(°C)",
                    anchor="free",
                    overlaying="y",
                    side="right",
                    position=0.9,
                ),
            )
        elif data in irradlabel:
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{afficheirr[data]}",
                    yaxis="y2",
                ),
            )
            fig.update_layout(
                yaxis2=dict(
                    title="Irradiation(W/m2)",
                    anchor="free",
                    overlaying="y",
                    side="left",
                    position=0.05,
                ),
            )

        elif data in icamlabel:
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{afficheicam[data]}",
                ),
                # secondary_y=False,
            )

        else:
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{affiche2[data]}",
                    yaxis="y3",
                ),
                # secondary_y=True,
            )
            fig.update_layout(
                yaxis3=dict(
                    title="Pourcentage(%)",
                    anchor="free",
                    overlaying="y",
                    side="right",
                    position=0.95,
                ),
            )
    fig.update_xaxes(title_text="Date")
    fig.update_layout(
        xaxis=dict(domain=[0.1, 0.9]), yaxis=dict(title_text="Puissance(W)")
    )
    # fig.update_yaxes(title_text="Puissance (W)")
    # fig.update_yaxes(title_text="Pourcentage", secondary_y=True)
    return fig  # , fig


# %%  Callbacks for Tab "Comparaison SteadySun"


## Journ Tab Graph


@app.callback(
    Output("SS_Journ_graph", "figure"),
    [
        Input("interval-component3", "n_intervals"),
        Input("SSJour_HEI_Rizo", "value"),
        Input("SSJour_Mod", "value"),
        Input("SSJour_MinMax", "value"),
    ],
)
def update_metricsSSjourn(n, sel1, sel2, sel3):
    global df_merged
    df_mergeddate = None
    df_mergeddate = pd.DataFrame.copy(df_merged)
    if (
        df_mergeddate["Date"][df_mergeddate["Ptot_HA"].last_valid_index()]
        .to_pydatetime()
        .hour
        != pytz.utc.localize(dt.utcnow()).astimezone(tz).hour
    ):
        df_mergeddate["Date"] = df_merged["Date"].apply(
            lambda x: pytz.utc.localize(x).astimezone(tz).replace(tzinfo=None)
        )
    Tlist = []
    unwanted = []
    for sel in (sel1, sel2, sel3):
        if isinstance(sel, list):
            unwanted += sel
        else:
            unwanted.append(sel)
    badlist = [
        "RIZOMM",
        "HEI",
        "_Forecast_",
        "_ForecastSS_",
        "_ForecastSE_",
        "Max",
        "Moy",
        "Min",
    ]
    badlist = [e for e in badlist if e not in unwanted]
    for x in SSlist:
        count = 0
        if badlist:
            for e in badlist:
                if e in x:
                    count += 1
        if count == 0:
            Tlist.append(x)
    dfaffiche = pd.melt(df_mergeddate[Tlist], id_vars=["Date"])
    fig = px.line(
        dfaffiche.dropna().sort_values("Date"),
        x="Date",
        y="value",
        color="variable",
        labels={"value": "Puissance (W)"},
        range_y=[1.2 * min(dfaffiche["value"].dropna()), 1.2 * max(dfaffiche["value"].dropna())],
        line_dash="variable",
        line_dash_map=line_dash_mapSS,
    )
    fig.update_layout(margin={"l": 40, "b": 40, "t": 40, "r": 40}, hovermode="closest")
    return fig


## Hist Tab Graph


@app.callback(
    Output("SS_hist_graph", "figure"),
    [
        Input("interval-component3", "n_intervals"),
        Input("SSHist_HEI_Rizo", "value"),
        Input("SSHist_Mod", "value"),
        Input("SSHist_MinMax", "value"),
        Input("SteadySun-date-picker-range", "start_date"),
        Input("SteadySun-date-picker-range", "end_date"),
    ],
)
def update_metricsSShist(n, sel1, sel2, sel3, start_date, end_date):
    global df_mergedtot
    df_mergeddate2 = None
    df_mergeddate2 = pd.DataFrame.copy(df_mergedtot)
    df_mergeddate2 = df_mergeddate2[
        (df_mergeddate2["Date"] >= start_date) & (df_mergeddate2["Date"] <= end_date)
    ]
    Tlist = []
    unwanted = []
    for sel in (sel1, sel2, sel3):
        if isinstance(sel, list):
            unwanted += sel
        else:
            unwanted.append(sel)
    badlist = [
        "RIZOMM",
        "HEI",
        "_Forecast_",
        "_ForecastSS_",
        "_ForecastSE_",
        "Max",
        "Moy",
        "Min",
    ]
    badlist = [e for e in badlist if e not in unwanted]
    for x in SSlist:
        count = 0
        if badlist:
            for e in badlist:
                if e in x:
                    count += 1
        if count == 0:
            Tlist.append(x)
    dfaffiche = pd.melt(df_mergeddate2[Tlist], id_vars=["Date"])
    fig = px.line(
        dfaffiche.dropna().sort_values("Date"),
        x="Date",
        y="value",
        color="variable",
        labels={"value": "Puissance (W)"},
        range_y=[ 1.2 * min(dfaffiche["value"].dropna()), 1.2 * max(dfaffiche["value"].dropna())],
        line_dash="variable",
        line_dash_map=line_dash_mapSS,
    )
    fig.update_layout(margin={"l": 40, "b": 40, "t": 40, "r": 40}, hovermode="closest")
    return fig


## comparaison steadyeye Tab Table


@app.callback(
    Output("tableSS", "data"),
    [
        Input("interval-component3", "n_intervals"),
        Input("SteadySun-date-picker-range", "start_date"),
        Input("SteadySun-date-picker-range", "end_date"),
    ],
)
def update_metricsSShistTable(n, start_date, end_date):
    global df_mergedtot
    df_mergeddate2 = None
    df_mergeddate2 = pd.DataFrame.copy(df_mergedtot)
    df_mergeddate2 = df_mergeddate2[
        (df_mergeddate2["Date"] >= start_date) & (df_mergeddate2["Date"] <= end_date)
    ]
    minHei = min(df_mergedtot["Ptot_HEI_PV"].dropna())
    maxHei = max(df_mergedtot["Ptot_HEI_PV"].dropna())
    minRizo = min(df_mergedtot["Ptot_RIZOMM_PV"].dropna())
    maxRizo = max(df_mergedtot["Ptot_RIZOMM_PV"].dropna())
    data = []

    def Genres(df_mergeddate2, forc, build, minh, maxh, mod):
        dff = pd.concat(
            [df_mergeddate2[forc], df_mergeddate2["Date"], df_mergeddate2[build]],
            axis=1,
        )
        dff.dropna(inplace=True)
        EVS = np.round(explained_variance_score(dff[build], dff[forc]), 2)
        MAE = np.round(mean_absolute_error(dff[build], dff[forc]), 2)
        RMSE = np.round(mean_squared_error(dff[build], dff[forc], squared=False), 2)
        nMAE = MAE#f"{round((MAE- minh)/(maxh-minh),4)*100:.2f}"
        nRMSE = RMSE#f"{round((RMSE- minh)/(maxh-minh),4)*100:.2f}"
        return {
            "Modèle": mod,
            "RMSE (W)": RMSE,
            """nRMSE (%)""": nRMSE,
            "MAE (W)": MAE,
            """nMAE (%)""": nMAE,
            "Explained_Variance_Score": EVS,
            "Date Début Comparaison": min(dff["Date"]),
        }

    data.append(
        Genres(
            df_mergeddate2,
            "Ptot_HEI_5RNS_ForecastSE_Moy",
            "Ptot_HEI_PV",
            minHei,
            maxHei,
            "Steady_Eye_HEI",
        )
    )
    data.append(
        Genres(
            df_mergeddate2,
            "Ptot_HEI_5RNS_ForecastSS_Moy",
            "Ptot_HEI_PV",
            minHei,
            maxHei,
            "Steady_Sat_HEI",
        )
    )
    data.append(
        Genres(
            df_mergeddate2,
            "Ptot_HEI_5RNS_Forecast_Moy",
            "Ptot_HEI_PV",
            minHei,
            maxHei,
            "Neurones_HEI",
        )
    )
    data.append(
        Genres(
            df_mergeddate2,
            "Ptot_RIZOMM_PV_ForecastSE_Moy",
            "Ptot_RIZOMM_PV",
            minRizo,
            maxRizo,
            "Steady_Eye_Rizomm",
        )
    )
    data.append(
        Genres(
            df_mergeddate2,
            "Ptot_RIZOMM_PV_ForecastSS_Moy",
            "Ptot_RIZOMM_PV",
            minRizo,
            maxRizo,
            "Steady_Sat_Rizomm",
        )
    )
    data.append(
        Genres(
            df_mergeddate2,
            "Ptot_RIZOMM_PV_Forecast_Moy",
            "Ptot_RIZOMM_PV",
            minRizo,
            maxRizo,
            "Neurones_Rizomm",
        )
    )

    return data


## card group + wind direction update
@app.callback(
    [
        Output("solirr_card", "children"),
        Output("humidity_card", "children"),
        Output("temp_card", "children"),
        Output("pressure_card", "children"),
        Output("wind_card", "children"),
        Output("wind_direction_graph", "figure"),
    ],
    [
        Input("interval_meteo_2mins", "n_intervals"),
    ],
)
def updatemeteo(n):
    global dfmeteoinst
    global dfmeteo
    fig = go.Figure()
    # Add trace

    fig.add_trace(
        go.Barpolar(
            r=[dfmeteoinst["windspeed"]],
            theta=[dfmeteoinst["winddirection"]],
            marker_color="rgb(135,206,250)",
            dr=0,
            width=10,
        )
    )
    # Add images
    fig.add_layout_image(
        dict(
            source=f"data:image/png;base64,{encoded_string_meteo_image}",
            xref="x",
            yref="y",
            x=-2,
            y=4,
            sizex=9.5,
            sizey=9.5,
            sizing="contain",
            opacity=1,
            layer="below",
        )
    )
    # fig.update_polars(radialaxis_showticklabels=False)
    # Set templates
    fig.update_layout(
        yaxis_visible=False,
        xaxis_visible=False,
        yaxis_showticklabels=False,
        xaxis_showticklabels=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_text="<b>Direction du Vent<b>",
        title_xanchor="center",
        title_xref="paper",
        title_x=0.5,
        title_yanchor="bottom",
        title_y=0,
        title_font_size=20,
    )  # polar=dict(sector=[n-3,n+3]),)
    fig.update_polars(
        radialaxis_showticklabels=False,
        radialaxis_showline=False,
        angularaxis_showgrid=False,
        angularaxis_showticklabels=True,
        radialaxis_showgrid=False,
        bgcolor="rgba(0,0,0,0)",
        angularaxis_rotation=90 + 180,
        angularaxis_direction="clockwise",
        angularaxis_ticktext=["N", "E", "S", "O"],
        angularaxis_tickmode="array",
        angularaxis_tickvals=[180, 270, 0, 90],
        angularaxis_tickfont_size=25,
        angularaxis_linecolor="rgba(0,0,0,0)",
    )
    return (
        f"{dfmeteoinst['solirr']:.0f} W/m",
        f"{dfmeteoinst['relhumid']:.1f}%",
        f"{dfmeteoinst['temp']:.1f}℃",
        f"{dfmeteoinst['pressatm']:.2f}hPa",
        f"{dfmeteoinst['windspeed']:.2f}m/s",
        fig,
    )


## rain card update
@app.callback(
    [Output("rain_card", "children")],
    [
        Input("interval_meteo_2mins", "n_intervals"),
        Input("rain_dropdown", "value"),
    ],
)
def updaterain(n, deltahours):
    global dfmeteo
    lastrain = dfmeteo[
        dfmeteo["Date"] >= dt.utcnow() - timedelta(hours=int(deltahours))
    ]["instarain"].sum()
    return [f"{lastrain:.3f}mm"]


## graphs
@app.callback(
    [
        Output("temp_graph", "figure"),
        Output("IRR_graph", "figure"),
        Output("rain_graph", "figure"),
        Output("wind_graph", "figure"),
    ],
    [
        Input("meteo_date_picker", "start_date"),
        Input("meteo_date_picker", "end_date"),
    ],
)
def generategraphs(start, end):
    # a=perf_counter()
    global dfmeteo
    dfmeteodate = pd.DataFrame.copy(dfmeteo)
    dfmeteodate = dfmeteodate[
        (dfmeteodate["Date"] >= start) & (dfmeteodate["Date"] <= end)
    ]
    if len(dfmeteodate)>8000 and len(dfmeteodate)<20000:
        saverain=dfmeteodate.set_index("Date")["instarain"].resample('10Min').sum()
        dfmeteodate=dfmeteodate.set_index("Date").resample('10Min').mean()
        
        dfmeteodate["instarain"]=saverain
        dfmeteodate.reset_index(inplace=True)
    if len(dfmeteodate)>8000:
        saverain=dfmeteodate.set_index("Date")["instarain"].resample('H').sum()
        dfmeteodate=dfmeteodate.set_index("Date").resample('H').mean()
        
        dfmeteodate["instarain"]=saverain
        dfmeteodate.reset_index(inplace=True)
    dateasnumpy=np.datetime_as_string(dfmeteodate["Date"].to_numpy())
    figtemp = make_subplots(specs=[[{"secondary_y": True}]])
    figtemp.add_trace(
        go.Scattergl(x=dateasnumpy, y=dfmeteodate["temp"].to_numpy(), name="Température(℃)"),
        secondary_y=False,
    )
    figtemp.add_trace(
        go.Scattergl(
            x=dateasnumpy,
            y=dfmeteodate["relhumid"].to_numpy(),
            name="Humidité Relative(%)",
        ),
        secondary_y=True,
    )
    figirr = make_subplots(specs=[[{"secondary_y": False}]])
    figirr.add_trace(
        go.Scattergl(
            x=dateasnumpy,
            y=dfmeteodate["solirr"].to_numpy(),
            name="Irradiation Solaire(W/m2)",
        )
    )
    figrain = make_subplots(specs=[[{"secondary_y": False}]])
    figrain.add_trace(
        go.Bar(
            x=dateasnumpy,
            y=dfmeteodate["instarain"].to_numpy(),
            name="Quantité de Pluie(mm)",
        )
    )
    figrain.update_traces(dict(marker_line_width=0))
    figwind = make_subplots(specs=[[{"secondary_y": False}]])
    figwind.add_trace(
        go.Scattergl(
            x=dateasnumpy,
            y=dfmeteodate["windspeed"].to_numpy(),
            name="Vitesse du vent(m/s)",
        )
    )
    figwind.add_trace(
        go.Scattergl(
            x=dateasnumpy,
            y=dfmeteodate["windgustspeed"].to_numpy(),
            name="Vitesse des rafales de vent(m/s)",
        )
    )
    figtemp.update_xaxes(title_text="Date")
    figtemp.update_yaxes(title_text="Température(℃)", secondary_y=False)
    figtemp.update_yaxes(title_text="Humidité Relative(%)", secondary_y=True)

    figirr.update_xaxes(title_text="Date")
    figirr.update_yaxes(title_text="Irradiation Solaire(W/m2)")

    figrain.update_xaxes(title_text="Date")
    figrain.update_yaxes(title_text="Quantité de Pluie(mm)", secondary_y=False)

    figwind.update_xaxes(title_text="Date")
    figwind.update_yaxes(title_text="Vitesse(m/s)", secondary_y=False)
    # print(perf_counter()-a)
    return figtemp, figirr, figrain, figwind


#%%
## ICAM CALLBACKS

## Historique
@app.callback(
    Output("histo-graph-icam", "figure"),
    [
        Input("historique-sel-icam", "value"),
        Input("ICAM_datepicker", "start_date"),
        Input("ICAM_datepicker", "end_date"),
    ],
)
def update_graph(sel_value, start_date, end_date):
    global dficam
    fig = go.Figure()
    # dficamloc = pd.DataFrame.copy(dficam)
    dficamloc = dficam[(dficam["Date"] >= start_date) & (dficam["Date"] <= end_date)]
    fig.add_trace(
        go.Scatter(
            x=dficamloc["Date"],
            y=dficamloc[f"{sel_value}"],
            name=f"{sel_value}",
        )
    )
    fig.update_xaxes(title_text="Date")
    if sel_value == "Etot_ICAM_Capacity" or sel_value == "Etot_ICAM_Remaining":
        fig.update_layout(yaxis=dict(title_text="Énergie(Wh)"))
    else:
        fig.update_layout(yaxis=dict(title_text="Puissance(W)"))
    fig.update_layout(
        uirevision="constant",
        margin={"l": 40, "b": 40, "t": 10, "r": 0},
        hovermode="closest",
    )
    return fig

## journaliere


@app.callback(
    Output("daily-graph-icam", "figure"),
    [
        Input("daily-sel-icam", "value"),
    ],
)
def update_graph(sel_value):
    global dfjourIC
    if "Etot_ICAM_Capacity" or "Etot_ICAM_Remaining" in sel_value:
        fig = make_subplots(specs=[[{"secondary_y": True}]])
    else:
        fig = go.Figure()
    # dficamloc = pd.DataFrame.copy(dficam)
    for sel in sel_value:
        if sel == "Etot_ICAM_Capacity" or sel == "Etot_ICAM_Remaining":
            fig.add_trace(
                go.Scatter(
                    x=dfjourIC["Date"],
                    y=dfjourIC[f"{sel}"],
                    name=f"{sel}",
                ),
                secondary_y=True,
            )
        else:
            fig.add_trace(
                go.Scatter(
                    x=dfjourIC["Date"],
                    y=dfjourIC[f"{sel}"],
                    name=f"{sel}",
                ),
                secondary_y=False,
            )
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Puissance(W)", secondary_y=False)
    fig.update_yaxes(title_text="Énergie(Wh)", secondary_y=True)
    fig.update_layout(
        uirevision="constant",
        margin={"l": 40, "b": 40, "t": 10, "r": 0},
        hovermode="closest",
    )
    return fig


## Analyse ICAM
@app.callback(
    Output("analyse-graph-icam", "figure"),
    # Output("analyse-graph-reports", "figure"),
    [
        Input("CheckID_icam", "value"),
        Input("analyse-date-picker-range-icam", "start_date"),
        Input("analyse-date-picker-range-icam", "end_date"),
    ],
)
def update_graph1(chckl, start_date, end_date):
    fig = go.Figure()
    global df_mergedtot2
    global affiche
    global affiche2
    df_mergedtotdate2 = None
    df_mergedtotdate2 = pd.DataFrame.copy(df_mergedtot2)
    df_mergedtotdate2 = df_mergedtotdate2[
        (df_mergedtotdate2["Date"] >= start_date)
        & (df_mergedtotdate2["Date"] <= end_date)
    ]
    dateasnumpy=np.datetime_as_string(df_mergedtotdate2["Date"].to_numpy())
    for data in chckl:
        if data in dailylabel:
            if data == "Rizomm_Consommation":
                fig.add_trace(
                    go.Scattergl(
                        x=dateasnumpy,
                        y=df_mergedtotdate2[f"Ptot_{affiche[data].upper()}"].to_numpy(),
                        name=f"{affiche[data]}",
                    ),
                    # secondary_y=False,
                )
            elif data == "HEI_PV":
                fig.add_trace(
                    go.Scattergl(
                        x=dateasnumpy,
                        y=df_mergedtotdate2[f"Ptot_{data}"].to_numpy(),
                        name=f"{data}",
                    ),
                    # secondary_y=False,
                )
            else:
                fig.add_trace(
                    go.Scattergl(
                        x=dateasnumpy,
                        y=df_mergedtotdate2[f"Ptot_{affiche[data]}"].to_numpy(),
                        name=f"{affiche[data]}",
                    ),
                    # secondary_y=False,
                )
        elif data == "ICL_conso" or data == "Junia_conso":
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{affiche2[data]}",
                ),
                # secondary_y=False,
            )
        elif data == "temp" or data == "AirTemp":
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{affichetemp[data]}",
                    yaxis="y4",
                ),
            )
            fig.update_layout(
                yaxis4=dict(
                    title="Température(°C)",
                    anchor="free",
                    overlaying="y",
                    side="right",
                    position=0.9,
                ),
            )
        elif data in irradlabel:
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{afficheirr[data]}",
                    yaxis="y2",
                ),
            )
            fig.update_layout(
                yaxis2=dict(
                    title="Irradiation(W/m2)",
                    anchor="free",
                    overlaying="y",
                    side="left",
                    position=0.05,
                ),
            )

        elif data in icamlabel:
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{afficheicam[data]}",
                ),
                # secondary_y=False,
            )

        else:
            fig.add_trace(
                go.Scattergl(
                    x=dateasnumpy,
                    y=df_mergedtotdate2[data].to_numpy(),
                    name=f"{affiche2[data]}",
                    yaxis="y3",
                ),
                # secondary_y=True,
            )
            fig.update_layout(
                yaxis3=dict(
                    title="Pourcentage(%)",
                    anchor="free",
                    overlaying="y",
                    side="right",
                    position=0.95,
                ),
            )
    fig.update_xaxes(title_text="Date")
    fig.update_layout(
        xaxis=dict(domain=[0.1, 0.9]), yaxis=dict(title_text="Puissance(W)")
    )
    # fig.update_yaxes(title_text="Puissance (W)")
    # fig.update_yaxes(title_text="Pourcentage", secondary_y=True)
    return fig  # , fig


# %% Main
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", threaded=True)
    
