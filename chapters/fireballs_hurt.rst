
Fireballs Hurt
==============

It is great to watch your fireballs fly around.
However, they are not very dangerous.
Let's make them more harmful.

Add a collision check to the `update()` function, comparing the position of the player to that of each fireball.
Complete the code:

.. code:: python3

    def check_collision(game):
        for f in game.fireballs:
            if f.x == game.x and ...:
                game.health -= ...

Decide **how much** damage a fireball should do.

Then add a call to the `check_collision()` function to `update()`. This takes care of **fireballs moving into the player**.
Add another call to `check_collision()` to the `move_player()` function, so that it also hurts when **the player moves into a fireball**.

.. hint::

    When the feature works, you may want to move some of the code in `update()` to a separate function.
