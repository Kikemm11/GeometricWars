"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

import pygame
from gale.state import StateMachine, BaseState

from src import mixins
import settings


class Player(mixins.DrawableMixin, mixins.AnimatedMixin, mixins.CollidableMixin):
    def __init__(self, x, y, width, height, texture_id, states, animation_defs, zoom_scale = 0.8):
        self.x = x
        self.y = y
        self.width = width * zoom_scale
        self.height = height * zoom_scale
        self.vx: float = 0
        self.vy: float = 0
        self.texture_id = texture_id
        self.frame_index = -1
        self.state_machine = StateMachine(states)
        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
        self.vulnerable = False
        self.vulnerable_timer = 0
        self.flash_timer = 0
        self.item = None
        self.shape_counter = 0
        self.zoom_scale = zoom_scale

    def change_state(self, state_id, *args, **kwargs):
        self.state_machine.change(state_id, *args, **kwargs)

    def update(self, dt):

        self.state_machine.update(dt)
        mixins.AnimatedMixin.update(self, dt)

        if self.vulnerable:
            self.flash_timer += dt
            self.vulnerable_timer += dt

        if self.vulnerable_timer > settings.PLAYER_VULNERABLE_TIME:
            self.vulnerable = False
            self.vulnerable_timer = 0
            self.flash_timer = 0

        next_y = self.y + self.vy * dt
        next_x = self.x + self.vx * dt

        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)

        if self.vy < 0:
            self.y = max(0, next_y)
        else:
            self.y = min(settings.VIRTUAL_HEIGHT - self.height, next_y)

    def render(self, surface):
        if not self.vulnerable:
            super().render(surface, zoom_scale=self.zoom_scale)

        if self.vulnerable and self.flash_timer > 0.06:
            super().render(surface, zoom_scale=self.zoom_scale)
            self.flash_timer = 0

    def solve_world_collide(self):

        if self.vx > 0:
            self.x -= 0.5
            self.vx = 0
        elif self.vx < 0:
            self.x += 0.5
            self.vx = 0
        elif self.vy > 0:
            self.y -= 0.5
            self.vy = 0
        elif self.vy < 0:
            self.y += 0.5
            self.vy = 0

    def go_vulnerable(self):
        self.vulnerable = True
        self.vx = 0
        self.vy = 0