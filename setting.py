# import library
from enum import Enum
from pygame import Color

# properties of application
CAPTION = "Medify"


# size of screen

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)


# color

WHITE = "#ffffff"
BLACK = "#000000"
SILVER = "#c0c0c0"

# constant parameter
class Align(Enum):
    NONE = 0
    CENTER = 1

class User(Enum):
    NONE = 0
    MOUSE = 1
    KEYBOARD = 2
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def checkin(point, rect):
    if rect.x <= point.x and point.x <= rect.x + rect.w and rect.y <= point.y and point.y <= rect.y+rect.h:
        return True
    else:
        return False

