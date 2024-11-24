Code Cleanup: Split a Function
==============================

You may observe that the function `move_player()` has become quite long.
Long function are harder to understand and are a frequent source of bugs.
In this exercise, you will extract two shorter functions from the longer one.


Edit the code
-------------

First, move the code for handling teleportation into a separate function.
Give the function the following header:

.. code:: python3

   def check_teleporters(game):
       ...

Move the block of code for teleportation from `move_player()` to `check_teleporters()`.
Then call the new function from `move_player()` exactly where you took the code from:

.. code:: python3

   check_teleporters(game)


.. hint::

    Before doing anything else, run the game and see whether there is anything unusual.

Extract another function
------------------------

Once the code is working, extract another function for calculating the position of the next tile.
Follow the same procedure as above.
Define a function with a `def` statement and a return at the end:

.. code:: python3

   def get_next_position(x, y, direction):
       ...
       return x, y

Move the code that modifies coordinates into the new function, replacing `new_x` by `x` and `new_y` by `y`.
Add a function call to `move_player()`:

.. code:: python3

   new_x, new_y = get_next_position(game.x, game.y, direction)

In the end, everything should work as before.

.. hint::

    This change has no effect on the game itself.
    But the new function will be useful as soon as we add more game elements that move around!
