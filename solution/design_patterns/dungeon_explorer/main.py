"""
graphics engine for 2D games
"""
import os
from typing import Any
import numpy as np
import cv2
from game import DungeonGame

TILE_PATH = os.path.split(__file__)[0] + '/tiles'

# title of the game window
GAME_TITLE = "Dungeon Explorer"

# map keyboard keys to move commands
MOVES = {
    "a": "left",
    "d": "right",
    "w": "up",
    "s": "down",
}

#
# constants measured in pixels
#
SCREEN_SIZE_X, SCREEN_SIZE_Y = 640, 640
TILE_SIZE = 64


def read_image(filename: str) -> Any:
    """
    Reads an image from the given filename and doubles its size.
    If the image file does not exist, an error is created.
    """
    img = cv2.imread(filename)  # sometimes returns None
    if img is None:
        raise IOError(f"Image not found: '{filename}'")
    result = np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))  # double image size
    return result


def read_images() -> dict[str, Any]:
    return {
        filename[:-4]: read_image(os.path.join(TILE_PATH, filename))
        for filename in os.listdir(TILE_PATH)
        if filename.endswith(".png")
    }


def draw_tile(frame, x, y, image, xbase=0, ybase=0) -> None:
    # calculate screen position in pixels
    xpos = xbase + x * TILE_SIZE
    ypos = ybase + y * TILE_SIZE
    # copy the image to the screen
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = image


def draw(game: DungeonGame, images: Any) -> None:
    # initialize screen
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    # draw player
    draw_tile(frame, x=game.x, y=game.y, image=images["player"])
    # display complete image
    cv2.imshow(GAME_TITLE, frame)


def handle_keyboard(game: DungeonGame):
    """keys are mapped to move commands"""
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        game.status = "exit1ed"
    if key in MOVES:
        game.move_player(MOVES[key])


def main():
    images = read_images()
    game = DungeonGame()
    game.start_game()
    while game.status == "running":
        draw(game, images)
        handle_keyboard(game)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()