
0. start
- run prototype
- read code
- add up-down movement

Draw the Floor
==============

In this exercise, we will make the character walk on a stone floor.
To do so, we need to add a representation of the dungeon to the game data.

TODO IMAGE GRID

The complete feature consists of three steps:

1. create a data structure containing a map of the dungeon
2. fill the dungeon map with floor tiles
3. draw each floor tile on the screen


Create a data structure
-----------------------

First, add a new attribute to the `DungeonGame` class.
We will call it `level`:

.. code:: python3

    level: list[str]

The list will contains multiple rows. Each row represents a row on the screen.
Each row contains multiple characters, each representing a single tile in the dungeon.

.. hint::

    When you run the code, you should see an error message similar to:

    ::

       level
           Field required [type=missing, input_value={'x': 8, 'y': 1}, input_type=dict]

Fill the dungeon map
--------------------

We need to provide data for the level when the game starts.
Add a new parameter to the creation of `DungeonGame` in the `start_game()` function:

.. code:: python3

    level=[
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
    ]

Here you have a straightforward representation of a 10 x 10 dungeon.
It is a bit boring, because it only contains floor tiles.
But we will add other things soon.

.. hint::

    When you run the program, it the character should move.
    However, you cannot see the floor yet.

Draw floor tiles
----------------

The last detail is to draw the floor.
For every floor tile, we will draw the image `floor.png`.
The module responsible for the graphics is `main.py`.
We need to explicitly draw *every tile in every row*.
This is done by a loop within a loop.

Add the following code section to the function `draw()`:

.. code:: python3

    # draw dungeon tiles
    for y, row in enumerate(game.level):
        for x, tile in enumerate(row):
            draw_tile(frame, x=x, y=y, image=images["floor"])

.. hint::

   You need to figure out where in the function to position these four lines.
   When everything works, the game should look like this:

   .. figure:: floor_tiles.png

Stop at Walls
=============

At the moment, it is easy to run off the screen, crashing the program.
In this exercise, you will add walls that stop the player, also making the dungeon more interesting.

To make the walls work, you need to take care of the following:

1. add walls to the dungeon map
2. draw the walls
3. make sure the player cannot move into a wall

Add walls to the dungeon map
----------------------------

The data structure we created for the floor tiles makes it easy to edit the dungeon.
All you need to do is add walls to the level in the `start_game()` function.
Use the hash symbol `#`.

Replace a few of the floor symbols by walls, e.g. creating a border.
The size of the dungeon should not change.

.. hint::

    Running the game should work, but you won't see anything.

Draw the walls
--------------

To see the walls, you need the image `wall.png`.
In the `draw()` function in `main.py`, you need to distinguish between floors and walls.
The logic you need to add is the following:

1. go through all tiles in the level (we have this already)
2. if the tile is a floor, draw `floor.png`
3. if the tile is a wall, draw `wall.png`

Add the following lines, replacing the one inside the two loops in `draw()`:

.. code:: python3

    if tile == ".":
        draw_tile(frame, x=x, y=y, image=images["floor"])

.. hint::

    When you run the code, you should notice that some floor tiles are missing:

    .. image:: missing_floor_tiles.png

Now, add a **second if statement** similar to the first one that draws the walls.

.. hint::

    The result should look like this:

    .. image:: wall_tiles.png

Stop at walls
-------------

Currently, the player can move through the walls.
Let's stop them.
You need the following logic:

1. calculate the new position where the player *would* move
2. if there is a floor in the new position, move there
3. if there is a wall, do nothing

You need to implement this logic in the `move_player()` function.

First, copy the current position of the player:

.. code:: python3

   def move_player(game, direction: str) -> None:
       """Things that happen when the player walks on stuff"""
       new_x = game.x
       new_y = game.y
       ...

Second, modify the `if` statements so that they modify the new position instead:

.. code:: python3

    if direction == "right":
        new_x += 1
    ...

