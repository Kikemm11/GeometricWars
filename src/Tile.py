import pygame
import settings


class Tile():
    def __init__(self, x, y, frame):
        self.size = settings.TILE_SIZE
        self.x = x * self.size
        self.y = y * self.size
        self.texture = settings.TEXTURES["tilesheet"]
        self.frame = settings.FRAMES["tilesheet"][frame]

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y), self.frame)

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.size, self.size)