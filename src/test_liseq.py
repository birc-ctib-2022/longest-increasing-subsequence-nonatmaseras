"""Testing module liseq"""

from liseq import liseq


def test_special_cases() -> None:
    """A quick test of some special cases."""
    assert liseq([]) == []
    assert liseq('a') == [0]
    assert liseq('abcd') == [0, 1, 2, 3]


def test_your_own_tests() -> None:
    """Add your own tests below."""
    assert liseq([12, 45, 32, 65, 78, 23, 35, 45, 57]) == [0, 5, 6, 7, 8] # <- to get your attention
