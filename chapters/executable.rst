
Build an Executable
===================

First you need to install the **pyinstaller** library.
Type into a command line terminal:

.. code::

   pip install pyinstaller

Then switch to your project directory, and run in a terminal:

.. code::

   pyinstaller main.py --add-data tiles:tiles
   
If you have more files than the tiles you need to add multiple ``--add-data`` instructions, e.g.:

.. code::

   --add-data images:images    # adds the images/ folder
   --add-data *.mp3:.          # adds all .mp3 files from the main folder
   --add-data .:.              # adds everything in the main folder

Use absolute paths for images and sounds
----------------------------------------

In order to having correct file paths, you need to add the absolute path to all image and sound files that are not tiles, e.g.:

.. code::

   abs_path = os.path.split(__file__)[0]
   img = cv2.imread(abs_path + "/myshop.png")

instead of

.. code::

   img = cv2.imread("myshop.png")  # will not work in executable


.. hint::

   On MacOS, you may observe an error resulting from a version conflict between **PyQt5** and **PyQt6**.
   Fix it by adding the following to the **pyinstaller** command:

   .. code::

      --exclude-module=PyQt5

    The full command might look like this:
    
    .. code::

       pyinstaller --exclude-module=PyQt5 main.py --add-data tiles:tiles --add-data *.wav:. --add-data *.mp3:. --add-data *.flac:. --add-data *.png:.

.. hint::

   If you manage to create an executable that runs, it is a good idea to save the exact pyinstaller command to your ``README.md`` file so that you know what to do next time.