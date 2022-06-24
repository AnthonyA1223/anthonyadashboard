SElist = [
    "Ptot_HEI_5RNS_ForecastSE_Max",
    "Ptot_HEI_5RNS_ForecastSE_Min",
    "Ptot_HEI_5RNS_ForecastSE_Moy",
    "Ptot_RIZOMM_PV_ForecastSE_Max",
    "Ptot_RIZOMM_PV_ForecastSE_Min",
    "Ptot_RIZOMM_PV_ForecastSE_Moy",
]

Tablelist = [
    "Modèle",
    "RMSE (W)",
    """nRMSE (%)""",
    "MAE (W)",
    """nMAE (%)""",
    "Explained_Variance_Score",
    "Date Début Comparaison",
]


SSlist = [
    "Date",
    "Ptot_HEI_5RNS_ForecastSE_Max",
    "Ptot_HEI_5RNS_ForecastSE_Min",
    "Ptot_HEI_5RNS_ForecastSE_Moy",
    "Ptot_HEI_5RNS_ForecastSS_Max",
    "Ptot_HEI_5RNS_ForecastSS_Min",
    "Ptot_HEI_5RNS_ForecastSS_Moy",
    "Ptot_RIZOMM_PV_ForecastSE_Max",
    "Ptot_RIZOMM_PV_ForecastSE_Min",
    "Ptot_RIZOMM_PV_ForecastSE_Moy",
    "Ptot_RIZOMM_PV_ForecastSS_Max",
    "Ptot_RIZOMM_PV_ForecastSS_Min",
    "Ptot_RIZOMM_PV_ForecastSS_Moy",
    "Ptot_HEI_5RNS_Forecast_Max",
    "Ptot_HEI_5RNS_Forecast_Min",
    "Ptot_HEI_5RNS_Forecast_Moy",
    "Ptot_RIZOMM_PV_Forecast_Max",
    "Ptot_RIZOMM_PV_Forecast_Min",
    "Ptot_RIZOMM_PV_Forecast_Moy",
    "Ptot_HEI_PV",
    "Ptot_RIZOMM_PV",
]

line_dash_mapSS = {
    "Ptot_HEI_5RNS_ForecastSE_Max": "dash",
    "Ptot_HEI_5RNS_ForecastSE_Min": "dash",
    "Ptot_HEI_5RNS_ForecastSE_Moy": "solid",
    "Ptot_HEI_5RNS_ForecastSS_Max": "dash",
    "Ptot_HEI_5RNS_ForecastSS_Min": "dash",
    "Ptot_HEI_5RNS_ForecastSS_Moy": "solid",
    "Ptot_RIZOMM_PV_ForecastSE_Max": "dash",
    "Ptot_RIZOMM_PV_ForecastSE_Min": "dash",
    "Ptot_RIZOMM_PV_ForecastSE_Moy": "solid",
    "Ptot_RIZOMM_PV_ForecastSS_Max": "dash",
    "Ptot_RIZOMM_PV_ForecastSS_Min": "dash",
    "Ptot_RIZOMM_PV_ForecastSS_Moy": "solid",
    "Ptot_HEI_5RNS_Forecast_Max": "dash",
    "Ptot_HEI_5RNS_Forecast_Min": "dash",
    "Ptot_HEI_5RNS_Forecast_Moy": "solid",
    "Ptot_RIZOMM_PV_Forecast_Max": "dash",
    "Ptot_RIZOMM_PV_Forecast_Min": "dash",
    "Ptot_RIZOMM_PV_Forecast_Moy": "solid",
    "Ptot_HEI_PV": "solid",
    "Ptot_RIZOMM_PV": "solid",
}

dailylabel = [
    "HA_Consommation",
    "HEI_13RT_Consommation",
    "HEI_5RNS_Consommation",
    "Rizomm_Consommation",
    "Ilot_Consommation",
    "Ilot_PV",
    "RIZOMM_PV",
    "HEI_PV",
]

affiche = {
    "RIZOMM_PV": "RIZOMM_PV",
    "HEI_PV": "HEI_5RNS",
    "HA_Consommation": "HA",
    "HEI_13RT_Consommation": "HEI_13RT",
    "HEI_5RNS_Consommation": "HEI_5RNS",
    "Rizomm_Consommation": "Rizomm",
    "Ilot_Consommation": "Ilot",
    "Ilot_PV": "Ilot_PV",
}

