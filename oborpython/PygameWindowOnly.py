""" Working wiht pygame GUI for OOP projects, Menoko OG 4-21-2023"""
# Pygame demo 0 - Window Only
#  1 Import packages
import pygame
from pygame.locals import *
import sys

# 2 Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 Iniitialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 Load assets: image(s), sounds(s), etc.

# 5 Initialize variables

# 6 Loop forever
while True:
    
    # 7 Check for and hanlde events
    for event in pygame.event.get():
        #Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 Do any "per frame" actions

    # 9 Clear the window
    window.fill(BLACK)
    
    # 10 Draw all window elements
    
    # 11 Update the window
    pygame.display.update()
    
    # 12 Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)