# import libraby
import pygame
from setting import *
from widget import Widget

class Textview(Widget):
    def __init__(self, parent, name = "", color = BLACK, pos = [0, 0], fontSize = 14, text = "", wrap = True, hover = "none", align=[Align.CENTER, Align.CENTER], display = Display.SHOW):
        super().__init__(parent=parent, name=name, align=align, hover=hover, display=display, pos=pos)
        self.color = color
        self.fontSize = fontSize
        self.font = pygame.font.SysFont("Arial", self.fontSize)
        self.text = text
        self.wrap = wrap
        self.content = self.font.render(self.text, True, self.color, self.parent.inherit)
        self.w = self.content.get_width()
        self.h = self.content.get_height()
        if (self.wrap):
            self.parent.w = self.w
            self.parent.h = self.h

    def update(self):
        self.font = pygame.font.SysFont("Arial", self.fontSize)
        self.content = self.font.render(self.text, True, self.color, self.parent.inherit)
        self.w = self.content.get_width()
        self.h = self.content.get_height()
        if (self.wrap):
            self.parent.w = self.w
            self.parent.h = self.h
        super().update()

    def draw(self, surface):
        self.update()
        surface.blit(self.content, self.rect)