affiche2 = {
    "ACR": "AutoConso Rizomm",
    "APR": "AutoProd Rizomm",
    "ACH": "AutoConso HEI",
    "APH": "AutoProd HEI",
    "ACRH": "AutoConso Rizomm et HA",
    "APRH": "AutoProd Rizomm et HA",
    "ACT": "AutoConso Totale",
    "APT": "AutoProd Totale",
    "Junia_conso": "Junia",
    "ICL_conso": "ICL",
}
config = {
    "toImageButtonOptions": {"width": None, "height": None}
}  ## for graph to image scaling.

tab_style_div1 = {
    "testAlign": "left",
    "padding": "70px 0px",
    "position": "absolute",
    "height": "0%",
    "width": "0%",
}

analyse_tab_checklist = [
    {
        "label": "Conso HA",
        "value": "HA_Consommation",
    },
    {
        "label": "Conso HEI_13RT",
        "value": "HEI_13RT_Consommation",
    },
    {
        "label": "Conso HEI_5RNS",
        "value": "HEI_5RNS_Consommation",
    },
    {
        "label": "Conso Rizomm",
        "value": "Rizomm_Consommation",
    },
    {
        "label": "Conso ICL",
        "value": "ICL_conso",
    },
    {
        "label": "Conso Junia",
        "value": "Junia_conso",
    },
    {
        "label": "Conso Ilot",
        "value": "Ilot_Consommation",
    },
    {
        "label": "PV Ilot",
        "value": "Ilot_PV",
    },
    {
        "label": "PV HEI",
        "value": "HEI_PV",
    },
    {
        "label": "PV Rizomm",
        "value": "RIZOMM_PV",
    },
    {
        "label": "AutoConso Rizomm",
        "value": "ACR",
    },
    {
        "label": "AutoProd Rizomm",
        "value": "APR",
    },
    {
        "label": "AutoConso HEI",
        "value": "ACH",
    },
    {
        "label": "AutoProd HEI",
        "value": "APH",
    },
    {
        "label": "AutoConso Rizomm et HA",
        "value": "ACRH",
    },
    {
        "label": "AutoProd Rizomm et HA",
        "value": "APRH",
    },
    {
        "label": "AutoConso Totale",
        "value": "ACT",
    },
    {
        "label": "AutoProd Totale",
        "value": "APT",
    },
    {
        "label": "Irradiation Station Météo",
        "value": "solirr",
    },
    {
        "label": "GHI Prévision Météo",
        "value": "GhiMoy",
    },
    {
        "label": "DNI Prévision Météo",
        "value": "DniMoy",
    },
    {
        "label": "GHI Historique Météo",
        "value": "Ghi",
    },
    {
        "label": "DNI Historique Météo",
        "value": "Dni",
    },
    {
        "label": "Température Station Météo",
        "value": "temp",
    },
    {
        "label": "Température Prévision Météo",
        "value": "AirTemp",
    },
    {
        "label": "Production ICAM PV",
        "value": "Ptot_ICAM_PV",
    },
    {
        "label": "Consommation ICAM Totale",
        "value": "Ptot_Ilot_ICAM",
    },
    {
        "label": "Consommation ICAM Batiment",
        "value": "Ptot_Bat",
    },
    {
        "label": "Consommation ICAM atelier",
        "value": "Ptot_ICAM_Transfo_250KVA",
    },
    {
        "label": "Consommation ICAM Maison",
        "value": "Ptot_ICAM_MI",
    },
    {
        "label": "ICAM Battery Restant",
        "value": "Etot_ICAM_Remaining",
    },
    {
        "label": "ICAM Battery Puissance",
        "value": "Ptot_ICAM_Batt",
    },
    {
        "label": "Consommation ICAM EDF",
        "value": "Ptot_ICAM_EDF",
    },
]

