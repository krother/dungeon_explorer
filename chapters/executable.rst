
Build an Executable
===================

First you need to install the **pyinstaller** library.
Type into a command line terminal:

.. code::

   pip install pyinstaller

Then switch to your project directory, and run in a terminal:

.. code::

   pyinstaller main.py --add-data tiles:tiles --add-data *.ogg:.
   --add-data .:.

Use absolute paths for images and sounds
----------------------------------------

In order to having correct file paths, you need to add the absolute path to all image and sound files that are not tiles, e.g.:

.. code::

   abs_path = os.path.split(__file__)[0]
   img = cv2.imread(abs_path + "/myshop.png")

instead of

.. code::

   img = cv2.imread("myshop.png")  # will not work in executable
