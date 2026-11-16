
import pandas as pd

from src.textdashboard import render_dashboard


def test_dashboard_lists_sensors():
    times = pd.date_range(
        "2026-11-20 10:00:00", periods=2, freq="1s"
    )

    df = pd.DataFrame({
        "timestamp": times,
        "sensor_id": ["temp_01", "temp_02"],
        "value": [20.0, 21.5],
    })

    text = render_dashboard(df)

    assert "temp_01" in text
    assert "temp_02" in text
    assert "Alertes : 0" in text


def test_dashboard_handles_empty_dataframe():
    import pandas as pd
    from src.textdashboard import render_dashboard
    df = pd.DataFrame(columns=["timestamp", "sensor_id", "value"])
    text = render_dashboard(df)
    assert "Alertes : 0" in text
