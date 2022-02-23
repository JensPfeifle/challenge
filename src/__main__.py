"""
Main entrypoint.
"""
from src.intervals import Interval, merge

if __name__ == "__main__":
    example = [Interval(*i) for i in [[25, 30], [2, 19], [14, 23], [4, 8]]]
    print(merge(example))
