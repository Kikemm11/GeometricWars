import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text

import settings
from src.Player import Player
from src.Map import Map
from src.CirclePlayer import CirclePlayer
from src.SquarePlayer import SquarePlayer


class PlayState(BaseState):

    def enter(self) -> None:
        self.title = Text(
            "Geometric Wars",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH,
            settings.VIRTUAL_HEIGHT // 4,
            (197, 195, 198),
            shadowed=True,
        )

        self.map = Map()

        self.circle_player = CirclePlayer(settings.TILE_SIZE + 0.7, settings.VIRTUAL_HEIGHT // 2 - settings.PLAYER_HEIGHT//8)
        self.circle_player.change_state("idle")

        self.square_player = SquarePlayer(settings.VIRTUAL_WIDTH - settings.PLAYER_WIDTH - settings.TILE_SIZE - 0.5, settings.VIRTUAL_HEIGHT // 2 - settings.PLAYER_HEIGHT//8)
        self.square_player.change_state("idle")
        

    def update(self, dt: float) -> None:
        self.circle_player.update(dt)
        self.square_player.update(dt)

        self.check_players_collision(self.circle_player, self.square_player)

        if self.check_player_sides_collision(self.circle_player) or self.check_player_obstacle_collision(self.circle_player):
            self.circle_player.solve_world_collide()

        if self.check_player_sides_collision(self.square_player) or self.check_player_obstacle_collision(self.square_player):
            self.square_player.solve_world_collide()


    def render(self, surface: pygame.Surface) -> None:
        self.map.render(surface)
        self.circle_player.render(surface)
        self.square_player.render(surface)


    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.circle_player.on_input(input_id, input_data)
        self.square_player.on_input(input_id, input_data)


    def check_players_collision(self, circle_player, square_player):
        if circle_player.collides(square_player) or square_player.collides(circle_player):
            circle_player.vx = square_player.vx = 0
            circle_player.vy = square_player.vy = 0

    def check_player_sides_collision(self, player):
        for tile in self.map.collidable_tiles:
            if player.collides(tile):
                return True 
        return False
    
    def check_player_obstacle_collision(self, player):
        for obstacle in self.map.obstacles:
            if player.collides(obstacle):
                return True
        return False