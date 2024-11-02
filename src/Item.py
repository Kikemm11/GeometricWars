import pygame
import settings


class Item():
    def __init__(self, x, y, width, height, texture, frame):
        self.width = width
        self.height = height
        self.x = x + (settings.TILE_SIZE // 2) - (self.width // 2)
        self.y = y + (settings.TILE_SIZE // 2) - (self.height // 2)
        self.texture = settings.TEXTURES[texture]
        self.frame = settings.FRAMES[frame][0]
        self.taken = False

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y), self.frame)

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)