"""Fenêtre glissante pour un flux de capteurs."""
from collections import deque


class SlidingWindow:
    """Garde les `size` dernières valeurs reçues."""

    def __init__(self, size):
        if size <= 0:
            raise ValueError("size doit être supérieur à 0")
        self.size = size
        self._values = deque(maxlen=size)

    def add(self, value):
        self._values.append(value)

    def values(self):
        return list(self._values)

    def is_full(self):
        return len(self._values) == self.size

    def mean(self):
        if not self._values:
            return None
        return sum(self._values) / len(self._values)

    def min(self):
        return min(self._values) if self._values else None

    def max(self):
        return max(self._values) if self._values else None


def moving_average(values, size):
    """Moyenne glissante de chaque valeur sur les `size` dernières."""
    window = SlidingWindow(size)
    result = []
    for value in values:
        window.add(value)
        result.append(window.mean())
    return result