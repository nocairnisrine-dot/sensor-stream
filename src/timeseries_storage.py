"""Stockage des séries temporelles (SQLite)."""
import sqlite3
from contextlib import closing

import pandas as pd

COLUMNS = ["timestamp", "sensor_id", "value"]
TABLE = "readings"


def save_readings(df, path, if_exists="append"):
    """Enregistre les mesures dans SQLite.

    Retourne le nombre de lignes écrites.
    """
    missing = [c for c in COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Colonnes manquantes : {missing}")
    data = df[COLUMNS].copy()
    data["timestamp"] = pd.to_datetime(
        data["timestamp"]
    ).dt.strftime("%Y-%m-%d %H:%M:%S")
    with closing(sqlite3.connect(path)) as conn:
        data.to_sql(TABLE, conn, if_exists=if_exists,
                    index=False)
    return len(data)


def load_readings(path, sensor_id=None):
    """Relit les mesures, triées par date."""
    query = f"SELECT {', '.join(COLUMNS)} FROM {TABLE}"
    params = ()
    if sensor_id is not None:
        query += " WHERE sensor_id = ?"
        params = (sensor_id,)
    query += " ORDER BY timestamp"
    with closing(sqlite3.connect(path)) as conn:
        df = pd.read_sql_query(query, conn, params=params)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df
