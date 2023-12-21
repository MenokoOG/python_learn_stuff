"""Pygame demo using the Ball class, bounce many balls, Menoko OG 4-22-2023"""
# 1 - import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import * # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 7

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: images, sound, etc.

# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall) # append the new Ball to the list of Balls

# 6 - Loop forever
while True:
    
    # 7 - Check for and hanlde events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update() # tell the Ball to update itself
    
    # 9 - Clear the window before drawing agian
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()   # tell the ball to draw itself
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)