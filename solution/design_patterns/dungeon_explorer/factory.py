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


class TileFactory:

    def __init__(self, zoom_factor: int=2):
        self.tile_size = 32 * zoom_factor
        self.zoom_factor = zoom_factor
        self._images = self._read_all_images()

    def __getitem__(self, key):
        return self._images[key]

    def read_image(self, filename: str) -> Any:
        """
        Reads an image from the given filename and doubles its size.
        If the image file does not exist, an error is created.
        """
        img = cv2.imread(filename)  # sometimes returns None
        if img is None:
            raise IOError(f"Image not found: '{filename}'")
        result = np.kron(img, np.ones((self.zoom_factor, self.zoom_factor, 1), dtype=img.dtype))  # double image size
        return result

    def _read_all_images(self) -> dict[str, Any]:
        return {
            filename[:-4]: self.read_image(os.path.join(TILE_PATH, filename))
            for filename in os.listdir(TILE_PATH)
            if filename.endswith(".png")
        }


f = TileFactory(zoom_factor=3)

def draw_tile(frame, x, y, image, xbase=0, ybase=0) -> None:
    # calculate screen position in pixels
    xpos = xbase + x * f.tile_size
    ypos = ybase + y * f.tile_size
    # copy the image to the screen
    frame[ypos : ypos + f.tile_size, xpos : xpos + f.tile_size] = image


def draw(game: DungeonGame) -> None:
    # initialize screen
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    # draw player
    draw_tile(frame, x=game.x, y=game.y, image=f["player"])
    # display complete image
    cv2.imshow(GAME_TITLE, frame)
