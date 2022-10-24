"""EX07 - Test for Dictionary Functions!"""

__author__ = "935081174"

from dictionary import invert, favorite_color


def test_invert_empty() -> None:
    """Tests for empty dictionary inverting."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert() -> None:
    """Tests for dictionary inverting."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2() -> None:
    """Tests, in a different way, to see if fucntion works for invert function!"""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_favorite_color_equalnumber() -> None:
    """Test favorite_color function with a tie in favorite colors."""
    b: dict[str, str] = {"Aj": "black", "Marwan": "green"}
    assert favorite_color(b) == 'black'


def test_favorite_color() -> None:
    """Test to find most shared favorite color."""
    b: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(b) == 'blue'


def test_favorite_color_2() -> None:
    """Test in a different was to find the most shared favorite color."""
    assert favorite_color({"Aj": "benz", "Marwan": "lambo", "Youssef": "lambo"}) == "lambo"