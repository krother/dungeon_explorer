"""
Generators for moving monsters.
Implements the Strategy Pattern.
"""

from typing import Generator

Position = tuple[int, int]

class LeftRightMove:
    """
    Stateful implementation of a movement pattern.
    Uses the Iterator Pattern.
    """
    def __init__(self, start: Position, steps: int):
        self.position = start
        self.direction = "left"
        self.steps = steps
        self.counter = steps

    def get_next_position(self) -> Position:
        ...


def move_left_right(position: Position, steps: int) -> Generator[Position, None, None]:
    x, y = position
    while True:
        for _ in range(steps):
            x, y = x - 1, y
            yield x, y
        for _ in range(steps):
            x, y = x + 1, y
            yield x, y


def move_up_down(position: Position, steps: int) -> Generator[Position, None, None]:
    x, y = position
    while True:
        for _ in range(steps):
            x, y = x, y - 1
            yield x, y
        for _ in range(steps):
            x, y = x, y + 1
            yield x, y
