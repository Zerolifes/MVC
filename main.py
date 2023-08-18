# import library
import pygame
from setting import *
from widget import Widget
from calendarManager import CalendarManager

# init pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(CAPTION)


# declare objects
ROOT = Widget(pos=[0, 0], size=WINDOW_SIZE, background=WHITE)
calendarManager = CalendarManager(parent=ROOT, pos=[0, 30], size=[760,550], align=[Align.CENTER, Align.NONE], background=SILVER,boderRadius=10)

# application
running = True
while running:

    # user contact
    userContact = User.NONE
    infor = "none"

    # listen user's contacts
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            userContact = User.MOUSE
            x, y = pygame.mouse.get_pos()
            infor = Point(x, y)
        elif event.type == pygame.KEYDOWN:
            userContact = User.KEYBOARD
            infor = event.key

    # clear screen
    screen.fill(WHITE)

    # draw objects
    calendarManager.draw(screen, userContact=userContact, infor=infor)

    # display screen
    pygame.display.flip()

# quit pygame
pygame.quit()