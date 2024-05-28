"""
the Dungeon Explorer game logic
"""
import random

from pydantic import BaseModel


class Teleporter(BaseModel):
    x: int
    y: int
    target_x: int
    target_y: int


class Fireball(BaseModel):
    x: int
    y: int
    direction: str


class Skeleton(BaseModel):
    x: int
    y: int

class Level(BaseModel):
    level: list[list[str]]
    teleporters: list[Teleporter] = []
    fireballs: list[Fireball] = []
    skeletons: list[Skeleton] = []

class DungeonGame(BaseModel):
    status: str = "running"
    x: int
    y: int
    coins: int = 0
    health: int = 150
    items: list[str] = []
    current_level: Level
    level_number: int = 0


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

    if "key" in game.items and game.current_level.level[new_y][new_x] == "D":
        game.items.remove("key")
        game.current_level.level[new_y][new_x] = "d"
    if game.current_level.level[new_y][new_x] == "€":
        game.current_level.level[new_y][new_x] = "."
        game.coins += 1      
    if game.current_level.level[new_y][new_x] == "k":
        game.current_level.level[new_y][new_x] = "."
        game.items.append("key")
    if game.current_level.level[new_y][new_x] == "T":
        game.current_level.level[new_y][new_x] = "."
        game.health -= 30
    if game.current_level.level[new_y][new_x] == "~":
        game.health -= 10
    if game.current_level.level[new_y][new_x] in ".d~":
        game.x = new_x
        game.y = new_y
    if game.current_level.level[new_y][new_x] == "x":
        game.level_number += 1
        if game.level_number < len(LEVELS):
            # move to next level
            game.current_level = LEVELS[game.level_number]
        else:
            # no more levels left
            game.status = "finished"
    
    check_teleporters(game)
    check_collision(game)


def check_teleporters(game):
    for t in game.current_level.teleporters:
       if game.x == t.x and game.y == t.y:
           game.x = t.target_x
           game.y = t.target_y


def check_collision(game):
    for f in game.current_level.fireballs:
        if f.x == game.x and f.y == game.y:
            game.health -= 50
    for s in game.current_level.skeletons:
        if s.x == game.x and s.y == game.y:
            game.health -= 10


def update(game):
    # health check
    if game.health <= 0:
        game.status = "game over"

    # move fireballs
    for f in game.current_level.fireballs:
        new_x, new_y = get_next_position(f.x, f.y, f.direction)
        if game.current_level.level[new_y][new_x] in ".€kd":  # flies over coins and keys
            f.x, f.y = new_x, new_y
        elif f.direction == "right":
            f.direction = "left"
        elif f.direction == "left":
            f.direction = "right"

    # move skeletons
    for s in game.current_level.skeletons:
        direction = random.choice(["up", "down", "left", "right"])
        new_x, new_y = get_next_position(s.x, s.y, direction)
        if game.current_level.level[new_y][new_x] in ".€kd":  # flies over coins and keys
            s.x, s.y = new_x, new_y

    check_collision(game)


def parse_level(level):
    return [list(row) for row in level]

LEVEL_ONE = Level(
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
    ],
    fireballs=[
        Fireball(x=1, y=8, direction="right")
    ],
    skeletons=[
        Skeleton(x=3, y=5)
    ]
)

LEVEL_TWO = Level(
    level=parse_level([
        "###########",
        "#k#######k#",
        "#.#..x..#.#",
        "#~#.....#~#",
        "#.#.....#.#",
        "#.###.###.#",
        "#..~...~..#",
        "###########"
        ]),
    skeletons=[
        Skeleton(x=5, y=3)
    ]
)
LEVELS = [LEVEL_ONE, LEVEL_TWO]


def start_game():
    return DungeonGame(
        x=8,
        y=1,
        current_level=LEVEL_ONE,
    )