analyse_tab_checklist_ICAM = [
    {
        "label": "Conso HA",
        "value": "HA_Consommation",
    },
    {
        "label": "Conso HEI_13RT",
        "value": "HEI_13RT_Consommation",
    },
    {
        "label": "Conso HEI_5RNS",
        "value": "HEI_5RNS_Consommation",
    },
    {
        "label": "Conso Rizomm",
        "value": "Rizomm_Consommation",
    },
    {
        "label": "Conso ICL",
        "value": "ICL_conso",
    },
    {
        "label": "Conso Junia",
        "value": "Junia_conso",
    },
    {
        "label": "Conso Ilot",
        "value": "Ilot_Consommation",
    },
    {
        "label": "PV Ilot",
        "value": "Ilot_PV",
    },
    {
        "label": "PV HEI",
        "value": "HEI_PV",
    },
    {
        "label": "PV Rizomm",
        "value": "RIZOMM_PV",
    },
    {
        "label": "Irradiation Station Météo",
        "value": "solirr",
    },
    {
        "label": "GHI Prévision Météo",
        "value": "GhiMoy",
    },
    {
        "label": "DNI Prévision Météo",
        "value": "DniMoy",
    },
    {
        "label": "GHI Historique Météo",
        "value": "Ghi",
    },
    {
        "label": "DNI Historique Météo",
        "value": "Dni",
    },
    {
        "label": "Température Station Météo",
        "value": "temp",
    },
    {
        "label": "Température Prévision Météo",
        "value": "AirTemp",
    },
    {
        "label": "Production ICAM PV",
        "value": "Ptot_ICAM_PV",
    },
    {
        "label": "Consommation ICAM Totale",
        "value": "Ptot_Ilot_ICAM",
    },
    {
        "label": "Consommation ICAM Batiment",
        "value": "Ptot_Bat",
    },
    {
        "label": "Consommation ICAM atelier",
        "value": "Ptot_ICAM_Transfo_250KVA",
    },
    {
        "label": "Consommation ICAM Maison",
        "value": "Ptot_ICAM_MI",
    },
    {
        "label": "ICAM Battery Restant",
        "value": "Etot_ICAM_Remaining",
    },
    {
        "label": "ICAM Battery Puissance",
        "value": "Ptot_ICAM_Batt",
    },
    {
        "label": "Consommation ICAM EDF",
        "value": "Ptot_ICAM_EDF",
    },
]


afficheirr = {
    "GhiMoy": "GHI Prévision Météo",
    "DniMoy": "DNI Prévision Météo",
    "Ghi": "GHI Historique Météo",
    "Dni": "DNI Historique Météo",
    "solirr": "Irradiation Station Météo",
}


irradlabel = ["GhiMoy", "DniMoy", "Ghi", "Dni", "solirr"]


affichetemp = {
    "temp": "Température Station Météo",
    "AirTemp": "Température Prévision Météo",
}

afficheicam = {
    "Ptot_ICAM_PV": "Production ICAM PV",
    "Ptot_Bat": "Consommation ICAM Batiment",
    "Ptot_ICAM_Transfo_250KVA": "Consommation ICAM atelier",
    "Ptot_ICAM_MI": "Consommation ICAM Maison",
    "Ptot_Ilot_ICAM": "Consommation ICAM Totale",
    "Etot_ICAM_Remaining": "ICAM Battery Restant",
    "Ptot_ICAM_Batt": "ICAM Battery Puissance",
    "Ptot_ICAM_EDF": "Consommation ICAM EDF",
}


icamlabel = [
    "Ptot_ICAM_PV",
    "Ptot_Bat",
    "Ptot_ICAM_Transfo_250KVA",
    "Ptot_ICAM_MI",
    "Ptot_Ilot_ICAM",
    "Etot_ICAM_Remaining",
    "Ptot_ICAM_Batt",
    "Ptot_ICAM_EDF",
]

icamaffichedaily = [
    "Etot_ICAM_Capacity",
    "Etot_ICAM_Remaining",
    "Ptot_ICAM_Batt",
    "Ptot_ICAM_EDF",
    "Ptot_ICAM_MI",
    "Ptot_ICAM_Ond_1",
    "Ptot_ICAM_Ond_2",
    "Ptot_ICAM_PV",
    "Ptot_ICAM_Transfo_250KVA",
    "Ptot_ICAM_Transfo_400KVA",
    "Ptot_Ilot",
    "Ptot_Bat",
]


icamaffichehist = [
    "Etot_ICAM_Capacity",
    "Etot_ICAM_Remaining",
    "Ptot_ICAM_Batt",
    "Ptot_ICAM_EDF",
    "Ptot_ICAM_MI",
    "Ptot_ICAM_Ond_1",
    "Ptot_ICAM_Ond_2",
    "Ptot_ICAM_PV",
    "Ptot_ICAM_Transfo_250KVA",
    "Ptot_ICAM_Transfo_400KVA",
    "Ptot_Ilot_ICAM",
    "Ptot_Bat",
]