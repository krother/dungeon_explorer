"""
the Dungeon Explorer game logic
"""

from pydantic import BaseModel

from typing import Literal

GameStatus = Literal["running", "exited"]


class DungeonGame(BaseModel):
    _status: GameStatus = "running"
    x: int = 8
    y: int = 1
    level: list[str]

    def __str__(self):
        return f"Player at {self.x}/{self.y}"

    def __repr__(self):
        return str(self)

    @property
    def status(self) -> GameStatus:
        return self._status

    @status.setter
    def status(self, value: GameStatus) -> None:
        if value not in {"running", "exited"}:
            raise ValueError(f"invalid status: {value}")
        self._status = value

    def move_player(self, direction: str) -> None:
        """Things that happen when the player walks on stuff"""
        if direction == "right":
            self.x += 1
        elif direction == "left":
            self.x -= 1

    def start_game(self): ...
