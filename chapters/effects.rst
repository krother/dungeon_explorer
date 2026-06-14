
Special Effects
===============

In this chapter, you learn to create customized special effects that use **direct pixel manipulation**.
To accomodate different effects, you will use **subclasses** and **methods**.

1. Create an effects module
---------------------------

Place the effects in a new file ``effects.py``.
Create a new class ``Effect`` there.
This class is a **superclass**, a generic structure that does not represent any effect in particular.

Note that it contains a **method**, a function attached specifically to that class.
You can recognize methods by the special parameter ``self``.
It contains only the command ``pass`` that does nothing.

.. code:: python

   import numpy as np
   from pydantic import BaseModel
   
   TILE_SIZE = 64

   class Effect(BaseModel):
   
       x: int
       y: int
       countdown: int
   
       def draw(self, frame):
           pass

2. Add a subclass
-----------------

Now let's create an actual effect: random blur.
Create a **subclass**. It has the same data structure as ``Effect``, but replaces the ``draw()`` method:

.. code:: python

    class RandomBlur(Effect):

        def draw(self, frame):
            random_tile = np.random.randint(0, 255, size=(TILE_SIZE, TILE_SIZE, 3), dtype=np.uint8)
            frame[self.y * TILE_SIZE: self.y * TILE_SIZE + TILE_SIZE,
                self.x * TILE_SIZE: self.x * TILE_SIZE + TILE_SIZE] = random_tile

3. Add effects to the game
--------------------------

Add an effects attribute to the DungeonGame class:

.. code:: python

    effects: list[Effect] = []

But to add an actual effect, you would use the subclass.
Add the effect either in ``start_game`` or whenever something interesting happens, e.g. telportation.

.. code:: python

   game.effects.append(RandomBlur(x=8, y=1, countdown=500))

For both, add the according imports to ``game.py``.

4. Draw the effect
------------------

To see anything, you need to call the draw method to ``main.draw()``:

.. code:: python

    # draw special effects
    for e in game.effects:
        e.draw(frame)

Now you should already see the effect, but it does not stop.

.. note::

    You do not need to supply a value for the ``self`` parameter.
    For ``self``, Python uses the **intstance** (in this case ``e``) automatically.
    
    If you find that a bit confusing, I'm with you.

5. Countdown and cleanup
------------------------

For the effect to expire, you need to decrease the countdown of the effect.
Then clean up the expired ones.
Add a function anywhere in ``game.py`` or ``main.py``:

.. code:: python

    def update_effects(game):
        new_effects = []
        
        # add a loop that decreases the countdown for all effects
        # and only collect those where it is greater than zero
        
        game.effects = new_effects

Call the function in the while loop in ``main.py`` or the ``update()`` function in ``game.py``:

.. hint::

   If you are in for a challenge, write the function directly into the ``DungeonGame`` class as a method.
   For clarity, rename ``game`` to ``self`` in the method.
   Call it with:

   .. code:: python

      game.update_effects()

6. More effects
---------------

Here is a simple fading effect:

.. code:: python

    class FadeIn(Effect):

        def draw(self, frame):
            tile = frame[self.y * TILE_SIZE: self.y * TILE_SIZE + TILE_SIZE,
                self.x * TILE_SIZE: self.x * TILE_SIZE + TILE_SIZE]
            tile[tile > (255 - self.countdown)] = 0
            frame[self.y * TILE_SIZE: self.y * TILE_SIZE + TILE_SIZE,
                self.x * TILE_SIZE: self.x * TILE_SIZE + TILE_SIZE] = tile


Here is some blinking text with an extra attribute:

.. code:: python

    class ColorText(Effect):

        text: str
        
        def draw(self, frame):
            if self.countdown % 2 == 0:
                color = (255, 0, 255)
            else:
                color = (0, 255, 255)
            cv2.putText(frame,
                self.text,
                org=(self.y * TILE_SIZE, self.x * TILE_SIZE),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.0,
                color=color,
                thickness=2,
            )


.. seealso::

    - `Academis NumPy Tutorial <https://www.academis.eu/numpy_graphics/>`__ – simple NumPy drawing examples
    - `Pixels2GenAI <https://burakkagann.github.io/Pixels2GenAI/>`__ – in-depth graphics tutorial by Burak Kagan Yilmazer
