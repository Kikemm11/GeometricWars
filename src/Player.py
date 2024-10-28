from typing import TypeVar, Dict, Any, Tuple

from gale.state import StateMachine, BaseState
from src import mixins
import settings


class Player(mixins.DrawableMixin, mixins.AnimatedMixin, mixins.CollidableMixin):
    def __init__(self, player_def: Dict[str, Dict[str, Any]]) -> None:
        self.x = player_def["x"]
        self.y = player_def["y"]
        self.width = player_def["width"]
        self.height = player_def["height"]
        self.vx: float = 0
        self.vy: float = 0
        self.texture_id = player_def["texture_id"]
        self.frame_index = -1
        self.state_machine = StateMachine(player_def["states"])
        self.current_animation = None
        self.animations = {}
        self.generate_animations(player_def["animation_defs"])

    def change_state(
        self, state_id: str, *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> None:
        self.state_machine.change(state_id, *args, **kwargs)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        mixins.AnimatedMixin.update(self, dt)
        self.y += self.vy * dt

        next_x = self.x + self.vx * dt

        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(self.tilemap.width - self.width, next_x)