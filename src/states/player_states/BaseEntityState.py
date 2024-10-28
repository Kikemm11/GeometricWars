
from gale.state import BaseState, StateMachine

class BaseEntityState(BaseState):
    def __init__(self, entity, state_machine) -> None:
        super().__init__(state_machine)
        self.entity = entity