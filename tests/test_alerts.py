import pandas as pd

from src.alerts import detect_alerts


def _readings(values):
    times = pd.date_range(
        "2026-11-20 10:00:00",
        periods=len(values),
        freq="1s",
    )
    return pd.DataFrame({
        "timestamp": times,
        "sensor_id": "temp_01",
        "value": values,
    })


def test_detects_low_and_high():
    df = _readings([5.0, 20.0, 35.0])
    out = detect_alerts(df, low=10, high=30)
    assert out["reason"].tolist() == [
        "below_threshold",
        "above_threshold",
    ]


def test_no_alert_when_in_range():
    assert len(detect_alerts(_readings([20.0]))) == 0


def test_values_equal_to_thresholds_do_not_alert():
    import pandas as pd
    from src.alerts import detect_alerts
    times = pd.date_range(
        "2026-11-20 10:00:00", periods=2, freq="1s"
    )
    df = pd.DataFrame({
        "timestamp": times,
        "sensor_id": "temp_01",
        "value": [10.0, 30.0],
    })
    assert len(detect_alerts(df, low=10, high=30)) == 0
