"""
Tests for intervals.
"""

import pytest

# pylint: disable=missing-docstring, redefined-builtin
from src.intervals import Interval, merge


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [[0,10]],
            [[0,10]],
        ),
        (
            [[25, 30], [2, 19], [14, 23], [4, 8]],
            [[2, 23], [25, 30]],
        ),
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ),
    ],
)
def test_merge(input: list[list[int]], expected: list[list[int]]) -> None:
    intervals = [Interval(*i) for i in input]
    expected_result = [Interval(*i) for i in expected]
    assert merge(intervals) == expected_result


def test_empty() -> None:
    assert merge([]) == []

