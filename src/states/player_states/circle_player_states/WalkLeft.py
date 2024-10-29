from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState

import settings


class WalkLeft(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = settings.CIRCLE_PLAYER_VX * -1
        self.entity.vy = 0
        self.entity.change_animation("walk-left")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            print("Move left")
        elif input_id == "move_right" and input_data.pressed:
            print("Move right")
        elif input_id == "move_up" and input_data.pressed:
            print("Move up")
        elif input_id == "move_down" and input_data.pressed:
            print("Move down")    