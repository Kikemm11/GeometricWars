"""
Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the AnimatedMixin.
"""

from gale.state import BaseState, StateMachine

class BaseEntityState(BaseState):
    def __init__(self, entity, state_machine):
        super().__init__(state_machine)
        self.entity = entity