"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

import pygame
import settings


class Obstacle():
    def __init__(self, x, y):
        self.width = settings.OBSTACLE_WIDTH
        self.height = settings.OBSTACLE_HEIGHT
        self.x = x + (settings.TILE_SIZE // 2) - (self.width // 2)
        self.y = y + (settings.TILE_SIZE // 2) - (self.height // 2)
        self.texture = settings.TEXTURES["obstacle"]
        self.frame = settings.FRAMES["obstacle"][0]
    

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y), self.frame)

    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)