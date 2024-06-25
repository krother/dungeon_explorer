The Prototype
=============

.. topic:: Goal

   Execute a Python program that 
   draws 2D graphics and processes keyboard input.

To get your programming efforts off the ground quickly,
you will start with a minimalistic dungeon game.
In the game you move a graphical icon using the keyboard.
The prototype helps us to get rid of installation issues right away.

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
Unzip the tile images and place the folder ``tiles/`` next to the Python files (without an extra subfolder).

Install Dependencies
--------------------

You need to install several libraries.
Open a terminal (on Windows, use the **Anaconda Prompt**).
Go to the folder containing the files with:

::

   cd my_project_folder/

and type:

::

   pip install -r requirements.txt
   
Execute the prototype
---------------------

Use the same terminal as before. Run the game with:

::

   python main.py

You should see a screen where you can move a character with the keys **A and D**:

.. image:: ../images/prototype.png

Open an editor
--------------

To work with the code, you will need a **Text editor**.
Anaconda comes with **Spyder**, a beginner-friendly editor for Python code.
Start it through the **Anaconda Navigator**. 

**VSCode** is another great editor.
**PyCharm** is also great, but can be overwhelming for a first-time programmer.

.. warning::

   Do not use Windows Notepad for editing code under any circumstances.
   It does not have syntax highlighting or any other useful features and will mess up special characters.

Review the code
---------------

Opn the file ``game.py``. Inspect the code. Take notes about:

* code that you understand
* code that you do not understand
* questions that you have

Complete the movement
---------------------

So far, the character can only move left and right.
Add code that moves the character up and down.

Run the program and make sure it works.
