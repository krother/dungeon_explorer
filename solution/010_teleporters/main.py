"""
graphics engine for 2D games
"""
import os
import numpy as np
import cv2
from game import start_game, move_player, update
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
SCREEN_SIZE_X, SCREEN_SIZE_Y = 840, 640
TILE_SIZE = 64

SYMBOLS = {
    ".": "floor",
    "#": "wall",
    "€": "coin",
    "T": "trap",
    "k": "key",
    "x": "stairs_down",
    "d": "open_door",
    "D": "closed_door",
    }

def read_image(filename: str) -> np.ndarray:
    """
    Reads an image from the given filename and doubles its size.
    If the image file does not exist, an error is created.
    """
    img = cv2.imread(filename)  # sometimes returns None
    if img is None:
        raise IOError(f"Image not found: '{filename}'")
    img = np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))  # double image size
    return img


def read_images():
    return {
        filename[:-4]: read_image(os.path.join(TILE_PATH, filename))
        for filename in os.listdir(TILE_PATH)
        if filename.endswith(".png")
    }


def draw_tile(frame, x, y, image, xbase=0, ybase=0):
    # calculate screen position in pixels
    xpos = xbase + x * TILE_SIZE
    ypos = ybase + y * TILE_SIZE
    # copy the image to the screen
    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = image


def draw(game, images):
    # initialize screen
    frame = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)
    # draw dungeon tiles
    for y, row in enumerate(game.level):
        for x, tile in enumerate(row):
            draw_tile(frame, x=x, y=y, image=images[SYMBOLS[tile]])
    # draw player
    draw_tile(frame, x=game.x, y=game.y, image=images["player"])
    # draw teleporters
    for t in game.teleporters:
        draw_tile(frame, x=t.x, y=t.y, image=images["teleporter"])
    # display coins
    draw_tile(frame, xbase=660, ybase=32, x=0, y=0, image=images["coin"])
    cv2.putText(frame,
                str(game.coins),
                org=(730, 78),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5,
                color=(255, 128, 128),
                thickness=3,
                )
    # health bar
    frame[120:160, 660:660 + game.health] = (0, 255, 0)
    # inventory
    for i, item in enumerate(game.items):
        y = i // 2  # floor division: rounded down
        x = i % 2   # modulo: remainder of an integer division
        draw_tile(frame, xbase=660, ybase=192, x=x, y=y, image=images[item])

    cv2.imshow(GAME_TITLE, frame)


def handle_keyboard(game):
    """keys are mapped to move commands"""
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "q":
        game.status = "exited"
    if key in MOVES:
        move_player(game, MOVES[key])


# game starts
images = read_images()
game = start_game()
while game.status == "running":
    draw(game, images)
    update(game)
    handle_keyboard(game)

cv2.destroyAllWindows()
