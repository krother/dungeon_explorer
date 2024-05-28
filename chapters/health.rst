
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

    .. figure:: ../images/health_bar.png
