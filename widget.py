# import library
import pygame
from setting import *

class Widget:

    def __init__(self, parent = 'none', name ="", pos = [0, 0], size = [0, 0], align = [Align.NONE, Align.NONE], background = "none", boderRadius = 0, hover="none", display = Display.SHOW):
        self.parent = parent
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.absx = pos[0]
        self.absy = pos[1]
        self.w = size[0]
        self.h = size[1]
        self.display = display
        self.rect = [self.x, self.y, self.w, self.h]
        self.align = align
        if background != "none": self.background = background
        else: self.background = self.parent.inherit
        self.inherit = self.background
        if hover != "none": self.hover = hover
        else: self.hover = self.background
        self.boderRadius = boderRadius
        self.views = []

    def update(self):
        # update rect
        self.x = self.parent.x + self.absx
        self.y = self.parent.y + self.absy
        if self.align[0] == Align.CENTER:
            self.x = self.parent.x + (self.parent.w - self.w) // 2
        if self.align[1] == Align.CENTER:
            self.y = self.parent.y + (self.parent.h - self.h) // 2
        self.rect = [self.x, self.y, self.w, self.h]

    def draw(self, surface):
        if self.display == Display.HIDE: return
        self.update()
        x, y = pygame.mouse.get_pos()
        if checkin(Point(x,y), self):
            pygame.draw.rect(surface, self.hover, self.rect, border_radius=self.boderRadius)
            self.inherit = self.hover
        else:
            pygame.draw.rect(surface, self.background, self.rect, border_radius=self.boderRadius)
            self.inherit = self.background
        for view in self.views:
            view.draw(surface)


    def changeView(self, name, object):
        if self.name != name:
            for view in self.views:
                view.changeView(name, object)
        self = object

