Teleporters 
===========

Your implementation is getting towards more and more complex features.
In this exercise, you will add a teleporter that transports the player to a different location.
A teleporter is more complex than the coins, keys and doors in the previous chapters.
You will need to create an own data structure for it.
The following steps are necessary:

1. create a teleporter class
2. add a teleporter to the level
3. draw the teleporter
4. teleport the player

Create a teleporter class
-------------------------

The reason you need a new class is that you need not only to store where a teleporter is, but also where it should transport the player. 
A single tile on the map cannot hold all that information, considering you may want to have multiple teleporters on the map.

Create a new class `Teleporter` that contains the x/y-position of a teleporter and the position it teleports to:

.. code:: python3
  
    class Teleporter(BaseModel):
        x: int
        y: int
        target_x: int
        target_y: int


Add a teleporter to the level
-----------------------------

To add one or more teleporters to the dungeon, you also need to add a single line to the `DungeonGame` class:

.. code:: python3

   teleporters: list[Teleporter] = []

Now add a teleporter in the `start_game()` function right after the `level` attribute:

.. code:: python3

    teleporters=[
        Teleporter(x=1, y=2, target_x=2, target_y=8),
    ]

Note that you do not need to edit the level map!


Draw the teleporter
-------------------

One drawback of having teleporters as their own attribute is that you need to draw them explicitly.
In the `draw()` function, add the following paragraph **after** drawing the level tiles:

.. code:: python3

    # draw teleporters
    for t in game.teleporters:
        draw_tile(frame, x=t.x, y=t.y, image=images["teleporter"])

.. hint::

    Now you should see the teleporter. Although you can walk into it, it does not teleport anything:

    .. figure:: ../images/add_teleporter.png

Teleport the player
-------------------

A teleporter should move the player as soon as they step on it.
In a first attempt, we will simply check all teleporters in the `move_player()` function.
Complete the following code:

.. code:: python3

   for t in game.teleporters:
       if game.x == t.x and ...:
           game.x = t.target_x
           ...

As soon as you add the complete section at the bottom of `move_player()`, your teleporter should start working!

.. hint::

    The approach with the loop is not the most efficient one,
    but Python is more than fast enough to get away with it.
