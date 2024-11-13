import pygame
import settings

from src.Projectile import Projectile

class ProjectileFactory():

    @classmethod
    def throw_projectile(cls, map, player):

        x = None
        y = None
        state = None

        animation_id = (animation_id for animation_id in player.animations.keys() if player.animations[animation_id] == player.current_animation).__next__()
        direction = animation_id.split('-')[1]

        if direction == 'up':
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y - 15
            state = f"throw-{direction}"
        elif direction == 'down':
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y + player.height
            state = f"throw-{direction}"
        elif direction == 'left':
            x = player.x - settings.PROJECTILE_SIZE
            y = player.y + (player.height // 2) - (settings.PROJECTILE_SIZE // 2)
            state = f"throw-{direction}"
        else:
            x = player.x + player.width
            y = player.y + (player.height // 2) - (settings.PROJECTILE_SIZE // 2)
            state = f"throw-{direction}"


        projectile = Projectile(x, y)
        projectile.change_state(state)
        projectile.change_animation("throw")

        map.projectiles.append(projectile)