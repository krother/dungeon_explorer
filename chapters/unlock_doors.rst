
Unlock Doors
============

Let's use the keys to open doors.
In this exercise, you will place closed doors on the map.
Keys in the inventory can be used to open them. Each key works only once.
The implementation is done in two steps:

1. add doors to the level
2. open a closed door with a key
3. walk through an open door

Add doors
---------

Lets use the characters `D` and `d` for closed and open doors.
They correspond to the images `open_door.pny` and `closed_door.png`, respecitvely.
Add both to the `SYMBOLS` dictionary.

Open a closed door
------------------

When opening a closed door, a couple of things need to be done.
The code below contains placeholders, and only the new things are implemented explicitly.
Fill in the rest – you should find similar examples in the `move_player()` function.

.. code:: python3

    if "key" in game.items and ...:  # check whether there is a door
        game.items.remove("key")     # key can be used once
        ...                          # replace the closed door by an open one

Depending on where in `move_player()` you place this code, the character will or will not move into the opened door immediately.

Walk through an open door
-------------------------

Checking for an open door can be done in the same way as checking for a floor tile.
However, you may want to use the following expression instead of two separate `if` statements:

.. code:: python3

    if game.level[new_y][new_x] in ".d":  # place all tiles on which you can walk here
        game.x = new_x
        ...

.. hint::

    The outcome should look like this:

    .. figure:: ../images/door_opened.png
