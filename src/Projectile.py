"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

import pygame
from gale.input_handler import InputData

from gale.state import StateMachine, BaseState
from src import mixins

from src.Obstacle import Obstacle

import settings


class Projectile(mixins.DrawableMixin, mixins.AnimatedMixin, mixins.CollidableMixin):
    def __init__(self, x, y): 
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

        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
    

    def update(self, dt, collidable_objects, map):
        
        mixins.AnimatedMixin.update(self, dt)

        self.y +=  + self.vy * dt
        self.x +=  + self.vx * dt

        for object in collidable_objects:
            if self.collides(object):
                self.on_collide(object, map)


    def get_collision_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


    def on_collide(self, object, map):
        if isinstance(object, Obstacle):
            map.obstacles.remove(object)

        if self in map.projectiles:
            map.projectiles.remove(self)
            
        settings.SOUNDS["hit"].stop()
        settings.SOUNDS["hit"].play()