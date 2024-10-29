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

# Size we want to emulate
VIRTUAL_WIDTH = 400
VIRTUAL_HEIGHT = 192

# Size of our actual window
WINDOW_WIDTH = VIRTUAL_WIDTH * 4 - 300
WINDOW_HEIGHT = VIRTUAL_HEIGHT * 4 - 70

BASE_DIR = pathlib.Path(__file__).parent

# Circle player size

CIRCLE_PLAYER_WIDTH = 37
CIRCLE_PLAYER_HEIGHT = 35
CIRCLE_PLAYER_VX = 30
CIRCLE_PLAYER_VY = 30

# Square player size

SQUARE_PLAYER_WIDTH = 39
SQUARE_PLAYER_HEIGHT = 46
SQUARE_PLAYER_VX = 30
SQUARE_PLAYER_VY = 30

TEXTURES = {
    "background": pygame.image.load(BASE_DIR / "assets" / "textures" / "background.png"),
    "circle_player": pygame.image.load(BASE_DIR / "assets" / "textures" / "circle_player.png"),
    "square_player": pygame.image.load(BASE_DIR / "assets" / "textures" / "square_player.png"),
}

FRAMES = {
    "circle_player": frames.generate_frames(TEXTURES["circle_player"], CIRCLE_PLAYER_WIDTH, CIRCLE_PLAYER_HEIGHT),
    "square_player": frames.generate_frames(TEXTURES["square_player"], SQUARE_PLAYER_WIDTH, SQUARE_PLAYER_HEIGHT),
}

pygame.mixer.init()

SOUNDS = {
}

pygame.font.init()

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 16),
    "large": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "font.ttf", 24),
}