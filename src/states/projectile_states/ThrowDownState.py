from src.states.player_states.BaseEntityState import BaseEntityState
import settings

class ThrowDownState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0