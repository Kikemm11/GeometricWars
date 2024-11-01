import pygame
from gale.input_handler import InputData

from gale.state import StateMachine, BaseState
from src import mixins

from src.states.projectile_states import ThrowUpState, ThrowDownState, ThrowLeftState, ThrowRightState
from src.Obstacle import Obstacle

import settings


class Projectile(mixins.DrawableMixin, mixins.AnimatedMixin, mixins.CollidableMixin):
    def __init__(self, x, y) -> None:
        
        self.x = x
        self.y = y
        self.vx = settings.PROJECTILE_VELOCITY
        self.vy = settings.PROJECTILE_VELOCITY
        self.size = settings.PROJECTILE_SIZE
        self.texture_id = "projectile"
        self.frame_index = -1

        animation_defs={
            "throw": {"frames": [0, 1, 2], "interval": 0.2},
        }

        states = {
                "throw-up": lambda sm: ThrowUpState.ThrowUpState(self, sm),
                "throw-down": lambda sm: ThrowDownState.ThrowDownState(self, sm),
                "throw-left": lambda sm: ThrowLeftState.ThrowLeftState(self, sm),
                "throw-right": lambda sm: ThrowRightState.ThrowRightState(self, sm),
            }


        self.state_machine = StateMachine(states)

        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
    

    def update(self, dt, collidable_objects, map) -> None:
        
        mixins.AnimatedMixin.update(self, dt)

        self.y +=  + self.vy * dt
        self.x +=  + self.vx * dt

        for object in collidable_objects:
            if self.collides(object):
                self.on_collide(object, map)


    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def change_state(
        self, state_id: str, *args, **kwargs) -> None:
        self.state_machine.change(state_id, *args, **kwargs)

    def on_collide(self, object, map):
        if isinstance(object, Obstacle):
            map.obstacles.remove(object)

        if self in map.projectiles:
            map.projectiles.remove(self)
