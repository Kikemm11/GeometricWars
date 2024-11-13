import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text

import settings


class GameEndState(BaseState):
    def enter(self, winning_player_msg: str, text_color: pygame.Color) -> None:
        self.winning_player_msg = winning_player_msg
        self.text_color = text_color

    def render(self, surface: pygame.Surface) -> None:
        render_text(
            surface,
            f"GAME OVER!  {self.winning_player_msg}",
            color=self.text_color,
            font=settings.FONTS["large"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=settings.VIRTUAL_HEIGHT // 2,
            center=True,
            shadowed=True,
        )
        render_text(
            surface,
            f"(Any key to go to Menu)",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["large"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=settings.VIRTUAL_HEIGHT - settings.VIRTUAL_HEIGHT // 3,
            center=True,
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_data.pressed:
            self.state_machine.change("start")
