import pygame
import settings

from src.Projectile import Projectile

class ProjectileFactory():

    @classmethod
    def throw_projectile(cls, map, player):

        x = None
        y = None
        state = None

        if player.vx > 0:
            x = player.x + player.width
            y = player.y + (player.height // 2) - (settings.PROJECTILE_SIZE // 2)
            state = "throw-right"
        elif player.vx < 0:
            x = player.x - settings.PROJECTILE_SIZE
            y = player.y + (player.height // 2) - (settings.PROJECTILE_SIZE // 2)
            state = "throw-left"
        elif player.vy > 0:
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y + player.height
            state = "throw-down"
        elif player.vy < 0:
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y - 15
            state = "throw-up"
        else:
            x = player.x + (player.width // 2) - (settings.PROJECTILE_SIZE // 2)
            y = player.y + player.height
            state = "throw-down"
        
        projectile = Projectile(x, y)
        projectile.change_state(state)
        projectile.change_animation("throw")

        map.projectiles.append(projectile)

