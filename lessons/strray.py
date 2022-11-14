"""An example of vectorized opeartions via operator overloading."""

from __future__ import annoatations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        #TODO
        #1. Loop through each item in self's items list
        for item in self:
            item += rhs
            result.items.append(item)
        #   2. Concatentate rhs to the item value
        #   3. Append the resulting string to result's item's list
        return result


a: StrArray = StrArray(["Armondo", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")