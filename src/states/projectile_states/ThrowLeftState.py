from src.states.player_states.BaseEntityState import BaseEntityState
import settings

class ThrowLeftState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vy = 0
        self.entity.vx *= -1