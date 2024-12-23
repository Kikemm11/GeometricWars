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

from src.Player import Player
from src.CirclePlayer import CirclePlayer
from src.SquarePlayer import SquarePlayer


class StartState(BaseState):

    def enter(self):
        
        pygame.mixer.music.load(
            settings.BASE_DIR / "assets" / "sounds" / "menu.mp3"
        )
        pygame.mixer.music.play(loops=-1)

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

    

    def update(self, dt):
        self.circle_player.update(dt)
        self.square_player.update(dt)

        self.erratic_players(self.circle_player, self.square_player)

    def render(self, surface):

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
                self.state_machine.change("instructions")
                
                
    def exit(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        

    def erratic_players(self, circle_player, square_player):

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