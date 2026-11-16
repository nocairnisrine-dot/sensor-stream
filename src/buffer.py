"""Tampon des N dernières mesures."""
from collections import deque

import pandas as pd


class ReadingBuffer:
    def __init__(self, maxlen=100):
        self._items = deque(maxlen=maxlen)

    def add(self, timestamp, sensor_id, value):
        self._items.append((timestamp, sensor_id, value))

    def __len__(self):
        return len(self._items)

    def to_dataframe(self):
        return pd.DataFrame(
            list(self._items),
            columns=["timestamp", "sensor_id", "value"],
        )
