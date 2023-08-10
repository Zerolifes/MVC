# import library
import pygame
from setting import *
from widget import Widget
from calendarManager import CalendarManager



# init pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)


# declare objects
ROOT = Widget(pos=[0, 0], size=WINDOW_SIZE, background=WHITE)
calendarManager = CalendarManager(parent=ROOT, pos=[0, 30], size=[760,550], align=[Align.CENTER, Align.NONE], background=SILVER,boderRadius=10)

# application
running = True
while running:
    # listen user's contacts
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # clear screen
    screen.fill(WHITE)

    # draw objects
    calendarManager.draw(screen)

    # display screen
    pygame.display.flip()

# quit pygame
pygame.quit()