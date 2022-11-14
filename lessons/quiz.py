"""practice"""


# def odd_and_even(x: list[int]) -> list[int]:
#     i: int = 0
#     new_list: list[int] = []
#     while i < len(x):
#         if i % 2 == 0 and x[i] % 2 != 0:
#             new_list.append(x[i])
#         i += 1
#     return new_list



# def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
#     """Averages grades."""
#     average: dict[str, float] = {}
#     for student in grades:
#         total: int = 0
#         for grade in grades[student]:
#             total += grade
#         average[student] = total / len(grades[student])
#     return average


# def best_animals(visits: dict[str, int]) -> list[str]:
#     result: list[str] = []
#     i: int = 0
#     while i < 3:
#         max: int = 0
#         animals: str = ""
#         for key in visits:
#             if visits[key][i] > max:
#                 max = visits[key][i]
#                 animals = key
#         result.append(animals)
#         i += 1 
#     return result


from typing import Union

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result