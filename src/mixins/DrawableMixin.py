"""
Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the AnimatedMixin.
"""

import pygame
import settings

class DrawableMixin:
    def render(self, surface, zoom_scale=1):
        texture = settings.TEXTURES[self.texture_id]
        frame = settings.FRAMES[self.texture_id][self.frame_index]
        image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        image.fill((0, 0, 0, 0))
        image.blit(texture, (0, 0), frame)
        image = pygame.transform.scale_by(image, zoom_scale)

        surface.blit(image, (self.x, self.y))
