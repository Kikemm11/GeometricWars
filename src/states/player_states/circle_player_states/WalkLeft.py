from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState

import settings


class WalkLeft(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = settings.PLAYER_VX * -1
        self.entity.vy = 0
        self.entity.change_animation("walk-left")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left_2" and input_data.released:
            self.entity.change_state("idle-left")
        elif input_id == "move_right_2" and input_data.pressed:
            self.entity.change_state("walk-right")
        elif input_id == "move_up_2" and input_data.pressed:
            self.entity.change_state("walk-up")
        elif input_id == "move_down_2" and input_data.pressed:
            self.entity.change_state("walk-down") 