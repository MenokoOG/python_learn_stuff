""" Working with pygame GUI for OOP projects, Menoko OG 4-21-2023"""
# Pygame demo 1- draw one image
# Import packages
import pygame
from pygame.locals import *
import sys

#Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#Iniitialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets: image(s), sounds(s), etc.
ballImage = pygame.image.load("PygameOneImage/images/ball.png")
#Initialize variables

# Loop forever
while True:
    
    #Check for and hanlde events
    for event in pygame.event.get():
        #Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any "per frame" actions

    #Clear the window
    window.fill(BLACK)
    
    #Draw all window elements
    # Draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))
    
    #Update the window
    pygame.display.update()
    
    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  #make pygame wait