.. hint::

    At this point, the game should work, but you can still walk into walls.

Third, check for floors in the new position. For that you need to look up a tile in `game.level`.
Use **indexing**, indicated by the square brackets. Note that the y coordinate goes first:

    if game.level[new_y][new_x] == ".":
        game.x = new_x
        game.y = new_y

If the tile contains a wall, `game.x` and `game.y` will not get updated. So nothing happens.

.. hint::

    Run the game. You should see that the player cannot move into walls any mor.


Extra: Fountain
---------------

Add another element to the dungeon, e.g. a fountain using the image `fountain.png`.


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

.. hint::

    The outcome should look like this:

    .. figure:: stairs_added.png


Collect Coins
=============

In this chapter, you will add gold coins to the dungeon that the player can collect.
This feature comes with a bit more hidden complexity.
The following steps are necessary:

1. add coins to the level map
2. draw the coins
3. change the level data structure so that it can be modified
4. remove coins that have been collected
5. count the collected coins
6. create a score display

Add coins to the level map
--------------------------

You could use the Euro sign `€` for the coins in the `level` attribute of the game.
If you prefer a different currency sumbol like `$`, GBP, Renminbi, Rupee, Yen or Emoji, go for it.
Python uses **Unicode** symbols, so technically almost all symbols should work.

Add a few coins in different places of the map.

Draw the coins
--------------

Add an extra `if` statement in the `draw()` function, like in the previous cases to include the coin symbol.
The image to draw is `coin.png`.

.. hint::

    If you run the game, you should already see the coins.
    They are however impassable.

Change the level data structure
-------------------------------

The next step is a bit more technical. We have to make a modification, because the string datatype `str` in Python cannot be modified.
Replace the type definition in the `DungeonGame` class from:

.. code:: python3

    level = list[str]

to a **list of lists of single characters** or:

.. code:: python3

    level = list[list[str]]

Theoretically, you could now create your level in the `start_game()` function by making each tile a single string:

