"""
Simplify (merge) intervals.
"""

from typing import NamedTuple


class Interval(NamedTuple):
    "A closed interval between start and end."
    start: int
    end: int

    def __str__(self) -> str:
        return f"[{self.start},{self.end}]"


def merge(intervals: list[Interval]) -> list[Interval]:
    """
    Simplify the given list of intervals by merging overlapping and adjacent
    intervals.

    For example:
     [1, 6], [8, 15], [12, 18] -> [1, 6], [8, 18]
     [1, 2], [2, 6], [8, 10] -> [1, 6], [8, 10]
    """
    # Sort intervals by increasing start time.
    intervals = sorted(intervals, key=lambda i: i.start)

    # Handle empty input.
    if not intervals:
        return []

    merged_intervals = intervals[:1]
    for interval in intervals[1:]:
        previous = merged_intervals[-1]
        if interval.start == interval.end:
            # Skip empty intervals.
            continue
        if interval.start <= previous.end:
            # Interval overlaps previous -> merge intervals.
            new_end = max(previous.end, interval.end)
            merged_intervals[-1] = Interval(previous.start, new_end)
        else:
            # Non-overlapping interval.
            merged_intervals.append(interval)

    return merged_intervals
