The Observer Pattern
====================

Read about the `Observer Pattern <https://sourcemaking.com/design_patterns/observer>`__ . Implement it for **collision detection**:

- the `DungeonGame` class keeps a list of objects that need to be notified
- every time a player or monster changes their position, check for collisions
- each notified object has a `check_collision()` method

Use the signature:

.. code:: python3

    class Observable:

        def check_collision(other: Player|Monster) -> bool:
            ...


.. hint::

    Consider implementing the `__del__` method (the destructor in Python) so that objects can unregister themselvers.
