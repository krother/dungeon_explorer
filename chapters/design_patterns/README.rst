
The Facade Pattern
==================

Implement the `Facade Pattern <https://sourcemaking.com/design_patterns/facade>`__ for the class `DungeonGame`.
The Facade class should serve as the **only** contact point with the UI, so that:

- the UI (`main.py`) only accesses attributes and methods of the Facade.
- the UI may use auxiliary data structures (e.g. models returned by Facade methods)
- the `DungeonGame` class or any classes beneath contain any UI code (textures, drawing, screen I/O)
- the graphics engine in UI could be replaced, without modifying the Facade
- the Facade serves as a contact point for writing test code.

Automated Tests
===============

Write one or more Unit Tests against the Facade.
See `https://github.com/krother/advanced_python_de/tree/main/solutions/packages/space-package/tests` for an example of test code.

----

The Strategy Pattern
====================

Implement the `Strategy Pattern <https://sourcemaking.com/design_patterns/strategy>`__ to move traps and monsters in the game.
There should be multiple **movement patterns** that can be freely combined with monsters.
Each monster should have a `movement` attribute that references the strategy.

Implement the following strategies:

- no movement at all
- move left-right until an obstacle is hit
- move up-down until an obstacle is hit
- move randomly

Instead of implementing each strategy as a class, Python gives us the option to use a generator.
Consider the following signature:

.. code:: python3

    Position = tuple[int, int]

    def move_always_left(dungeon: DungeonGame) -> Iterable(Position):
        while True:
            yield "left"

The strategy will require a dungeon object to check for obstacles.
Use the strategy in a monster class:

.. code:: python3

    class Monster:

        def __init__(self, dungeon):
            self.movement = move_always_left(dungeon)

        def update():
            self.position = next(self.movement)

----

The Repository Pattern
======================

Add a save/load functionality to the game. Implement the Repository Pattern.
Consider the following:

- put the repository in a separate module
- create a repository class
- for the class, use the `Singleton Pattern <https://sourcemaking.com/design_patterns/singleton>`__ (use the Python code example)
- the repository class should have two methods `load` and `save`
- choose a library for serialization (consider `pickle`, `json`, `sqlite` or `duckdb`)
- only one saved game should exist at any given time
- none of the code outside the repository should know what is used to store the game
- call the load/save functions from within the UI

Consider the following signature:

.. code:: python3

    def save(game: DungeonGame) -> None:
        ...

    def load() -> DungeonGame:
        ...

----

The Factory Pattern
===================

Implement a zoom factor so that the game can be played with different resolutions.
The tile bitmaps will be produced by a class implementing the `FactoryMethod <https://sourcemaking.com/design_patterns/factory_method>`__ pattern.
Use the following:

- create a new module `tiles.py`
- create a new class `TileFactory` that takes an integer zoom factor
- only very few zoom factors need to work (1, 2, 4)
- move the `read_images`, `read_image` and `TILE_SIZE` objects to the new module
- edit the line with `np.kron` (a Kronecker product) to zoom the tiles.

To retrieve tiles by a name, implement a `get_tile()` method. Alternatively, use the `__getitem__` magic method:

.. code:: python3

    class TileFactory:

        def __getitem__(self, name: str) -> np.ndarray:
            ...

    tf = TileFactory(zoom=2)
    tile = tf["player"]

.. hint::

    Having the factory opens up more flexible options like adding synonyms for the tiles
    or reading the tile definitions from a file.

----

The Iterator Pattern
====================

Implement a `MonsterManager` class that is reponsible for keeping all opponents in the game.
Use the `Iterator Pattern <https://sourcemaking.com/design_patterns/iterator>`__ to make the class iterable.
One option

In Python, there exists a shortcut using magic methods:

.. code:: python3

    class MonsterManager(BaseModel):

        monsters: list[Monster]

        def __iter__(self):
            """
            resets the iterator.
            has to return something with a next() method
            """
            self.__i = 0
            return self
        
        def __next__(self):
            if self.__i < len(self.monsters):
                self.__i += 1
                return self.monsters[self.__i - 1]
            else:
                raise StopIteration("the end")

    mm = MonsterManager(monsters=["trap", "ghost", "skeleton"])
    for m in mm:
        print(m)
                
Contrast this implementation with an alternative:

.. code:: python3

    class MonsterManager(BaseModel):

        monsters: list[Monster]

        def __iter__(self):
            return iter(self.monsters)

How does the behavior of the two implemenations differ?

----

The Decorator Pattern
=====================

Log the moves of the player in a file using a decorator.
The original `Decorator pattern <https://sourcemaking.com/design_patterns/decorator>`__ can be considered obsolete, but the main idea is useful.
Check the following sources to learn how decorators work:

- `a decorator function <https://www.academis.eu/advanced_python/functions/decorators.html>`__
- `a decorator class <https://www.academis.eu/advanced_python/classes/decorator_class.html>`__
- `the Python logging module <https://www.academis.eu/advanced_python/functions/decorators.html>`__

.. hint::

    Can you also log the moves of the monsters using the same decorator?

.. hint::

    Add other attributes and methods to the `MonsterManager` as you deem necessary.

----

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

----

The Composite Pattern
=====================

Implement a monster consisting of multiple `Monster` objects that occupy multiple tiles in the dungeon
(e.g. a dragon or giant snake).
Use the `Composite Pattern <https://sourcemaking.com/design_patterns/composite>`__.

----

The State Pattern
=================

Implement a `GamePaused` class that has the same interface as the `DungeonGame`.
The UI should have a `state` attribute that is an instance of either class.

Add a pause key that changes the state from the running game to the paused state and back.

.. seealso::

    `The State Pattern <https://sourcemaking.com/design_patterns/state>`__

----

The Adapter Pattern
===================

Write a custom monster that has a different interface than the monsters you already have.
Implement an adapter class that wraps the monster but inherits from your usual Monster class.

Also, write a mapper function that converts the attributes of one class to another.

----

The Builder Pattern
===================

The `Builder Pattern <https://sourcemaking.com/design_patterns/builder>`__ is very common. We will probably find an example for the Builder pattern soon.

----


Async
=====

Discuss pros and cons of distributing the movement of player and monsters to seaparate threads or `async` functions.

