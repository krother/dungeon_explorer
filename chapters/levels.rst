
Multiple Levels
===============

A game with only one level makes the game quite boring.
In this exercise, you will build more levels and make it possible to travel between them.
You will need to reorganize the code a bit:

1. Split the `DungeonGame` class
2. Update references to attributes
3. Create more levels
4. Switch between levels

Split the DungeonGame class
---------------------------

First, you need to change the data structure.
Currently, the `DungeonGame` class contains a few things that change between levels and others that don't.
You need to separate them.

Create a new class `Level` and move some attributes from `DungeonGame` there:

.. code:: python3

    class Level(BaseModel):
        level: list[list[str]]
        teleporters: list[Teleporter] = []
        fireballs: list[Fireball] = []
        skeletons: list[Skeleton] = []

The other attributes remain in `DungeonGame`:

.. code:: python3

    class DungeonGame(BaseModel):
        status: str = "running"
        x: int
        y: int
        coins: int = 0
        health: int = 150
        items: list[str] = []

Additionally, you need an attribute in `DungeonGame` that refers to the current level:

.. code:: python3

        current_level: Level

You also need to separate the two in the `start_level()` function.
Define the level object first:

.. code:: python3

    level_one = Level(
        level=parse_level([
            ...
        ])
        teleporters=[...],
        fireballs=[...],
        skeletons=[...],
    )

Then use that level when creating a `DungeonGame` object:

.. code:: python3

    return DungeonGame(
        x=8,
        y=1,
        current_level=level_one
    )

.. hint::

    The game will not run at this point.


Update references to attributes
-------------------------------

Because you moved attributes to the `Level` class, many references to them will not work.
You have to update many references to `game.something` to `game.current_level.something`.
For instance in `update()` the code may look like this:

.. code:: python3

    for f in game.fireballs:
        new_x, new_y = get_next_position(f.x, f.y, f.direction)
        if game.level[new_y][new_x] in ".€kd":
            ...

Change it to:

.. code:: python3

    for f in game.current_level.fireballs:
        new_x, new_y = get_next_position(f.x, f.y, f.direction)
        if game.current_level.level[new_y][new_x] in ".€kd":
            ...

Do the same for all attributes of the `Level` class in `update()`, `move_player()`, `check_collision()` and `draw()`.
If you extracted other functions, they may need to be changed, too.

.. hint::

    When you are done, the game should run again.
    If you have automated tests, they should help a lot.

Create more levels
------------------

Now you can create more levels by defining more `Level` objects.
To make it easier to use them later, define them at the top level of the program.

To indicate that the levels are global variables, you could use capital letters:

.. code:: python3

    LEVEL_TWO = Level(
        ...
    )

Move `level_one` from the `start_level()` function next to the new level(s) and rename it to `LEVEL_ONE`.

Switch between levels
---------------------

Now you can define a global list with all the levels in the game:

.. code:: python3

    LEVELS = [LEVEL_ONE, LEVEL_TWO, ...]

Add an attribute to the `DungeonGame` class indicating which level the player is in (0 corresponds to the first level):

.. code:: python3

    level_number: int = 0

All that is left to do is to increase that number when the player uses stairs.
If there is another level left, it is activated. When leaving the final level, the game should end.
Add the following code to the `move_player()` function, replacing the code handling stairs:

.. code:: python3

    if game.current_level.level[new_y][new_x] == "x":
        game.level_number += 1
        if game.level_number < len(LEVELS):
            # move to next level
            game.current_level = LEVELS[game.level_number]
        else:
            # no more levels left
            game.status = "finished"

 
.. hint::

    The way this code is organized the levels are not thrown away once the player leaves them.
    They are kept in memory in exactly the state you left them in.
    That means, if you would like to include stairs that bring you back to a level visited earlier,
    it is possible.

    Now you can build puzzles that take you back and forth across the dungeon!
