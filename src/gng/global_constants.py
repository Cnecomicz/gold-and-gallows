import json, pygame

pygame.init()
# TODO: move pygame.init() to main. Reason for delay: without
# pygame.init(), you get pygame.error: font not initialized.


FPS = 60
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720


# TODO: Add global data paths
FONT_SIZE = 20
BASIC_FONT = pygame.font.Font("freesansbold.ttf", FONT_SIZE)
ALCH_FONT = pygame.font.Font("./Fonts/1651_Alchemy.ttf", FONT_SIZE)
BB_FONT = pygame.font.Font("./Fonts/BlackBeard_Regular.otf", FONT_SIZE)


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

BGCOLOR = BLACK
TEXT_COLOR = WHITE

UP = [
    pygame.K_w,
    pygame.K_UP,
]
DOWN = [
    pygame.K_s,
    pygame.K_DOWN,
]
LEFT = [
    pygame.K_a,
    pygame.K_LEFT,
]
RIGHT = [
    pygame.K_d,
    pygame.K_RIGHT,
]
USE = [
    pygame.K_e,
    pygame.K_z,
]
DEBUG = [
    pygame.K_BACKQUOTE,
]
PAUSE = [
    pygame.K_ESCAPE,
]


AVERAGE_HP_PER_HD = 4.5

with open("JSON/monster_statistics_by_hit_dice.json", "r") as file:
    MONSTER_HP_AND_DAMAGE_LIST_OF_DICT = json.load(file)
