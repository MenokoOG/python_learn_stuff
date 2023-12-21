"""Building a SimpleButton Class project, Uses a "state machine approach, Menoko OG 4-22-2023"""
# SimpleButton class

import pygame
from pygame.locals import *

class SimpleButton():
    # Used to track the state of the button
    STATE_IDLE = "idle" # button is up, mouse not over button
    STATE_ARMED = "armed" #button is down, mouse over button
    STATE_DISARMED = "disarmed" # clicked down on button, rolled off
    