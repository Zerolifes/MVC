# import libraby
import pygame
from setting import *
from widget import Widget

class Textview(Widget):
    def __init__(self, parent, name = "", color = BLACK, fontSize = 14, text = "", wrap = True, hover = "none"):
        super().__init__(parent=parent, name=name, align=[Align.CENTER, Align.CENTER], hover=hover)
        self.color = color
        self.fontSize = fontSize
        self.font = pygame.font.SysFont("Arial", self.fontSize)
        self.text = text
        self.wrap = wrap
        self.content = self.font.render(self.text, True, self.color, self.parent.inherit)
        self.update()
    def update(self):
        self.w = self.content.get_width()
        self.h = self.content.get_height()
        if (self.wrap):
            self.parent.w = self.w
            self.parent.h = self.h
        self.x = self.parent.x + (self.parent.w - self.w) // 2
        self.y = self.parent.y + (self.parent.h - self.h) // 2
        self.rect = [self.x, self.y, self.w, self.h]
        self.font = pygame.font.SysFont("Arial", self.fontSize)
        self.content = self.font.render(self.text, True, self.color, self.parent.inherit)

    def draw(self, surface):
        self.update()
        surface.blit(self.content, self.rect)