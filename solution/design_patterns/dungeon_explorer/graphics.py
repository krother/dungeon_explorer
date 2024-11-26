import os
from typing import Any

import cv2
import numpy as np

from game import DungeonGame

TILE_PATH = os.path.split(__file__)[0] + '/tiles'

# title of the game window
GAME_TITLE = "Dungeon Explorer"


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


def read_all_images() -> dict[str, Any]:
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
