import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text

import settings
from src.Player import Player
from src.CirclePlayer import CirclePlayer
from src.SquarePlayer import SquarePlayer


class StartState(BaseState):

    def enter(self) -> None:
        self.title = Text(
            "Geometric Wars",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH,
            settings.VIRTUAL_HEIGHT // 4,
            (197, 195, 198),
            shadowed=True,
        )

        self.selected = 1

        self.circle_player = CirclePlayer(1, settings.VIRTUAL_HEIGHT - 50)
        self.circle_player.change_state("walk-right")

        self.square_player = SquarePlayer(
            settings.VIRTUAL_WIDTH - settings.PLAYER_WIDTH - 1,
            settings.VIRTUAL_HEIGHT - 50,
        )
        self.square_player.change_state("walk-left")

    def exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        self.circle_player.update(dt)
        self.square_player.update(dt)

        self.erratic_players(self.circle_player, self.square_player)

    def render(self, surface: pygame.Surface) -> None:

        surface.blit(settings.TEXTURES["background"], (0, 0))

        render_text(
            surface,
            "Geometric Wars",
            settings.FONTS["large"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 4,
            (255, 255, 255),
            center=True,
        )

        color = (81, 15, 160) if self.selected == 1 else (255, 255, 255)

        render_text(
            surface,
            "Play Game",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 100,
            color,
            center=True,
        )

        color = (81, 15, 160) if self.selected == 2 else (255, 255, 255)

        render_text(
            surface,
            "Instructions",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 70,
            color,
            center=True,
        )

        self.circle_player.render(surface)
        self.square_player.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_down" and input_data.pressed:
            self.selected = 2 if self.selected == 1 else 1

        elif input_id == "move_up" and input_data.pressed:
            self.selected = 1 if self.selected == 2 else 2

        elif input_id == "enter" and input_data.pressed:

            if self.selected == 1:
                self.state_machine.change("playstate")
            else:
                self.state_machine.change("instructions")

    def erratic_players(self, circle_player: Player, square_player: Player):

        if (
            circle_player.vx > 0
            and circle_player.x + circle_player.width >= settings.VIRTUAL_WIDTH // 2
        ):
            circle_player.change_state("walk-left")

        if circle_player.vx < 0 and circle_player.x <= 0:
            circle_player.change_state("walk-right")

        if (
            square_player.vx > 0
            and square_player.x + square_player.width >= settings.VIRTUAL_WIDTH
        ):
            square_player.change_state("walk-left")

        if square_player.vx < 0 and square_player.x <= settings.VIRTUAL_WIDTH // 2:
            square_player.change_state("walk-right")
