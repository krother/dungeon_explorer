Write a Video
=============

By adding a few  lines, you can record an in-game video.

First, add as the last line in the `draw()` function in `main.py`:

.. code:: python3

    return frame

Second, add in `main.py` before the `while` loop:

.. code:: python3

    fourcc = cv2.VideoWriter_fourcc(*"MP4V")
    out = cv2.VideoWriter("myvideo.mp4", fourcc,
                          60.0,   # frames per second
                          (SCREEN_SIZE_X,SCREEN_SIZE_Y)
                         )

Finally, replace the call to `draw()` inside the while loop with:

.. code:: python3

    frame = draw(game, images)
    out.write(frame)

Run the code and see if a video gets written.
