"""EX04 - `list` Utility Functions!"""

__author__ = "935081174"


def all(haystack: list[int], needle: int) -> bool:
    """Whether or not all the ints in the list are the same as the given int."""
    i: int = -1
    while i < len(haystack):
        if len(haystack) == 0:
            return False
        if haystack[i] != needle:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return the largest in the List."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else: 
        i: int = 0
        largest = input[i]
        while i < len(input):
            if input[i] > largest:
                largest = input[i]
            i += 1
        return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Wheather or not lists are equal."""
    i: int = -1
    if len(list1) != len(list2):
        return False
    while i < len(list1) and len(list2):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True