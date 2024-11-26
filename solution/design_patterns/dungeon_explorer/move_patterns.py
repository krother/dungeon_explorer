"""
Generators for moving monsters.
Implements the Strategy Pattern.
"""

from typing import Generator

Position = tuple[int, int]


def move_left_right(position: Position, steps: int) -> Generator:
    x, y = position
    while True:
        for _ in range(steps):
            x, y = x - 1, y
            yield x, y
        for _ in range(steps):
            x, y = x + 1, y
            yield x, y


def move_up_down(position: Position, steps: int) -> Generator:
    x, y = position
    while True:
        for _ in range(steps):
            x, y = x, y - 1
            yield x, y
        for _ in range(steps):
            x, y = x, y + 1
            yield x, y
