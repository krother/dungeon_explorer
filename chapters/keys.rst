
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

.. code:: python3

    for i, item in enumerate(game.items):
        y = i // 2  # floor division: rounded down
        x = i % 2   # modulo: remainder of an integer division
        draw_tile(frame, xbase=660, ybase=96, x=x, y=y, image=images[item])
       

.. hint::

   Multiple keys in an inventory could look like this:

   .. figure:: ../images/add_keys.png

   If you like, you might create multiple keys as long as they have different symbols and names: `b:blue_key`, `r:red_key` etc.
