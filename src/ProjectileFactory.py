"""
Authors: 
- Ivan Maldonado (Kikemaldonado11@gmail.com)
- Juan Gomez (juan.andres.gomezp@gmail.com)

Developed at: November 2024
"""

import pygame
import settings

from src.Projectile import Projectile

class ProjectileFactory():

    @classmethod
    def throw_projectile(cls, map, player):

        x = None
        y = None
        state = None
        vx = vy = settings.PROJECTILE_VELOCITY

        animation_id = (animation_id for animation_id in player.animations.keys() if player.animations[animation_id] == player.current_animation).__next__()
        direction = animation_id.split('-')[1]

        if direction == 'up':
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y - 15
            vx = 0
            vy *= -1
        elif direction == 'down':
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y + player.height
            vx = 0
        elif direction == 'left':
            x = player.x - settings.PROJECTILE_SIZE
            y = player.y + (player.height // 2) - (settings.PROJECTILE_SIZE // 2)
            vx *= -1
            vy = 0
        else:
            x = player.x + player.width
            y = player.y + (player.height // 2) - (settings.PROJECTILE_SIZE // 2)
            vy = 0

        projectile = Projectile(x, y)
        projectile.vx = vx
        projectile.vy = vy
        projectile.change_animation("throw")

        map.projectiles.append(projectile)