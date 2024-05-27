"""
the Dungeon Explorer game logic
"""
from pydantic import BaseModel


class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int
    level: list[list[str]]
    coins: int = 0
    health: int = 150
    items: list = []


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

    if game.level[new_y][new_x] == "€":
        game.level[new_y][new_x] = "."
        game.coins += 1      
    if game.level[new_y][new_x] == "k":
        game.level[new_y][new_x] = "."
        game.items.append("key")
    if game.level[new_y][new_x] == "T":
        game.level[new_y][new_x] = "."
        game.health -= 30
    if game.level[new_y][new_x] == ".":
        game.x = new_x
        game.y = new_y
    if game.level[new_y][new_x] == "x":
        game.status = "finished"


def update(game):
    # health check
    if game.health == 0:
        game.status = "game over"


def parse_level(level):
    return [list(row) for row in level]


def start_game():
    return DungeonGame(
        x=8,
        y=1,
        level=parse_level([
            "##########",
            "#€€€.kkk.#",
            "#€€€.kTT.#",
            "####.#####",
            "#€...#..x#",
            "#....#...#",
            "#€.k€#T#T#",
            "##T###T#T#",
            "#€.......#",
            "##########",
        ])
    )
