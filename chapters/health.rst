
Health
======

Sooner or later, the character may get hurt.
It could be quite demotivating if the game ends at the first contact with anything harmful.
Let's add **health** as a game element.
A basic implementation needs the following:

1. add a health attribute
2. make it possible to take damage
3. draw a health bar

Health attribute
----------------

Add a new attribute ``health`` to the ``DungeonGame`` class.
It should have the type ``int``. Set an initial value that you decide.

Take damage
-----------

In the game it should be possible to lose health.
If the health becomes zero, the game ends.
Add this as a simple function in ``game.py``:

.. code:: python3

   def take_damage(game):
       game.health -= 1
       if game.health <= 0:
           game.status = "game over"


.. hint::

    This function has no effect on the game yet.
    We will call it in the next chapter.

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

   for i in range(game.health):
       draw_tile(frame, xbase=620, ybase=100, x=i, y=0, ...)

.. hint::

    The outcome could look like this:

    .. figure:: ../images/health_bar.png
