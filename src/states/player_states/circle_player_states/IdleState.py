from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left_2" and input_data.pressed:
            self.entity.change_state("walk-left")
        elif input_id == "move_right_2" and input_data.pressed:
            self.entity.change_state("walk-right")
        elif input_id == "move_up_2" and input_data.pressed:
            self.entity.change_state("walk-up")
        elif input_id == "move_down_2" and input_data.pressed:
            self.entity.change_state("walk-down")         