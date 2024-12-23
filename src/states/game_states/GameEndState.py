"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text

import settings

from src.CirclePlayer import CirclePlayer
from src.SquarePlayer import SquarePlayer


class GameEndState(BaseState):
    def enter(self, **params):
        
        pygame.mixer.music.load(
            settings.BASE_DIR / "assets" / "sounds" / "gameover.mp3"
        )
        pygame.mixer.music.play(loops=-1)
        
        self.player = params.get("player")

        if self.player:
            self.player.x = (settings.VIRTUAL_WIDTH // 2) - (self.player.width // 2)
            self.player.y = settings.VIRTUAL_HEIGHT // 2
            self.player.change_state("idle-down")

        self.selected = 1

    def render(self, surface):

        surface.blit(settings.TEXTURES["background"], (0, 0))

        message = "You've win!" if self.player else "It's a tie!"
        color = (255, 255, 255)

        color = (
            (64, 209, 244)
            if self.player and isinstance(self.player, CirclePlayer)
            else color
        )
        color = (
            (244, 64, 94)
            if self.player and isinstance(self.player, SquarePlayer)
            else color
        )

        render_text(
            surface,
            message,
            color=color,
            font=settings.FONTS["medium"],
            x=settings.VIRTUAL_WIDTH // 2,
            y=settings.VIRTUAL_HEIGHT // 4,
            center=True,
            shadowed=True,
        )

        if self.player:
            self.player.render(surface)

        color = (81, 15, 160) if self.selected == 1 else (255, 255, 255)

        render_text(
            surface,
            "Play Again",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 50,
            color,
            center=True,
        )

        color = (81, 15, 160) if self.selected == 2 else (255, 255, 255)

        render_text(
            surface,
            "Menu",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 20,
            color,
            center=True,
        )

    def on_input(self, input_id, input_data):
        if input_id == "move_down" and input_data.pressed:
            self.selected = 2 if self.selected == 1 else 1
            settings.SOUNDS["select"].stop()
            settings.SOUNDS["select"].play()

        elif input_id == "move_up" and input_data.pressed:
            self.selected = 1 if self.selected == 2 else 2
            settings.SOUNDS["select"].stop()
            settings.SOUNDS["select"].play()

        elif input_id == "enter" and input_data.pressed:

            if self.selected == 1:
                self.state_machine.change("playstate")
            else:
                self.state_machine.change("start")

    def exit(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()