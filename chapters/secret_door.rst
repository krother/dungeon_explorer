
Secret door (Optional)
----------------------

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

.. note::

   At the moment, the location of the secret door and the trigger are hardcoded.
   To make the mechanics more generic (e.g. to have multiple secret doors),
   you will need the **dictionary** data structure.
   Dictionaries will be introduced in the chapter :ref:`teleporters`.