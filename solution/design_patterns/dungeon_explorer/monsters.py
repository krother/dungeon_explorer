from typing import Callable, Generator
from functools import partial

from pydantic import BaseModel

from move_patterns import Position, move_left_right


class Monster(BaseModel):
    kind: str
    position: Position
    speed: int = 1
    move_pattern: Callable
    __gen: Generator | None = None

    def __init__(self, *args, **kwargs):  # args is a Sequence or Iterable, kwargs is a dict
        super().__init__(*args, **kwargs)
        self.__gen = self.move_pattern(self.position)

    def __str__(self):
        return f"{self.kind} at {self.position}"

    def move(self):
        self.position = next(self.__gen)


if __name__ == "__main__":
    m = Monster(kind="zombie", position=(3, 5), move_pattern=partial(move_left_right, steps=3))
    for _ in range(10):
        m.move()
        print(m)
