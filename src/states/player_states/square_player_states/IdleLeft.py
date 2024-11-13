from gale.input_handler import InputData
from src.states.player_states.BaseEntityState import BaseEntityState


class IdleLeft(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle-left")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left" and input_data.pressed:
            self.entity.change_state("walk-left")
        elif input_id == "move_right" and input_data.pressed:
            self.entity.change_state("walk-right")
        elif input_id == "move_up" and input_data.pressed:
            self.entity.change_state("walk-up")
        elif input_id == "move_down" and input_data.pressed:
            self.entity.change_state("walk-down")