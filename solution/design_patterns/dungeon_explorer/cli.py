"""
Game without graphical interface

Enter keys one by one and confirm with enter
"""

from copy import deepcopy
from game import DungeonGame


# map keys to move commands
MOVES = {
    "a": "left",
    "d": "right",
    "w": "up",
    "s": "down",
}


def draw(game):
    level = [list(row) for row in game.level]
    level[game.y][game.x] = "P"
    print("\n".join(["".join(row) for row in level]))


def main():
    game = DungeonGame(
        x=8,
        y=1,
        level=[
            "##########",
            "#........#",
            "#........#",
            "#........#",
            "#........#",
            "#........#",
            "#........#",
            "#........#",
            "#........#",
            "##########",
        ],
    )
    game.start_game()
    while game.status == "running":
        draw(game)
        key = input()
        if key == "q":
            break
        if key in MOVES:
            game.move_player(MOVES[key])
        print(game.model_dump())


if __name__ == "__main__":
    main()
