Fireball!
=========

Now it is time for some serious action.
You will add a fireball that moves back and forth in the dungeon.
This is by far the most complex feature so far, but it can be done in small steps.
Also, you have already created a lot of similar code that should help.
The following steps are necessary:

1. create a Fireball class
2. add a fireball to the level
3. draw the fireball
4. move the fireball
5. Slow down the fireball

Create a Fireball class
-----------------------

You need a new class, so that the fireball can move independently.
Also, this makes it possible to add many fireballs.

Create a new class `Fireball` with the following attributes:

- an x and y position
- a direction indicating where the fireball will move, e.g. `"up"`

The other classes should have enough examples that you can borrow from.

Add a fireball to the level
---------------------------

The game needs to store the fireballs as a extra list.
Add a new attribute to the `DungeonGame` class that is a list of fireball objects.
You can borrow the strategy from the `Teleporter` class, the code should be very similar.

Also, create a fireball when the level is created.
Create a single fireball first.
Decide on a starting position and a direction.

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

The logic to move the fireball is as follows:

- calculate the position where the fireball would move
- if that square is free, move there
- if not, turn around

Implement these steps in the `update()` function:

.. code:: python3

    # move fireballs
    for f in game.fireballs:
        new_x, new_y = get_next_position(f.x, f.y, f.direction)
        if game.level[new_y][new_x] in ".€k":  # flies over coins and keys
            f.x, f.y = new_x, new_y

You also need to take care of the situation when the fireball hits an obstacle.
In that case, reverse the direction:

.. code:: python3

        elif f.direction == "right":
            f.direction = "left"
        ..

Add the code for other direction changes you would like to have.

.. hint::

    It might be a good idea to move the code into a separate function.
    But for now you should rejoice if you see a moving fireball!


Slow down the fireball
----------------------

Depending on your machine, the fireball is either very fast or insanely, abysmally fast.
For any human player to have a chance dodging it, you need to make the movement slower.

A good place to control the speed of the game is in `main.py`. 
We will simply call `update()` less frequently.

Modify the `while` loop by adding a counter variable that counts the game cycles (or frames):

.. code:: python3

    counter = 0
    while game.status == "running":
        counter += 1

Now you can use the modulus to call `update()` in every 100th cycle:

.. code:: python3

    if counter % 100 == 0:
        update(game)

Adjust the number until you have a speed that you think is good.
