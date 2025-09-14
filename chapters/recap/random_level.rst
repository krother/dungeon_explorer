
Random Level Generator
======================

Let's write a better level generator.
This time, the level should contain some random walls, coins and traps.

First, import some libraries:

.. code:: python3

   import random
   import pprint  # pretty-print

Next, define an empty list. We want to fill it with 10 rows, each containing a **list** of 10 floor tiles.
Complete the gap:

.. code:: python3

   level = []
   for i in range(10):
       level.append(...)
   pprint.pprint(level)

Now, roll a random position and a random tile.
Modify the list accordingly.
Complete the gaps in the code:

.. code:: python3

    x = random.randint(0, 9)
    y = ...
    tile = random.choice(["#", "€", "T"])
    level[...][...] = ...
    pprint.pprint(level)

Repeat the above 50 times.

If you would like to use the level in the game, you need to reformat everything to a list of strings.
Use the following code:

.. code:: python3

   for row in level:
       print("list('" + ''.join(row) + "'),")
