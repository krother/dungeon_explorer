
from pprint import pprint 
from typing import Literal

from pydantic import BaseModel


GameStatus = Literal["running", "exited"]


class DungeonGame(BaseModel):
    _status: GameStatus = "running"
    x: int = 8
    y: int = 1
    level: list[str]

class Position(BaseModel):
    x: int
    y: int

Tile = Literal["#", ".", "€"]

class Player(BaseModel):
    health: int = 3
    position: Position

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__private: str = "foo"  # define an extra private attribute that pydantic should ignore


class Level(BaseModel):
    level_map: list[list[Tile]]


class WebGame:

    def __init__(self, dungeon_game: DungeonGame, id: int):
        self.id = id
        self.game = dungeon_game

    @property
    def player(self) -> Player:
        return Player(position=Position(x=self.game.x, y=self.game.y))

    @property
    def level(self) -> Level:
        return Level(level_map=[list(row) for row in self.game.level])

    def set_tile(self, position: Position, tile: Tile):
        row = self.level.level_map[position.y]
        row[position.x] = tile
        self.game.level[position.y] = "".join(row)
        # TODO check if position is inside playing field


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
web_game = WebGame(game, id=42)
web_game.set_tile(Position(x=3, y=2), "€")

pprint(web_game.level.level_map)
