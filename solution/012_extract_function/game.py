"""
the Dungeon Explorer game logic
"""
from pydantic import BaseModel


class Teleporter(BaseModel):
    x: int
    y: int
    target_x: int
    target_y: int


class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int
    level: list[list[str]]
    coins: int = 0
    health: int = 150
    items: list[str] = []
    teleporters: list[Teleporter] = []


def get_next_position(x, y, direction):
    if direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    elif direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    return x, y


def move_player(game, direction: str) -> None:
    """Things that happen when the player walks on stuff"""
    new_x, new_y = get_next_position(game.x, game.y, direction)

    if "key" in game.items and game.level[new_y][new_x] == "D":
        game.items.remove("key")
        game.level[new_y][new_x] = "d"
    if game.level[new_y][new_x] == "€":
        game.level[new_y][new_x] = "."
        game.coins += 1      
    if game.level[new_y][new_x] == "k":
        game.level[new_y][new_x] = "."
        game.items.append("key")
    if game.level[new_y][new_x] == "T":
        game.level[new_y][new_x] = "."
        game.health -= 30
    if game.level[new_y][new_x] in ".d":
        game.x = new_x
        game.y = new_y
    if game.level[new_y][new_x] == "x":
        game.status = "finished"
    
    check_teleporters(game)


def check_teleporters(game):
    for t in game.teleporters:
       if game.x == t.x and game.y == t.y:
           game.x = t.target_x
           game.y = t.target_y


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
            "#€€€.....#",
            "#.€€.kTT.#",
            "####.#####",
            "#€...#..x#",
            "#....#...#",
            "#€.k€#T#T#",
            "##T###D#D#",
            "#€..D....#",
            "##########",
        ]),
        teleporters=[
            Teleporter(x=1, y=2, target_x=2, target_y=8),
        ]
    )
