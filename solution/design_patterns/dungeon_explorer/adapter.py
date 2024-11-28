from pprint import pprint
from typing import Literal

from pydantic import BaseModel


GameStatus = Literal["running", "exited"]


class DungeonGame(BaseModel):
    _status: GameStatus = "running"
    x: int = 8
    y: int = 1
    level: list[str]


Position = tuple[int, int]


class Player(BaseModel):
    health: int = 3
    position: Position


class Level(BaseModel):
    level_map: list[list[str]]


class WebGame(BaseModel):
    id: int
    player: Player
    level: Level


def convert_game(game: DungeonGame, id: int) -> WebGame:
    return WebGame(
        id=id,
        player=Player(
            health=3,
            position=(game.x, game.y),
        ),
        level=Level(level_map=[list(row) for row in game.level]),
    )


if __name__ == "__main__":
    game = DungeonGame(
        x=3,
        y=1,
        level=[
            "######",
            "#....#",
            "#....#",
            "#....#",
            "#....#",
            "######",
        ],
    )
    web_game = convert_game(game=game, id=42)
    pprint(web_game.model_dump())
