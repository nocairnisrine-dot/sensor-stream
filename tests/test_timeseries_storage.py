import pandas as pd
import pytest

from src.timeseries_storage import (
    load_readings,
    save_readings,
)


def _readings():
    times = pd.date_range(
        "2026-11-20 10:00:00", periods=3, freq="1s"
    )
    return pd.DataFrame({
        "timestamp": times,
        "sensor_id": ["temp_01", "temp_02", "temp_01"],
        "value": [20.0, 21.5, 22.0],
    })


def test_roundtrip(tmp_path):
    db = str(tmp_path / "readings.db")
    assert save_readings(_readings(), db) == 3
    out = load_readings(db)
    assert out["value"].tolist() == [20.0, 21.5, 22.0]


def test_filter_by_sensor(tmp_path):
    db = str(tmp_path / "readings.db")
    save_readings(_readings(), db)
    out = load_readings(db, sensor_id="temp_01")
    assert len(out) == 2


def test_missing_column_raises(tmp_path):
    db = str(tmp_path / "readings.db")
    bad = _readings().drop(columns=["value"])
    with pytest.raises(ValueError):
        save_readings(bad, db)


def test_unknown_sensor_returns_empty(tmp_path):
    db = str(tmp_path / "readings.db")
    save_readings(_readings(), db)
    out = load_readings(db, sensor_id="temp_99")
    assert len(out) == 0
