"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

import pygame

from gale.game import Game
from gale.input_handler import InputData
from gale.state import StateMachine

from src.states import game_states


class GeometricWars(Game):
    def init(self):
        self.state_machine = StateMachine(
            {
                "start": game_states.StartState,
                "playstate": game_states.PlayState,
                "game-over": game_states.GameEndState,
                "instructions": game_states.InstructionsState,
            }
        )
        self.state_machine.change("start")

    def update(self, dt):
        self.state_machine.update(dt)

    def render(self, surface):
        self.state_machine.render(surface)

    def on_input(self, input_id, input_data):
        if input_id == "quit" and input_data.pressed:
            self.quit()
        else:
            self.state_machine.on_input(input_id, input_data)
