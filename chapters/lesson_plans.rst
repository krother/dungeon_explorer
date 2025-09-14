
Lesson Goals for Teachers 
=========================

In this chapters, I put down some notes about the lessons where I used the DungeonExplorer game.
I wrote them mostly for myself, but you might find them useful as well.
    

Session 1: Installation Party
-----------------------------

* Activity so that participants get to know each other
* Warm-up to learn about existing skills about computers and programming.
* Brief overview of the course and programming methodology.

**Goal:** Participants work through an installation guide to set up their Python environment. They run a prototype program that they will start developing with, displaying a player in a 2D dungeon. The session is concluded by reading the code together.

**Key concepts:** Python interpreter, editor, instructions, logging

Session 2: Moving around
------------------------

**Goal:** Participants make the player move around in a dungeon using the keyboard.
They complete the existing left/right movement from the prototype using a step-by-step guide. Fast students edit the level in a text editor.

**Key concepts:** integer, string, nested list, indexing, arithmetics.

Session 3: Walls
----------------

**Goal:** Participants make the player stop at walls.
They implement new code using a step-by-step guide. Fast students implement a pit that the player should avoid falling into.

**Key concepts:** conditional expressions, variable assignments

Session 4: Custom tiles
-----------------------

**Goal:** Participants add their own graphic elements.
They examine, how symbols used during the game are mapped to graphics. It is discussed why an abstraction is necessary. They browse the OpenGameArt website for graphics they want to use and add them to the game.

**Key concepts:** files, abstraction, dictionary

Session 5: Inventory
--------------------

**Goal:** Participants make the player pick up keys .
They implement an inventory that can contain multiple items using a step-by-step guide. Fast students add more items players can collect.

**Key concepts:** lists, appending, indexing and removing.

Session 6: Doors
----------------

**Goal:** Participants make the player use keys to unlock doors.
When walking into a door, it is checked whether the player has the according key. Fast students add custom graphics to have more types of keys available.

**Key concepts:** conditional expressions, list ``in`` operator

Session 7: Teleporters
----------------------

**Goal:** Participants create teleporters that transport the player to another location.
They implement a data structure that can be used to look up multiple teleporters and their destinations.
Fast students implement switches that open secret doors or close pits.

**Key concepts:** dictionary, key, value, tuple

Session 8: Functions
--------------------

**Goal:** Participants split the growing code into multiple functions.
They use existing automated test code to make sure that the change does not break things. They publish their code before and after the change. Fast students implement their own test code.

**Key concepts:** function, function argument, return, refactoring, automated test

Session 9: Fireballs
--------------------

**Goal:** Participants create dangerous fireballs that move.
They implement a fireball that is spawned in regular intervals and moves along a straight line until it hits a wall. Fast students create fireballs in multiple locations and/or directions.

**Key concepts:** update cycle, data model, attributes

Session 10: Damage
------------------

**Goal:** Participants make the fireballs hurt if they hit a player.
The position of player and fireball is compared regularly and the health of the player decreased on a hit. The code is split into modules. Fast students implement a healing potion.

**Key concepts:** modules, import

Session 11: Skeletons
---------------------

**Goal:** Participants create skeletons that chase the player.
The skeletons follow a random move pattern, making them much more dangerous. Fast students implement an orc with a smarter move pattern and/or create a dragon that spits fireballs.

**Key concepts:** random module, builtin modules

Session 12: More monsters
-------------------------

**Goal:** Participants enable players to defeat monsters.
They implement code to attack adjacent monsters and remove them from the game. They define a helper function that handles the *attack* action. Fast students implement extra melee and/or ranged weapons.

**Key concepts:** use case, function design, function scope, local vs global variables

Session 13: More levels
-----------------------

**Goal:** Participants create a dungeon with 2+ levels.
They define a level data structure containing a floor plan, items, doors, switches, monsters etc. Stairs move the player to the next level. Fast students create more levels.

**Key concepts:** state diagram, global vs. local variables

Session 14: Titles
------------------

**Goal:** Participants create a title screen for the game that disappears when a key is pressed.

**Key concepts:** modules, music with pygame.

Session 15: Presentation
------------------------
**Goal:** Participants record a video of their game for the final presentation.
They present the program and highlights from teh code to eacdh other and celebrate the success.
