
Music
=====

Some background music adds a lot of atmosphere to the game.
Including music is not difficult to do.
Look around `opengameart.org <https://opengameart.org/>`__ for freely available music in the MP3 format.
You can also use an AI to generate some.

To play the music from your game, you need the `pygame` library.
Install it from the command line with:

::

    pip install pygame

.. hint::

    On some systems, you may need to check the `PyGame documentation <https://www.pygame.org/docs/>`__ for installation details.

The following code starts the music:

.. code:: python3

    from pygame import mixer
    
    mixer.init()
    mixer.music.load("my_music_filename.mp3)
    mixer.music.play(loops=-1)

At the end of the program, you may want to stop the music:

.. code:: python3

    mixer.music.stop()

That's it. Have fun!
