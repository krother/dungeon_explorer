Code cleanup: Lookup Table
==========================

In an ongoing software project, it is useful to clean up the code from time to time.
In this exercise, you will clean up the code for drawing.

When you read the code for the `draw()` function, you might notice that there are a lot of very similar lines, e.g.:

.. code:: python3

    if tile == ".":
        draw_tile(frame, x=x, y=y, image=images["floor"])
    if tile == "#":
        draw_tile(frame, x=x, y=y, image=images["wall"])

This code is unnecessarily long. The problem also becomes worse, the more different tiles you add.
The `if` statements only differ in the character and image they map to each other.

Extract a dictionary
--------------------
The character-image pairs can be more cleanly defined in a **dictionary**:

.. code:: python3

    SYMBOLS = {
        ".": "floor",
        "#": "wall",
        ...
        }

Now it is enough to **one** call to `draw_tile()` that looks up the image.
The `if` statements are completely unnecessary and can be removed:

.. code:: python3

    draw_tile(frame, x=x, y=y, image=images[SYMBOLS[tile]])

.. hint::

    Note that you will still need extra code to draw the player, health bar, coin display etc.

Add a new tile
--------------
Apart from the code getting shorter, it is much easier now to add new elements to the dungeon.
All you need to do is to add an entry to `SYMBOLS` and you can add them to your level.

Pick one or more new images and add them to beautify your level.
