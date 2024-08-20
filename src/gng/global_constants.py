import pygame
from pygame.locals import *

pygame.init()


FPS = 60
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

FONT_SIZE = 20
BASIC_FONT = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
ALCH_FONT = pygame.font.Font("Fonts/1651_Alchemy.ttf", FONT_SIZE)
BB_FONT = pygame.font.Font("Fonts/BlackBeard_Regular.otf", FONT_SIZE)


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

BGCOLOR = BLACK
TEXT_COLOR = WHITE

UP = [K_w, K_UP]
DOWN = [K_s, K_DOWN]
LEFT = [K_a, K_LEFT]
RIGHT = [K_d, K_RIGHT]
USE = [K_e, K_z]

AVERAGE_HP_PER_HD = 4.5
