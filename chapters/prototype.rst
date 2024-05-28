The Prototype
=============

To get your programming efforts off the ground quickly,
you will start with a working version of the Dungeon Explorer game.
In the game you move a graphical icon using the keyboard.
The goal of this prototype is to prove that you can execute the code, 
process keyboard input and draw 2D graphics.

The prototype helps us to get rid of installation imssues right away.

To get it running, you need to work through a couple of steps:

1. install Python
2. download the code
3. install Dependencies
4. execute the prototype

Install Python
--------------

There are many distributions of Python.
Most of them will work for this project.

For beginners, I recommend the `Anaconda Distribution <https://www.anaconda.com/download>`__


Download the code
-----------------

You will need a couple of files to run the prototype:

- :download:`main.py <../prototype/main.py>` : the graphical interface for the game
- :download:`game.py <../prototype/game.py>` : the game mechanics
- :download:`requirements.txt <../prototype/requirements.txt>` : a list of libraries
- :download:`tile_images.zip <../prototype/tile_images.zip>` : the graphics

Download all files and place them in the same folder.
Unzip the tile images and place the folder `tiles/` next to the Python files (without an extra subfolder).

Install Dependencies
--------------------

You need to install several libraries.
Open a terminal (on Windows the **Anaconda Prompt**).
Go to the folder containing the files with:

::

   cd name/of/folder/

and type:

::

   pip install -r requirements.txt
   
Execute the prototype
---------------------

Use the same prompt as beforeChange to the directory with the ``.py`` files and run the game:

::

   python main.py

You should see a screen where you can move a character with the keys **A and D**:

.. image:: ../images/prototype.png
