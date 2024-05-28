
Exit Stairs
===========

Let's add stairs to the dungeon.
When the player steps on the stairs, the game should finish.
You need to take care of three thing:

1. add stairs to the level
2. draw the stairs
3. end the game when the player steps on the stairs

Add stairs to the level
-----------------------

To represent the stairs, use the symbol `x`.
Add it to the level in `start_game()` in a similar way as before.

Draw the stairs
---------------

Add an extra `if` statement in `draw()` that draws the image `stairs_down.png`.

End the game
------------

The game is controlled by the variable `game.status`.
As soon as it will contain anything else than `"running"`, the game will stop.

Now you can add the following logic to `move_player()`:

.. code:: python3

    if game.level[new_y][new_x] == "x":
        game.status = "finished"
