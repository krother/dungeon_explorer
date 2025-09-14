"""
the Dungeon Explorer game logic
"""
from pydantic import BaseModel
from typing import Callable

class Move(BaseModel):
    tile: str
    from_x: int
    from_y: int
    speed_x: int
    speed_y: int
    progress: int = 0
    complete: bool = False
    finished: Callable = None


class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int
    moves: list[Move] = []

def move_player(game: DungeonGame, direction: str) -> None:
    """Things that happen when the player walks on stuff"""
    if direction == "right":
        game.x += 1
    elif direction == "left":
        game.x -= 1
    ...


def start_game():
    return DungeonGame(
        x=8,
        y=1,
    )
