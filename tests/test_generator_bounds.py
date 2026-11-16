import pytest
from src.generator import generate_readings


def test_values_stay_within_narrow_bounds():
    values = generate_readings(100, low=10.001, high=10.004, seed=1)
    assert all(10.001 <= v <= 10.004 for v in values)


def test_low_above_high_raises():
    with pytest.raises(ValueError):
        generate_readings(5, low=20.0, high=10.0)
