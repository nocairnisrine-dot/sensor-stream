"""Détection d'alertes sur seuils."""
import pandas as pd


def detect_alerts(df, low=10.0, high=30.0):
    """Retourne les mesures hors seuils."""
    low_df = df[df["value"] < low]
    high_df = df[df["value"] > high]
    low_df = low_df.assign(reason="below_threshold")
    high_df = high_df.assign(reason="above_threshold")
    alerts = pd.concat([low_df, high_df])
    alerts = alerts.sort_values("timestamp")
    return alerts.reset_index(drop=True)
