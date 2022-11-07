"""Dictionary related utility functions."""

__author__ = "935081174"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reading every row from csv into a list of dicts."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """List of values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Tranform a table represnted as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(new_column: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in new_column:
        count: int = 0
        result[column] = []
        while count < N and count < len(new_column[column]):
            result[column].append(new_column[column][count])
            count += 1
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """New column table."""
    result: dict[str, list[str]] = {}
    for key in names:
        if key in table:
            result[key] = table[key]
    return result


def concat(column_table: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat!"""
    result: dict[str, list[str]] = {}
    for key in column_table:
        result[key] = column_table[key]
    for key in column_table_2:
        if key in column_table:
            result[key] = column_table[key] + column_table_2[key]
        else:
            result[key] = column_table_2[key]
    return result