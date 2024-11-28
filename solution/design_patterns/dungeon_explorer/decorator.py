
from typing import Callable

class FailureCounter:

    def __init__(self, message):
        self.message: str = message
        self.function: Callable = None
        self.failcount: int = 0

    def __call__(self, func):  # called when we write @ once when defining a function
        """now we are decorating the function (replace it by our own)"""
        self.function = func
        return self.safe_call

    def safe_call(self, *args):
        try:
            self.function(*args)
        except IOError:
            self.failcount += 1
            print(self.message)
            print(f'An I/O error was caught in {self.function.__name__}')
            print(f"with the file name '{args[0]}'")
            print(f'this is failure #{self.failcount}\n')


@FailureCounter('--- FILE ERROR ---')
def risky_fileopen(filename):
    open(filename)

print(risky_fileopen)

risky_fileopen('not_existing_file')
risky_fileopen('doesnotexist_either')