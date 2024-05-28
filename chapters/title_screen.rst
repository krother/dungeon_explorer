Title Screen
============

At the beginning of the game, there should be a title screen before the actual game begins.
The title screen should have the following:

- a big image in the center
- a text below the image
- music playing in the background
- when the player presses a key, the title screen disappears and the game starts

You can use the image :download:`title.png <../images/title.png>`:

.. code:: python3

    img = cv2.imread("images/title.png")

For the text, you may want to create some empty space at the bottom of the image before you write into it:

.. code:: python3

    img[-100:] = 0  # last 100 pixel rows are black
    img = cv2.putText(
        img,
        "Hello World,
        org=(15, 490),  # x/y position of the text
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(255, 255, 255),  # white
        thickness=2,
    )


Finally, display everything on the screen:

.. code:: python3

    cv2.imshow("Cutscene", img)

See the previous chapter for including music.

Waiting for a key is easy if you do not want to do anything with the key:

.. code:: python3

    cv2.waitKey(0)

At the end, to not forget to clean up everything:

.. code:: python3

    cv2.destroyAllWindows()
    mixer.music.stop()

.. hint::

    Once the `cutscene()` function works, you may want to add different end screens both for the successful and unsuccessful ending.
