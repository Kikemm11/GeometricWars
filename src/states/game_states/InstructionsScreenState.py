import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text


pygame.mixer.init()

import settings


class InstructionsState(BaseState):
    def enter(self, text_color=pygame.Color(255, 255, 255)) -> None:
        self.text_color = text_color
        
        pygame.mixer.music.load(
            settings.BASE_DIR / "assets" / "sounds" / "menu.mp3"
        )
        pygame.mixer.music.play(loops=-1)
        

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
            f"Objective: Collect 10 items of your color",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=(settings.VIRTUAL_HEIGHT // 2) - 35,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            f"to win or try to get the most when time is up!",
            color=pygame.Color(255, 255, 255),
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=(settings.VIRTUAL_HEIGHT // 2) - 15,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "MOVE: Arrows",
            color=pygame.Color(244, 64, 94),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) + 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 20,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "MOVE: W A S D",
            color=pygame.Color(64, 209, 244),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) - 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 20,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "SHOOT: RCTRL",
            color=pygame.Color(244, 64, 94),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) + 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 40,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "SHOOT: F",
            color=pygame.Color(64, 209, 244),
            font=settings.FONTS["medium"],
            x=(settings.VIRTUAL_WIDTH // 2) - 80,
            y=(settings.VIRTUAL_HEIGHT // 2) + 40,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "Menu",
            color=pygame.Color(81, 15, 160),
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=settings.VIRTUAL_HEIGHT - 20,
            center=True,
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("start")

    def exit(self) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
