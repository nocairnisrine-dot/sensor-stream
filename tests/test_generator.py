from src.generator import generate_readings


def test_length():
    assert len(generate_readings(10, seed=1)) == 10


def test_range():
    values = generate_readings(100, low=10, high=20, seed=1)
    assert all(10 <= v <= 20 for v in values)
