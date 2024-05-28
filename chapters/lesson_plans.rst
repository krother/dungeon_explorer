
Lesson Plans
============
1.

Warm-up to learn about existing skills about computers and programming. Brief overview of the course and programming methodology.

Participants work through an installation guide to set up their Python environment. They run a prototype program that they will start developing with, displaying a player in a 2D dungeon. The session is concluded by reading the code together.

Key concepts: Python interpreter, editor, instructions, logging

-----

2.

Participants make the player move around in a dungeon using the keyboard.
They complete the existing left/right movement from the prototype using a step-by-step guide. Fast students edit the level in a text editor.

Key concepts: integer, string, nested list, indexing, arithmetics.

-----

3.

Participants make the player stop at walls.
They implement new code using a step-by-step guide. Fast students implement a pit that the player should avoid falling into.

Key concepts: conditional expressions, variable assignments

-----

4.

Participants add their own graphic elements.
They examine, how symbols used during the game are mapped to graphics. It is discussed why an abstraction is necessary. They browse the OpenGameArt website for graphics they want to use and add them to the game.

Key concepts: files, abstraction, dictionary

-----

5.

Participants make the player pick up keys .
They implement an inventory that can contain multiple items using a step-by-step guide. Fast students add more items players can collect.

Key concepts: lists, appending, indexing and removing.

-----

6.

Participants make the player use keys to unlock doors.
When walking into a door, it is checked whether the player has the according key. Fast students add custom graphics to have more types of keys available.

Key concepts: conditional expressions, list ‘in’ operator

-----

7.

Participants create teleporters that transport the player to another location.
They implement a data structure that can be used to look up multiple teleporters and their destinations.
Fast students implement switches that open secret doors or close pits.

Key concepts: dictionary, key, value, tuple

-----

8.
Participants split the growing code into multiple functions.
They use existing automated test code to make sure that the change does not break things. They publish their code before and after the change. Fast students implement their own test code.

Key concepts: function, function argument, return, refactoring, automated test

-----

9.
Participants create dangerous fireballs that move.
They implement a fireball that is spawned in regular intervals and moves along a straight line until it hits a wall. Fast students create fireballs in multiple locations and/or directions.

Key concepts: update cycle, data model, attributes

-----

10.
Participants make the fireballs hurt if they hit a player.
The position of player and fireball is compared regularly and the health of the player decreased on a hit. The code is split into modules. Fast students implement a healing potion.

Key concepts: modules, import

-----

11.
Participants create skeletons that chase the player.
The skeletons follow a random move pattern, making them much more dangerous. Fast students implement an orc with a smarter move pattern and/or create a dragon that spits fireballs.

Key concepts: random module, builtin modules

-----

12.
Participants enable players to defeat monsters.
They implement code to attack adjacent monsters and remove them from the game. They define a helper function that handles the ‘attack’ action. Fast students implement extra melee and/or ranged weapons.

Key concepts: use case, function design, function scope, local vs global variables

-----

13.
Participants create a dungeon with 2+ levels.
They define a level data structure containing a floor plan, items, doors, switches, monsters etc. Stairs move the player to the next level. Fast students create more levels.

Key concepts: state diagram, global vs. local variables

-----
14.
Participants store levels in files.
They implement code that loads levels from a directory with JSON files using a defined format. Levels are uploaded to GitHub, and students are encouraged to include each others’ level designs. Fast students create more levels.

Key concept: file paths, read/write functions, JSON 

-----

15.
Participants create a front page for their software.
They edit the README file to include installation instructions, a screenshot of their game, a license. They also add an in-game title banner.
