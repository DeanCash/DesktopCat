import sys
import pygame
import win32gui
from typing import Callable

from Constants import WINDOW_TITLE

# When the program is built into an exe, and lets say it crashes, it's hard to find out why it
# actually crashed, so I wrote a small 'ErrorHandler' (best name I have for it now) class that
# pretty much encapsulates the main function, so whenever the program does crash, the user will
# get MessageBox/popup on their screen with the error.
# 
# The way of doing this might change in the future, but I like it like this
class ErrorHandler:
    def __init__(self, function: Callable) -> None:
        self.__function = function

    def __call__(self) -> None:
        try:
            self.__function()
        except Exception as e:
            OK = 0
            pygame.quit()
            _ = win32gui.MessageBox(None, f"{WINDOW_TITLE} unexpectedly crashed\n\nERROR: {e}", "Unexpected Crash", OK)
            sys.exit(1)
