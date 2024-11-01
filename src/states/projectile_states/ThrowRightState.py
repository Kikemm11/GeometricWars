from src.states.player_states.BaseEntityState import BaseEntityState
import settings

class ThrowRightState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vy = 0