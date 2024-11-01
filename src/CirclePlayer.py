from typing import TypeVar

from gale.input_handler import InputData

from src.Player import Player
from src.states.player_states.circle_player_states import IdleState , WalkRight, WalkLeft, WalkUp, WalkDown

import pygame
import settings


class CirclePlayer(Player):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            x,
            y,
            settings.PLAYER_WIDTH,
            settings.PLAYER_HEIGHT,
            "circle_player",
            states={
                "idle": lambda sm: IdleState.IdleState(self, sm),
                "walk-right": lambda sm: WalkRight.WalkRight(self, sm),
                "walk-left": lambda sm: WalkLeft.WalkLeft(self, sm),
                "walk-up": lambda sm: WalkUp.WalkUp(self, sm),
                "walk-down": lambda sm: WalkDown.WalkDown(self, sm),
            },
            animation_defs={
                "idle": {"frames": [0,2], "interval": 0.2},
                "walk-right": {"frames": [8, 9, 10, 11], "interval": 0.2},
                "walk-left": {"frames": [4, 5, 6, 7], "interval": 0.2},
                "walk-up": {"frames": [12, 13, 14, 15], "interval": 0.2},
                "walk-down": {"frames": [0, 1, 2, 3], "interval": 0.2},
            },
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.state_machine.on_input(input_id, input_data)

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)