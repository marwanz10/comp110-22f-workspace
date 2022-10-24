"""EX07 - Dictionary Functions!"""

__author__ = "935081174"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Construct dict from two str."""
    result: dict[str, str] = {}
    d: int = len(a)
    for key in a:
        result[a[key]] = key
    e: int = len(result)
    if d != e:
        raise KeyError
    return result
    

def favorite_color(b: dict[str, str]) -> str:
    """Choose most common answer."""
    result: dict[str, str] = {}
    for key, b[key] in b.items():
        if b[key] not in result:
            result[b[key]] = 0
        else:
            result[b[key]] += 1
    return (max(result, key=result.get))


def count(c: list[str]) -> dict[str, int]:
    """count."""
    result: dict[str, int] = {}
    for key in c:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result