Skeletons
=========

Diversity is good! This also applies to the opponents in your dungeon.
Let's add a randomly moving skeleton.

For adding the skeleton, you can copy the mechanics of the fireball in most aspects.
The only thing that is really different is the movement pattern.
Add the following (somewhat dumb) random movement:

.. code:: python3

    import random  # add this on top of game.py

    # move skeletons (in update())
    for s in game.skeletons:
        direction = random.choice(["up", "down", "left", "right"])
        ...

Don't forget to include the skeleton in the collision detection.

.. hint::

    By now there is a lot going on:

    .. figure:: ../images/add_skeleton.png   
