from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState

import settings


class WalkDown(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = settings.CIRCLE_PLAYER_VY 
        self.entity.change_animation("walk-down")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            print("Move left")
        elif input_id == "move_right" and input_data.pressed:
            print("Move right")
        elif input_id == "move_up" and input_data.pressed:
            print("Move up")
        elif input_id == "move_down" and input_data.pressed:
            print("Move down")    