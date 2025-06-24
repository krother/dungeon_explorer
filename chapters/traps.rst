
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

When the player steps on a trap, you need to call the function implemented in the last chapter:

.. code:: python3

   game.take_damage()

.. hint::

   The outcome could look like this:

   .. figure:: ../images/add_traps.png

.. hint::

   The damage will be taken already when you **start moving** onto the trap.
   If you want to make it a bit nicer and apply the damage **after moving**, use the callback mechanism of the moves:

   .. code:: python3

      # player steps on a trap
      move = Move(
         ...,
         callback = take_damage,   
      )
