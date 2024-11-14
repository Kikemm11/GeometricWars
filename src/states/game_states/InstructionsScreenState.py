import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text


pygame.mixer.init()

import settings


class InstructionsState(BaseState):
    def enter(self, text_color=pygame.Color(255, 255, 255)) -> None:
        self.text_color = text_color
        pygame.mixer.music.load(r"assets\music\menu.mp3")
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def render(self, surface: pygame.Surface) -> None:

        surface.blit(settings.TEXTURES["background"], (0, 0))

        render_text(
            surface,
            f"Instructions",
            color=self.text_color,
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=(settings.VIRTUAL_HEIGHT // 4) - 10,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"Objective: Collect 10 materials of your color",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=(settings.VIRTUAL_HEIGHT // 2) - 35,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"to win or have the most when time is up!",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=(settings.VIRTUAL_HEIGHT // 2) - 25,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"MOVE WASD",
            color=pygame.Color(244, 64, 94),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) + 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 20,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"MOVE Arrows",
            color=pygame.Color(64, 209, 244),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) - 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 20,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"SHOOT F",
            color=pygame.Color(244, 64, 94),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) + 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 40,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"SHOOT RCTRL",
            color=pygame.Color(64, 209, 244),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) - 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 40,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"(Any key to go to Menu)",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=settings.VIRTUAL_HEIGHT - 20,
            center=True,
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_data.pressed:
            self.state_machine.change("start")

    def exit(self) -> None:
        pygame.mixer.music.stop()
        pass
