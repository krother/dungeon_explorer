
Save and Load the Game
======================

In a long game, you want to save your progress and continue later.
We will use the JSON format since it is dictionary-like and easy to read.
The ``json`` module is useful for saving pydantic objects.

Step 1: Convert game to json
----------------------------

The ``model_dump_json()`` method converts the entire game state to a JSON string:

.. code-block:: python

   j = game.model_dump_json()
   print(j)

.. note::

   ``game.model_dump()`` returns a Python dictionary instead of a string.

Step 2: Save json data to file
------------------------------

Write the JSON string to a file:

.. code-block:: python

   with open("save.json", "w") as f:
       f.write(j)


Step 3: Load the game
---------------------

Use the ``json`` library to read the game data back:

.. code-block:: python

   import json
   with open("save.json", "r") as f:
       d = json.load(f)
       print(d)

``d`` should now be a dictionary with all the game data.

Step 4: Convert dictionary to DungeonGame object
------------------------------------------------

Pass the dictionary to the ``DungeonGame`` constructor to restore the game:

.. code-block:: python

   from game import DungeonGame
   game = DungeonGame(**savegame)

Step 5: Add load/save buttons
-----------------------------

You can define keys in the ``MOVES`` dictionary in ``main.py``:

.. code-block:: python

   MOVES = {
       "l": "load",
       ...
   }

Then in the while loop, use the resulting commands:

.. code-block:: python

           # load and save the game
           if queued_move == "save":
               # add code for saving
               ...
           elif queued_move == "load":
               # add code for loading
               game = ...
           elif not is_player_moving(moves) and queued_move:
               move_player(game, queued_move)
