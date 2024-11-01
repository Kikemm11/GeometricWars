from src.states.player_states.BaseEntityState import BaseEntityState
import settings

class ThrowUpState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vy *= -1
        self.entity.vx = 0 
        