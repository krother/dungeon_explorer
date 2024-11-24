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

    level: list[str]

to a **list of lists of single characters** or:

.. code:: python3

    level: list[list[str]]

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

    cv2.putText(frame,
                str(game.coins),
                org=(730, 78),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5,
                color=(255, 128, 128),
                thickness=3,
                )

You may want to experiment with the parameter values for color, thickness and fontScale.
If you like, add a coin symbol next to it.

.. hint::

    Now you should see the number of coins in the display go up
    as you collect coins:

    .. figure:: ../images/coin_display.png
