import pathlib

import pygame

from gale import frames
from gale import input_handler

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_UP, "move_up")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_DOWN, "move_down")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_w, "move_up_2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_s, "move_down_2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left_2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right_2")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_f, "circle_throw")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RCTRL, "square_throw")

# War time
GAME_TIMER_DURATION_SECONDS = 99


# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 200

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4 - 300
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4 - 70

BASE_DIR = pathlib.Path(__file__).parent

# Tile size

TILE_SIZE = 20

TILE_CORNER = 0
TILE_SIDE = 1
TILE_FLOOR = [3, 4, 5, 6, 7, 8, 9]


# Obstacle size

OBSTACLE_WIDTH = 9
OBSTACLE_HEIGHT = 12

# Projectile info

PROJECTILE_SIZE = 12
PROJECTILE_VELOCITY = 50

# Number of obstacles

OBSTACLES = 45

# Items info

CIRCLE_ITEM_SIZE = 8
SQUARE_ITEM_WIDTH = 8
SQUARE_ITEM_HEIGHT = 10
ITEMS = 10


# Map size

MAP_WIDTH = VIRTUAL_WIDTH // TILE_SIZE
MAP_HEIGHT = VIRTUAL_HEIGHT // TILE_SIZE


# Player Info

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 23
PLAYER_VX = 40
PLAYER_VY = 40
PLAYER_VULNERABLE_TIME = 3


TEXTURES = {
    "background": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "background.png"
    ),
    "circle_player": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "circle_player.png"
    ),
    "square_player": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "square_player.png"
    ),
    "tilesheet": pygame.image.load(BASE_DIR / "assets" / "textures" / "tilesheet.png"),
    "obstacle": pygame.image.load(BASE_DIR / "assets" / "textures" / "obstacle.png"),
    "projectile": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "projectile.png"
    ),
    "circle_item": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "circle_item.png"
    ),
    "square_item": pygame.image.load(
        BASE_DIR / "assets" / "textures" / "square_item.png"
    ),
    "portal": pygame.image.load(BASE_DIR / "assets" / "textures" / "portal.png"),
}

FRAMES = {
    "circle_player": frames.generate_frames(
        TEXTURES["circle_player"], PLAYER_WIDTH, PLAYER_HEIGHT
    ),
    "square_player": frames.generate_frames(
        TEXTURES["square_player"], PLAYER_WIDTH, PLAYER_HEIGHT
    ),
    "tilesheet": frames.generate_frames(TEXTURES["tilesheet"], TILE_SIZE, TILE_SIZE),
    "obstacle": frames.generate_frames(
        TEXTURES["obstacle"], OBSTACLE_WIDTH, OBSTACLE_HEIGHT
    ),
    "projectile": frames.generate_frames(
        TEXTURES["projectile"], PROJECTILE_SIZE, PROJECTILE_SIZE
    ),
    "circle_item": frames.generate_frames(
        TEXTURES["circle_item"], CIRCLE_ITEM_SIZE, CIRCLE_ITEM_SIZE
    ),
    "square_item": frames.generate_frames(
        TEXTURES["square_item"], SQUARE_ITEM_WIDTH, SQUARE_ITEM_HEIGHT
    ),
    "portal": frames.generate_frames(TEXTURES["portal"], TILE_SIZE, TILE_SIZE),
}

pygame.mixer.init()

SOUNDS = {
    "hit": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "hit.wav"),
    "item": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "item.wav"),
    "hurt": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "hurt.wav"),
}

pygame.font.init()

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 16),
    "large": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 24),
}
