"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

from src.Player import Player
from src.states.player_states.circle_player_states import (
    IdleRight,
    IdleLeft,
    IdleUp,
    IdleDown,
    WalkRight,
    WalkLeft,
    WalkUp,
    WalkDown,
)

import pygame
import settings

from src.ProjectileFactory import ProjectileFactory


class CirclePlayer(Player):
    def __init__(self, x, y, collision_px_reduction=0):
        self.collision_px_reduction = collision_px_reduction
        super().__init__(
            x,
            y,
            settings.PLAYER_WIDTH,
            settings.PLAYER_HEIGHT,
            "circle_player",
            states={
                "idle-right": lambda sm: IdleRight.IdleRight(self, sm),
                "idle-left": lambda sm: IdleLeft.IdleLeft(self, sm),
                "idle-up": lambda sm: IdleUp.IdleUp(self, sm),
                "idle-down": lambda sm: IdleDown.IdleDown(self, sm),
                "walk-right": lambda sm: WalkRight.WalkRight(self, sm),
                "walk-left": lambda sm: WalkLeft.WalkLeft(self, sm),
                "walk-up": lambda sm: WalkUp.WalkUp(self, sm),
                "walk-down": lambda sm: WalkDown.WalkDown(self, sm),
            },
            animation_defs={
                "idle-right": {"frames": [8], "interval": 0.2},
                "idle-left": {"frames": [4], "interval": 0.2},
                "idle-up": {"frames": [12], "interval": 0.2},
                "idle-down": {"frames": [0], "interval": 0.2},
                "walk-right": {"frames": [8, 9, 10, 11], "interval": 0.2},
                "walk-left": {"frames": [4, 5, 6, 7], "interval": 0.2},
                "walk-up": {"frames": [12, 13, 14, 15], "interval": 0.2},
                "walk-down": {"frames": [0, 1, 2, 3], "interval": 0.2},
            },
        )

    def on_input(self, input_id, input_data) -> None:
        if not self.vulnerable:
            self.state_machine.on_input(input_id, input_data)

    def on_input_throw(self, input_id, input_data, map) -> None:
        if not self.vulnerable:
            if input_id == "circle_throw" and input_data.pressed:
                ProjectileFactory.throw_projectile(map, self)

    def get_collision_rect(self):
        return pygame.Rect(
            self.x + self.collision_px_reduction,
            self.y + self.collision_px_reduction,
            self.width - self.collision_px_reduction,
            self.height - self.collision_px_reduction,
        )

    def circle_throw(self, map):
        ProjectileFactory.throw_projectile


class CirclePortal:
    def __init__(self, x, y):
        self.size = settings.TILE_SIZE
        self.x = x
        self.y = y
        self.texture = settings.TEXTURES["portal"]
        self.frame = settings.FRAMES["portal"][0]

    def render(self, surface):
        surface.blit(self.texture, (self.x, self.y), self.frame)

    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)