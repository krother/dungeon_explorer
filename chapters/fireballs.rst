Fireballs
=========

Now it is time for some serious action.
You will add a fireball that moves back and forth in the dungeon.
This is by far the most complex feature so far, but it can be done in small steps.
Also, you have already created a lot of code that should help.
The following steps are necessary:

1. create a Fireball class
2. add a fireball to the level
3. draw the fireball
4. move the fireball
5. slow down the fireball
6. make the fireball cause damage

Create a Fireball class
-----------------------

You need a new class, so that the fireball can move independently.
Also, this makes it possible to add many fireballs.

Create a new class ``Fireball`` with the following attributes:

- a x position
- a y position
- a direction indicating where the fireball will move, e.g. ``"up"``

You can borrow examples from the other classes.

Add a fireball to the level
---------------------------

The game needs to store the fireballs as an extra list.
Add a new attribute to the ``DungeonGame`` class that is a list of fireball objects.
You can borrow the strategy from the ``Teleporter`` class, the code should be very similar.

- Also, create a fireball when the level is created.
- Create a single fireball first.
- Decide on a starting position and a direction.

.. hint::

    The game should run without any visible changes at this point.

Draw the fireball
-----------------

The drawing is not that different either.
Copy the section in `draw()` that draws teleporters and draw `fireball.png` instead.

.. hint::

    Now you should see a fireball that does not move.

    .. figure:: ../images/add_fireball.png

Move the fireball
-----------------

The logic to move a fireball is as follows:

- calculate the position where the fireball would move
- if that square is free, move there
- if not, turn around

Implement these steps in a new function ``move_fireball()``:

.. code:: python3

    def move_fireball(game, fireball):
        new_x, new_y = get_next_position(fireball.x, fireball.y, fireball.direction)
        if game.level[new_y][new_x] in ".€k":  # flies over coins and keys
            fireball.x = new_x
            fireball.y = new_y

You also need to take care of the situation when the fireball hits an obstacle.
In that case, reverse the direction:

.. code:: python3

        elif fireball.direction == "right":
            fireball.direction = "left"
        ..

Add the code for other direction changes you would like to have.

Check if the program is running although nothing is moving yet.

Regular updates
---------------

The fireballs need to be moved regularly. 
Add a new function ``update()`` to ``game.py`` that moves **all** the fireballs:

.. code:: python3

    def update(game):
        for f in game.fireballs:
            move_fireball(game, f)

Import and call the update function in ``main.py`` in the ``while`` loop after drawing:

.. code:: python3

    from game import update

    while game.status == "running":
        draw(game, images, moves)
        update(game)

Run the game. Now you should see a fireball moving.

Slow down the fireball
----------------------

Depending on your machine, the fireball is either very fast or insanely, abysmally fast.
For any human player to have a chance dodging it, you need to make the movement slower.

The smooth movement mechanism will help with that.
If you make sure that the new movement does not start before an old one finishes, the speed should become manageable.

First, the fireball needs to remember its move to check if it is finished.
Add to the ``Fireball`` class:

.. code:: python3

    class Fireball:
        ...
        move: Move = None


Now, create smooth moves in the ``move_fireball()`` function. They need to be added to **both** the fireball and the game:

.. code:: python3

    def move_fireball(game, fireball):
        ...
        fireball.move = Move(
            tile="fireball",
            from_x=fireball.x, from_y=fireball.y,
            speed_x = ..., speed_y = ...
        )
        game.moves.append(fireball.move)

.. hint::

   Figuring out the right values for ``speed_x`` and ``speed_y`` can be tricky. It either requires a lot of ``if`` commands. An easier alternative is to calculate it from the old and new x position!

Now the trick is to only update the fireballs if they have completed their move.
Modify the ``update()`` function:

.. code:: python3

    def update(game):
        for f in game.fireballs:
            if f.move and f.move.complete:
                move_fireball(game, f)

Now the fireball should move smoothly and in an acceptable speed!

Make the fireball cause damage
------------------------------

It is great to watch your fireballs fly around.
However, they are not very dangerous.
Let's make them more harmful.

Add a collision check, comparing the position of the player to that of each fireball.
Complete the code:

.. code:: python3

    def check_collision(game):
        for f in game.fireballs:
            if f.x == game.x and ...:
                take_damage()

Then add a call to the ``check_collision()`` function at the end of the ``update()`` function.
This takes care of **fireballs moving into the player**.

Add another call to ``check_collision()`` to the ``move_player()`` function, so that it also hurts when **the player moves into a fireball**.
