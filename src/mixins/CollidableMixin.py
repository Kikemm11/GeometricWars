"""
Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the AnimatedMixin.
"""

import pygame

class CollidableMixin:
    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, another):
        return self.get_collision_rect().colliderect(another.get_collision_rect())