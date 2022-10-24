"""EX05 - `list` Utility Functions!"""

__author__ = "935081174"


def only_evens(xs: list[int]) -> list[int]:
    """Output only the even elements of the input parameter."""
    i: int = 0
    even: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            even.append(xs[i])
        i += 1
    return even


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combining two lists?"""
    list_3: list[int] = []
    i: int = 0
    while i < len(list_1):
        list_3.append(list_1[i])
        i += 1
    i: int = 0
    while i < len(list_2):
        list_3.append(list_2[i])
        i += 1
    return list_3


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Creating subset of givin list!"""
    subset: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(a_list):
        end_index = len(a_list)
    if len(a_list) == 0 or start_index > end_index or end_index <= 0 or start_index == len(a_list):
        subset: list[int] = []
        return subset
    subset.append(a_list[start_index])
    subset.append(a_list[end_index - 1])
    return subset
