"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState


class IdleDown(BaseEntityState):
    def enter(self):
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle-down")

    def on_input(self, input_id, input_data):
        if input_id == "move_left" and input_data.pressed:
            self.entity.change_state("walk-left")
        elif input_id == "move_right" and input_data.pressed:
            self.entity.change_state("walk-right")
        elif input_id == "move_up" and input_data.pressed:
            self.entity.change_state("walk-up")
        elif input_id == "move_down" and input_data.pressed:
            self.entity.change_state("walk-down")