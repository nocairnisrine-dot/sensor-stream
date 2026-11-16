
from src.buffer import ReadingBuffer

def test_overflow_drops_oldest():

    buf = ReadingBuffer(maxlen=2)

    buf.add("2026-11-20 10:00:00", "temp_01", 1.0)

    buf.add("2026-11-20 10:00:01", "temp_01", 2.0)

    buf.add("2026-11-20 10:00:02", "temp_01", 3.0)

    assert buf.to_dataframe()["value"].tolist() == [2.0, 3.0]

def test_empty_buffer_has_columns():

    df = ReadingBuffer().to_dataframe()

    assert list(df.columns) == ["timestamp", "sensor_id", "value"]

    assert len(df) == 0

