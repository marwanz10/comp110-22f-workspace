"""EX05 - Tests for the utility fucntion!"""

__author__ = "935081174"


from utils import only_evens, concat, sub


def test_only_even_empty() -> None:
    """Tests for empty list in only_even function."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens() -> None:
    """Tests to see function works for only_evens?"""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_2() -> None:
    """Tests, in a different way, to see if fucntion works for only evens function!"""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_concat_empty() -> None:
    """Tests for empty list in conact function."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat() -> None:
    """Tests to see function works for conacat?"""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Tests, in a different way, to see if fucntion works for concat function!"""
    assert concat([1, 1, 1], [2, 2, 2]) == [1, 1, 1, 2, 2, 2]


def test_sub_empty() -> None:
    """Tests for empty list in sub function."""
    a_list: list[int] = []
    start_index: int = 2
    end_index: int = 4
    assert sub(a_list, start_index, end_index) == []


def test_sub() -> None:
    """Tests to see function works for sub?"""
    a_list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [20, 30]


def test_sub2() -> None:
    """Tests, in a different way, to see if fucntion works for sub function!"""
    assert sub([5, 5, 5, 5, 7], 3, 5) == [5, 7]