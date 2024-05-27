"""
the Dungeon Explorer game logic
"""
from pydantic import BaseModel


class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int


def move_player(game, direction: str) -> None:
    """Things that happen when the player walks on stuff"""
    if direction == "right":
        game.x += 1
    elif direction == "left":
        game.x -= 1


def start_game():
    return DungeonGame(
        x=8,
        y=1,
    )
