"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState

import settings


class WalkRight(BaseEntityState):
    def enter(self):
        self.entity.vx = settings.PLAYER_VX
        self.entity.vy = 0
        self.entity.change_animation("walk-right")

    def on_input(self, input_id, input_data):
        if input_id == "move_left_2" and input_data.pressed:
            self.entity.change_state("walk-left")
        elif input_id == "move_right_2" and input_data.released:
            self.entity.change_state("idle-right")
        elif input_id == "move_up_2" and input_data.pressed:
            self.entity.change_state("walk-up")
        elif input_id == "move_down_2" and input_data.pressed:
            self.entity.change_state("walk-down") 