.. code:: python3

    return DungeonGame(
        x=8,
        y=1,
        level=[
            "#","#","#","#","#","#","#","#","#","#",
            "#","€","€","€",".",".",".",".",".","#",
            ...

However, this makes the level hard to read.
Instead we will use a conversion function that translates the level into the new format.

Add a new function somewhere in `game.py`:

.. code:: python3

    def parse_level(level):
        return [list(row) for row in level]

And call the function when defining the level:

.. code:: python3

    return DungeonGame(
        x=8,
        y=1,
        level=parse_level([
            "##########",
            "#€€€.....#",
            ...
        ])
    )

As you can see, the level map stays easy to edit.

.. hint::

    Try to run the code.
    The program should do the same as before.
    The coins are still not collectible, but we have made that technically possible.

    If you want to see the function in action, add the line at the end of `game.py`.
    It prints an example output for a mini-level:

    .. code:: python3

       print(parse_level([
            "####",
            "#..#",
            "####",
       ]))

Remove collected coins
----------------------

Finally you can take care of collecting the coins.
This is a small but important addition in the `move_player()` function.
The following two lines let you pick up coins:

.. code:: python3

    if game.level[new_y][new_x] == "€":
        game.level[new_y][new_x] = "."

.. hint::

    The coins should be replaced by a floor tile.

    Depending on where in `move_player()` you placed the `if` statement,
    the player will or will not move on the position of the coin.

    Try to figure out the difference and decide for the variant you prefer.

Count collected coins
---------------------

At the moment, the coins simply evaporate when they are collected.
To keep track of the number of coins, add an attribute for the number of coins to the `DungeonGame` class:

.. code:: python3

    coins: int = 0

And increase the number of coins by one in `move_player()` when a coin is collected:

.. code:: python3

    game.coins += 1

Display coins
-------------

To see how many coins the player has collected, you should add some kind of money display.
Let's put it at the right side of the dungeon.
To make space for it, you need to make the window a bit more broad in `main.py`.

**Change the value for `SCREEN_SIZE_X` to 740.**

Now you have space to draw some text there. Add the following line anywhere in the `draw()` function:

.. code:: python3



If you like, add a coin symbol next to it. Complete the following command and add it to the `draw()` function.

.. code:: python3

    cv2.putText(frame,
                str(game.coins),
                org=(730, 78),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5,
                color=(255, 128, 128),
                thickness=3,
                )

You may want to experiment with the parameter values for color, thickness and fontScale.

.. hint::

    Now you should see the number of coins in the display go up
    as you collect coins:

    .. figure:: coin_display.png


Health
======

Sooner or later, the character may get hurt.
It could be quite demotivating if the game ends at the first contact with anything harmful.
Let's add **health** as a game element.
A basic implementation needs the following:

1. add a health attribute
2. perform a regular health check that could end the game
3. draw a health bar

Health attribute
----------------

Add a new attribute `health` to the `DungeonGame` class.
It should have the type `int`. Set an initial value that you decide.

Regular health check
--------------------

The game should check regularly whether the health is still positive.
If the health becomes zero, the game should end.
This is a good opportunity to introduce an `update()` function.
It will be useful for other recurrent tasks later.

Add a new function to `game.py`:

.. code:: python3

   def update(game):
       # health check
       if game.health <= 0:
           game.status = "game over"

Now you also need to call the `update()` function.
Add a call in `main.py` in the main event loop after the drawing:

.. code:: python3

    draw(game, images)
    update(game)
    ...

You also need to import the new function on top of `main.py`

.. hint::

    The function has no effect on the game yet.
    You will only see it when you add something that actually decreases the health.

Draw a health bar
-----------------

For the health bar, you have two options. Both need to be added to `draw()`

If the maximum health is high, you could draw an actual bar.
Adjust the pixel position and color of the bar so that it looks like you want it to.:

.. code:: python3

    frame[600:600 + game.health, 100:140] = (0, 0, 255)

Alternatively, if the health is a small number, you could draw an icon.
The following line draws a series of 1-3 icons.
Complete the gap with an image of your choice:

.. code:: python3

   for i in range(game.healt):
       draw_tile(frame, xbase=620, ybase=100, x=i, y=0, ...)

.. hint::

    The outcome could look like this:

    .. figure:: health_bar.png


Traps (Optional)
================

Adding traps is an optional feature that you may want to work on.
Do this if you have extra time and would like to figure out some details on your own.
Implement the following:

- add a trap symbol to the map
- pick an image for the trap
- draw the traps
- when the player steps, on a trap, decrease their health
- decide whether the player actually should move on the trap or stop before it
- decide whether the trap disappears when triggered or stays where it is. 

.. hint::

   The outcome could look like this:

   .. figure:: add_traps.png

Code cleanup: Drawing Images
============================

In an ongoing software project, it is useful to clean up the code from time to time.
In this exercise, you will clean up the code for drawing.

When you read the code for the `draw()` function, you might notice that there are a lot of very similar lines, e.g.:

.. code:: python3

    if tile == ".":
        draw_tile(frame, x=x, y=y, image=images["floor"])
    if tile == "#":
        draw_tile(frame, x=x, y=y, image=images["wall"])

This code is unneccessarily long. The problem also becomes worse, the more different tiles you add.
The `if` statements only differ in the character and image they map to each other.

Extract a dictionary
--------------------
The character-image pairs can be more cleanly defined in a **dictionary**:

.. code:: python3

    SYMBOLS = {
        ".": "floor",
        "#": "wall",
        ...
        }

Now it is enough to **one** call to `draw_tile()` that looks up the image.
The `if` statements are completely unnecessary and can be removed:

.. code:: python3

    draw_tile(frame, x=x, y=y, image=images[SYMBOLS[tile]])

.. hint::

    Note that you will still need extra code to draw the player, health bar, coin display etc.

Add a new tile
--------------
Apart from the code getting shorter, it is much easier now to add new elements to the dungeon.
All you need to do is to add an entry to `SYMBOLS` and you can add them to your level.

Pick one or more new images and add them to beautify your level.


Keys
====

It is time to let players pick up **keys**.
They should come in useful once we add some doors as well.
To collect keys, we need to manage **items** in general.
Again, a few steps are necessary:

1. add a key tile to the dungeon
2. add an items attribute to the game
3. pick up keys
4. draw all items in the inventory

Add a key tile
--------------

This works the same as for the earlier new tiles.
Add a new character and image name to the `SYMBOLS` dictionary and add the new tile to the level.

Add an items attribute
----------------------

To store items for later, the game needs an according data structure.
For the inventory you need a data structure that can store multiple items.
The inventory needs to have an **order** so that the inventory does not randomly rearrange itself.

A good data type for that situation is a Python `list`.
Each item is going to be a string.
Add a new field `items` to the `DungeonGame` class.
At the beginning, the list of items should be empty:

.. code:: python3

   items: list[str] = []

Pick up keys
------------

To pick up a key you need to add it to the `items` list.
Add an extra condition in the `move_player()` function that checks whether a new tile is a key.
If it is, add a key to the list:

.. code:: python3

   if game.level ... :
       game.items.append("key")

Also remove it from the map (same as with coins).

Draw the inventory
------------------

Drawing the items is similar to drawing a health bar from icons.
However, you may want to collect many items later, so lets reserve more space.
To draw items in multiple rows of 2 items each use the following loop in `draw()`:

.. code:: python::

    for i, item in enumerate(game.items):
        y = i // 2  # floor division: rounded down
        x = i % 2   # modulo: remainder of an integer division
        draw_tile(frame, xbase=660, ybase=96, x=x, y=y, image=images[item])
       

.. hint::

   Multiple keys in an inventory could look like this:

   .. figure:: add_keys.png

   If you like, you might create multiple keys as long as they have different symbols and names: `b:blue_key`, `r:red_key` etc.


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

    .. figure:: door_opened.png


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
A single tile on the map cannot hold all that information, considering you may want to have mulitple teleporters on the map.

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

    .. figure:: add_teleporter.png

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

Switch (Optional)
=================

Create a switch that opens a secret door.
Implement the following:

- the switch should replace one specific wall by an open door
- create a switch class that holds the position of the wall
- the switch is activated when you walk on it 
- look for a switch tile on `opengameart.org <https://opengameart.org>`__


Code Cleanup: Split a Function
==============================

You may observe that the function `move_player()` has become quite long.
Long function are harder to understand and are a frequent source of bugs.
In this exercise, you will extract two shorter functions from the longer one.

This coding strategy, called **refactoring**, uses the following pattern:

1. run the tests
2. edit the code
3. run the tests again

Run the tests
-------------

To make sure that the program does what it should, run the tests before you start.
Do this even if you built the test right before.
Even a small thing can ruin everything.

The test runner should confirm everything is OK:

::

    python -m pytest

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

.. warning::

    Before doing anything else, proceed with the following step.

Run the tests again
-------------------

Now run the tests to make sure that you did not break anything crucial with:

::

    python -m pytest

If it does not work, you need to fix the problem immediately or rewind your changes.

.. hint::

    It is also a good idea to run the game and see whether there is anything unusual.

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


Healing Potion (Optional)
=========================

Add a healing potion to the dungeon that restores some health if you ran into spikes or got scorched by a few fireballs.

Figure out by yourself how to do that.


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

    .. figure:: add_skeleton.png   


Multiple Levels
===============

- move level to file levels.py
- move SYMBOLS, parse_level and get_map_tiles to levels.py
- create LEVEL class
- create LEVELS list
- create new level
- add Game.current_level, Game.level
- move monters to Level
- extract start_level function

More Monsters (Optional)
========================

Look through the tiles.
Add another monster with slightly different properties, e.g.:

- move half as fast
- move through closed doors
- do a lot of damage
- do less damage if the player has an armor
- spawn fireballs (the fireballs should disapper when they hit a wall)


1.  title screen
- add cutscene
- add title screen
- add 2 end screens
- edit README
- add LICENSE
- everything to GitHub

- move move_fireball() and check_collision to monsters.py
- move it to module helpers.py
- move classes into new module data_model.py
- extract position class

-------------
1.

Warm-up to learn about existing skills about computers and programming. Brief overview of the course and programming methodology.

Participants work through an installation guide to set up their Python environment. They run a prototype program that they will start developing with, displaying a player in a 2D dungeon. The session is concluded by reading the code together.

Key concepts: Python interpreter, editor, instructions, logging

-----

2.

Participants make the player move around in a dungeon using the keyboard.
They complete the existing left/right movement from the prototype using a step-by-step guide. Fast students edit the level in a text editor.

Key concepts: integer, string, nested list, indexing, arithmetics.

-----

3.

Participants make the player stop at walls.
They implement new code using a step-by-step guide. Fast students implement a pit that the player should avoid falling into.

Key concepts: conditional expressions, variable assignments

-----

4.

Participants add their own graphic elements.
They examine, how symbols used during the game are mapped to graphics. It is discussed why an abstraction is necessary. They browse the OpenGameArt website for graphics they want to use and add them to the game.

Key concepts: files, abstraction, dictionary

-----

5.

Participants make the player pick up keys .
They implement an inventory that can contain multiple items using a step-by-step guide. Fast students add more items players can collect.

Key concepts: lists, appending, indexing and removing.

-----

6.

Participants make the player use keys to unlock doors.
When walking into a door, it is checked whether the player has the according key. Fast students add custom graphics to have more types of keys available.

Key concepts: conditional expressions, list ‘in’ operator

-----

7.

Participants create teleporters that transport the player to another location.
They implement a data structure that can be used to look up multiple teleporters and their destinations.
Fast students implement switches that open secret doors or close pits.

Key concepts: dictionary, key, value, tuple

-----

8.
Participants split the growing code into multiple functions.
They use existing automated test code to make sure that the change does not break things. They publish their code before and after the change. Fast students implement their own test code.

Key concepts: function, function argument, return, refactoring, automated test

-----

9.
Participants create dangerous fireballs that move.
They implement a fireball that is spawned in regular intervals and moves along a straight line until it hits a wall. Fast students create fireballs in multiple locations and/or directions.

Key concepts: update cycle, data model, attributes

-----

10.
Participants make the fireballs hurt if they hit a player.
The position of player and fireball is compared regularly and the health of the player decreased on a hit. The code is split into modules. Fast students implement a healing potion.

Key concepts: modules, import

-----

11.
Participants create skeletons that chase the player.
The skeletons follow a random move pattern, making them much more dangerous. Fast students implement an orc with a smarter move pattern and/or create a dragon that spits fireballs.

Key concepts: random module, builtin modules

-----

12.
Participants enable players to defeat monsters.
They implement code to attack adjacent monsters and remove them from the game. They define a helper function that handles the ‘attack’ action. Fast students implement extra melee and/or ranged weapons.

Key concepts: use case, function design, function scope, local vs global variables

-----

13.
Participants create a dungeon with 2+ levels.
They define a level data structure containing a floor plan, items, doors, switches, monsters etc. Stairs move the player to the next level. Fast students create more levels.

Key concepts: state diagram, global vs. local variables

-----
14.
Participants store levels in files.
They implement code that loads levels from a directory with JSON files using a defined format. Levels are uploaded to GitHub, and students are encouraged to include each others’ level designs. Fast students create more levels.

Key concept: file paths, read/write functions, JSON 

-----

15.
Participants create a front page for their software.
They edit the README file to include installation instructions, a screenshot of their game, a license. They also add an in-game title banner.
