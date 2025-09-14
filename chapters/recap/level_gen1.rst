
A simple level generator
========================

Let's implement a very straightforward level generator.
The following program should print an empty 10 x 10 box.

**Put the lines in the correct order and run the code.**

.. code:: python3

    border = wall * 10
    center = wall + floor * 8 + wall
    border += "\n"
    print(level)
    center += "\n"
    wall + floor * 8 + wall
    floor = "."
    level = border + center * 8 + border
    wall = "#"
