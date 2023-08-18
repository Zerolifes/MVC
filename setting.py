# import library
from enum import Enum
import tkinter as tk
import pygame

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
GRAY = "#a0a0a0"

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

DATES = {
    'Sunday' : 1,
    'Monday' : 2,
    'Tuesday' : 3,
    'Wednesday' : 4,
    'Thursday' : 5,
    'Friday' : 6,
    'Saturday' : 7
}
MONTHS = {
    'Jan' : 31,
    'Feb' : 28,
    'Mar' : 31,
    'Apr' : 30,
    'May' : 31,
    'Jun' : 30,
    'Jul' : 31,
    'Aug' : 31,
    'Sep' : 30,
    'Oct' : 31,
    'Nov' : 30,
    'Dec' : 31
}

class Display(Enum):
    HIDE = 0
    SHOW = 1

# global function
def checkin(point, rect):
    if rect.x <= point.x and point.x <= rect.x + rect.w and rect.y <= point.y and point.y <= rect.y+rect.h:
        return True
    else:
        return False



