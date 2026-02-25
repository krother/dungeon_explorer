Smooth Movement
===============

For a better experience, the player figure should not *jump* from one tile to the next, but rather *slide*.
This makes the drawing more complex. What you want to happen is something like this:

1. the player presses a move key
2. set a counter to 0
3. draw the player figure at the position + counter
4. increase the counter by one
5. repeat from 3. until the figure has completed its movement

This gets more complicated, because other things might happen in the meantime: the player presses another key that should be executed once the movement completes, or monsters move around as well.
The code in `main.py` can handle this kind of situation already.
You still need to tell it what to do.
In this chapter, you will create a **data structure for moves**.

A new module
------------

Start by defining what a *"Move"* is.
A Move should represent a graphical element that moves on the screen.
It needs a starting position, a direction and what graphical tile is moving.
We also need a counter that tracks how far the movement has proceeded.
This structure is generic enough that we can use it not only for the player, but also for other things.

Create a new Python file ``moves.py`` in the same directory as your other code.
Insert the following code:

.. code:: python3

    from typing import Callable
    from pydantic import BaseModel

    class Move(BaseModel):
        tile: str
        from_x: int
        from_y: int
        speed_x: int
        speed_y: int
        progress: int = 0
        complete: bool = False
        finished: Callable = None

.. warning::

    Do not change any of these names, the code in `main.py` needs them.

Import the module
-----------------

Now you can use the ``Move`` class in your program.
First, the ``game.py`` module needs to know about it.
Add on top of the ``game.py`` file:

.. code:: python3

    from moves import Move

and add to the ``DungeonGame`` class:

.. code:: python3

    moves: list[Move] = []

Test the program. It should still work although the movement looks the same as before.

Create moves
------------

Every time the player moves, you would add a new ``Move`` object and add it to ``game.moves``.
The ``main.py`` module does the rest. Add to the ``move_player()`` function:

.. code:: python3

    if direction == "right":
        move = Move(tile="player",
                    from_x=game.x, from_y=game.y,
                    speed_x = 2, speed_y = 0
                    )
        game.moves.append(move)
        game.x += 1

When you start the game, you should see the figure moving smoothly to the right.

Add similar code for the other directions as well.

.. hint::

   to make the figure move to the left, you will need a negative value.
   Try different speed parameters and see which one works best.

A secret door
-------------

You can use the ``moves`` mechanics for other things as well.
Lets add a secret door that opens when you reach a specific location.
You need the following steps to happen:

1. check if the player has reached the location opening the secret door
2. replace a wall by a floor tile
3. create a move of a wall tile

Implement all of this at the end of the ``move_player()`` function.
Complete the following code:

.. code:: python3

   if game.x == ... and ...:
      game.level[3][2] = "."  # wall in row 4 column 3
      move = Move(tile="wall",
                  ...
      )


Callback functions (Optional)
-----------------------------

Sometimes you may want something specific to happen exactly **after** a movement ends.
A powerful mechanic for this kind of behavior is using a **callback function**.
In the ``Move`` class, you can add callback functions that are called when the movement ends.

You don't need this for any game feature right now, but maybe you get some good ideas from it.
Here is a proof of concept. First, define the callback function:

.. code:: python3

    def player_move_finished(game):
        """outputs the coordinates of the player"
        print(game.x, game.y)

Then specify the callback when creating a move:

.. code:: python3

    move = Move(tile="player",
                    from_x=game.x, from_y=game.y,
                    speed_x = 2, speed_y = 0,
                    finished = player_move_finished,
                    )
    game.moves.append(move)

.. note::

    Do not include round brackets after ``player_move_finished``, because ``main.py`` takes care of calling it.


Adjusting damage events
-----------------------

Without modifications, damage from traps and monsters will be taken already when you **start moving** onto the trap.
If you want to make it a bit nicer, apply the damage **after moving**. 
Use the callback mechanism of the moves:

.. code:: python3

    # player steps on a trap
    move = Move(
        ...,
        finished = take_damage,   
    )
