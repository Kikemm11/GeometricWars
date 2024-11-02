from typing import TypeVar

from gale.input_handler import InputData

from src.Player import Player
from src.states.player_states.square_player_states import IdleState , WalkRight, WalkLeft, WalkUp, WalkDown

import pygame
import settings

from src.ProjectileFactory import ProjectileFactory


class SquarePlayer(Player):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            x,
            y,
            settings.PLAYER_WIDTH,
            settings.PLAYER_HEIGHT,
            "square_player",
            states={
                "idle": lambda sm: IdleState.IdleState(self, sm),
                "walk-right": lambda sm: WalkRight.WalkRight(self, sm),
                "walk-left": lambda sm: WalkLeft.WalkLeft(self, sm),
                "walk-up": lambda sm: WalkUp.WalkUp(self, sm),
                "walk-down": lambda sm: WalkDown.WalkDown(self, sm),
            },
            animation_defs={
                "idle": {"frames": [7], "interval": 0.2},
                "walk-right": {"frames": [4, 5], "interval": 0.1},
                "walk-left": {"frames": [3, 4], "interval": 0.1},
                "walk-up": {"frames": [0, 1, 2], "interval": 0.1},
                "walk-down": {"frames": [6, 7, 8], "interval": 0.1},
            },
        )


    def on_input(self, input_id: str, input_data: InputData) -> None:
        if not self.vulnerable:
            self.state_machine.on_input(input_id, input_data)


    def on_input_throw(self, input_id, input_data, map) -> None:
        if not self.vulnerable:
            if input_id == "square_throw" and input_data.pressed:
                ProjectileFactory.throw_projectile(map, self)


    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)