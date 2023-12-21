""" Working with pygame GUI for OOP projects, Menoko OG 4-21-2023"""
# Pygame demo 3(a) - image move by keyboard

#  1 Import packages
import pygame
from pygame.locals import *
import sys
import random 

# 2 Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

TARGET_X =400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 100
N_PIXELS_TO_MOVE = 3

# 3 Iniitialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 Load assets: image(s), sounds(s), etc.
ballimage = pygame.image.load("PygameOneImage/images/ball.png")
targetImage = pygame.image.load("PygameOneImage/images/target.jpg")

# 5 Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)


# 6 Loop forever
while True:
    
    # 7 Check for and hanlde events
    for event in pygame.event.get():
        #Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # see if user pressed a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE  
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE
                

    # 8 Do any "per frame" actions
    # Check if the ball is colliding with the target
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print("Ball is touching the target")
    
    # 9 Clear the window
    window.fill(BLACK)
    
    # 10 Draw all window elements
    #Draw the target and the ball
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballimage, (ballX, ballY))
    
    # 11 Update the window
    pygame.display.update()
    
    # 12 Slow things down a bit
    clock.tick(FRAMES_PER_SECOND) # make pygame wait