import pytest

from src.sliding_window import SlidingWindow, moving_average


def test_window_keeps_only_last_values():
    w = SlidingWindow(3)
    for v in [1, 2, 3, 4]:
        w.add(v)
    assert w.values() == [2, 3, 4]
    assert w.is_full()


def test_mean_min_max():
    w = SlidingWindow(3)
    for v in [10, 20, 30]:
        w.add(v)
    assert w.mean() == 20
    assert w.min() == 10
    assert w.max() == 30


def test_empty_window():
    w = SlidingWindow(3)
    assert w.mean() is None
    assert not w.is_full()


def test_invalid_size():
    with pytest.raises(ValueError):
        SlidingWindow(0)


def test_moving_average():
    assert moving_average([1, 2, 3, 4], 2) == [1, 1.5, 2.5, 3.5]


def test_add_rejects_non_number():
    w = SlidingWindow(3)
    with pytest.raises(TypeError):
        w.add("abc")