from src.states.player_states.circle_player_states.IdleState import  IdleState
import settings

PLAYER = {
    "circle": {
        "x": settings.VIRTUAL_WIDTH /2,
        "y": settings.VIRTUAL_HEIGHT - 50,
        "width": settings.CIRCLE_PLAYER_WIDTH,
        "height": settings.CIRCLE_PLAYER_HEIGHT,
        "texture_id": "circle_player",
        "states": {"idle": lambda sm: IdleState(self, sm)},
        "animation_defs": {"idle": {"frames": [0, 2], "interval": 0.25}},
    },
}