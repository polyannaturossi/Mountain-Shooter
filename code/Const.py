# C
import pygame

C_BLUE = (2, 50, 112)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 242, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMAGE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'level1bg6': 0,
    'level1bg7': 0,
    'level2bg0': 0,
    'level2bg1': 0,
    'level2bg2': 0,
    'Player1': 1,
    'Player1shot': 25,
    'Player2': 1,
    'Player2shot': 20,
    'Enemy1': 1,
    'Enemy1shot': 20,
    'Enemy2': 1,
    'Enemy2shot': 15,
}

ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'level1bg4': 999,
    'level1bg5': 999,
    'level1bg6': 999,
    'level1bg7': 999,
    'level2bg0': 999,
    'level2bg1': 999,
    'level2bg2': 999,
    'Player1': 300,
    'Player1shot': 1,
    'Player2': 300,
    'Player2shot': 1,
    'Enemy1': 50,
    'Enemy1shot': 1,
    'Enemy2': 60,
    'Enemy2shot': 1,
}

ENTITY_SCORE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'level1bg6': 0,
    'level1bg7': 0,
    'level2bg0': 0,
    'level2bg1': 0,
    'level2bg2': 0,
    'Player1': 0,
    'Player1shot': 0,
    'Player2': 0,
    'Player2shot': 0,
    'Enemy1': 100,
    'Enemy1shot': 0,
    'Enemy2': 125,
    'Enemy2shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 30,
    'Enemy1': 150,
    'Enemy2': 100,
}

ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level1bg4': 4,
    'level1bg5': 5,
    'level1bg6': 6,
    'level1bg7': 7,
    'level2bg0': 0,
    'level2bg1': 1,
    'level2bg2': 2,
    'Player1': 4,
    'Player1shot': 6,
    'Player2': 4,
    'Player2shot': 5,
    'Enemy1': 1,
    'Enemy1shot': 5,
    'Enemy2': 1,
    'Enemy2shot': 4,
}

EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 2000

# T
TIMEOUT_LEVEL = 20000  # 20 seconds

TIMEOUT_STEP = 100 # 10 ms

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
