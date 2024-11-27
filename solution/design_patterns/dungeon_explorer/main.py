"""
graphics engine for 2D games
"""

import cv2

from game import DungeonGame
from factory import draw

# map keyboard keys to move commands
MOVES = {
    "a": "left",
    "d": "right",
    "w": "up",
    "s": "down",
}


def handle_keyboard(game: DungeonGame):
    """keys are mapped to move commands"""
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        game.status = "exited"
    if key in MOVES:
        game.move_player(MOVES[key])


def main():
    game = DungeonGame(
        x=4,
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
        handle_keyboard(game)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
