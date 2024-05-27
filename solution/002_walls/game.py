"""
the Dungeon Explorer game logic
"""
from pydantic import BaseModel


class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int
    level: list[str]


def move_player(game, direction: str) -> None:
    """Things that happen when the player walks on stuff"""
    new_x = game.x
    new_y = game.y
    if direction == "right":
        new_x += 1
    elif direction == "left":
        new_x -= 1
    elif direction == "up":
        new_y -= 1
    elif direction == "down":
        new_y += 1
    if game.level[new_y][new_x] == ".":
        game.x = new_x
        game.y = new_y


def start_game():
    return DungeonGame(
        x=8,
        y=1,
        level=[
            "##########",
            "#........#",
            "#........#",
            "####.#####",
            "#....#...#",
            "#....#...#",
            "#....#.#.#",
            "##.###.#.#",
            "#........#",
            "##########",
        ]
    )
