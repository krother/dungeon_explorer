Stop at Walls
=============

At the moment, it is easy to run off the screen, crashing the program.
In this exercise, you will add walls that stop the player, also making the dungeon more interesting.

To make the walls work, you need to take care of the following:

1. add walls to the dungeon map
2. draw the walls
3. make sure the player cannot move into a wall

Add walls to the dungeon map
----------------------------

The data structure we created for the floor tiles makes it easy to edit the dungeon.
All you need to do is add walls to the level in the `start_game()` function.
Use the hash symbol `#`.

Replace a few of the floor symbols by walls, e.g. creating a border.
The size of the dungeon should not change.

.. hint::

    Running the game should work, but you won't see anything.

Draw the walls
--------------

To see the walls, you need the image `wall.png`.
In the `draw()` function in `main.py`, you need to distinguish between floors and walls.
The logic you need to add is the following:

1. go through all tiles in the level (we have this already)
2. if the tile is a floor, draw `floor.png`
3. if the tile is a wall, draw `wall.png`

Add the following lines, replacing the one inside the two loops in `draw()`:

.. code:: python3

    if tile == ".":
        draw_tile(frame, x=x, y=y, image=images["floor"])

.. hint::

    When you run the code, you should notice that some floor tiles are missing:

    .. image:: ../images/missing_floor_tiles.png

Now, add a **second if statement** similar to the first one that draws the walls.

.. hint::

    The result should look like this:

    .. image:: ../images/wall_tiles.png

Stop at walls
-------------

Currently, the player can move through the walls.
Let's stop them.
You need the following logic:

1. calculate the new position where the player *would* move
2. if there is a floor in the new position, move there
3. if there is a wall, do nothing

You need to implement this logic in the `move_player()` function.

First, copy the current position of the player:

.. code:: python3

   def move_player(game, direction: str) -> None:
       """Things that happen when the player walks on stuff"""
       new_x = game.x
       new_y = game.y
       ...

Second, modify the `if` statements so that they modify the new position instead:

.. code:: python3

    if direction == "right":
        new_x += 1
    ...

.. hint::

    At this point, the game should work, but you can still walk into walls.

Third, check for floors in the new position. For that you need to look up a tile in `game.level`.
Use **indexing**, indicated by the square brackets. Note that the y coordinate goes first:

.. code:: python3
 
    if game.level[new_y][new_x] == ".":
        game.x = new_x
        game.y = new_y

If the tile contains a wall, `game.x` and `game.y` will not get updated. So nothing happens.

.. hint::

    Run the game. You should see that the player cannot move into walls any more.


Extra: Fountain
---------------

Add another element to the dungeon, e.g. a fountain using the image `fountain.png`.
