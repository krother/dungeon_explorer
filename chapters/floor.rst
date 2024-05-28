Draw the Floor
==============

In this exercise, we will make the character walk on a stone floor.
To do so, we need to add a representation of the dungeon to the game data.

The complete feature consists of three steps:

1. create a data structure containing a map of the dungeon
2. fill the dungeon map with floor tiles
3. draw each floor tile on the screen


Create a data structure
-----------------------

First, add a new attribute to the `DungeonGame` class.
We will call it `level`:

.. code:: python3

    level: list[str]

The list will contains multiple rows. Each row represents a row on the screen.
Each row contains multiple characters, each representing a single tile in the dungeon.

.. hint::

    When you run the code, you should see an error message similar to:

    ::

       level
           Field required [type=missing, input_value={'x': 8, 'y': 1}, input_type=dict]

Fill the dungeon map
--------------------

We need to provide data for the level when the game starts.
Add a new parameter to the creation of `DungeonGame` in the `start_game()` function:

.. code:: python3

    level=[
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
    ]

Here you have a straightforward representation of a 10 x 10 dungeon.
It is a bit boring, because it only contains floor tiles.
But we will add other things soon.

.. hint::

    When you run the program, it the character should move.
    However, you cannot see the floor yet.

Draw floor tiles
----------------

The last detail is to draw the floor.
For every floor tile, we will draw the image `floor.png`.
The module responsible for the graphics is `main.py`.
We need to explicitly draw *every tile in every row*.
This is done by a loop within a loop.

Add the following code section to the function `draw()`:

.. code:: python3

    # draw dungeon tiles
    for y, row in enumerate(game.level):
        for x, tile in enumerate(row):
            draw_tile(frame, x=x, y=y, image=images["floor"])

.. hint::

   You need to figure out where in the function to position these four lines.
   When everything works, the game should look like this:

   .. figure:: ../images/floor_tiles.png

