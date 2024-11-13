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

        self.circle_player = CirclePlayer(
            settings.TILE_SIZE + 0.7,
            settings.VIRTUAL_HEIGHT // 2 - settings.PLAYER_HEIGHT // 8,
        )
        self.circle_player.change_state("idle")

        self.square_player = SquarePlayer(
            settings.VIRTUAL_WIDTH - settings.PLAYER_WIDTH - settings.TILE_SIZE - 0.5,
            settings.VIRTUAL_HEIGHT // 2 - settings.PLAYER_HEIGHT // 8,
        )
        self.square_player.change_state("idle")

        # Set the timer duration (in seconds)
        self.timer_duration = settings.GAME_TIMER_DURATION_SECONDS  # 1 minute
        # Set up the clock
        self.clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks()
        self.time_left = self.timer_duration

    def update(self, dt: float) -> None:
        # region clock
        seconds = (
            pygame.time.get_ticks() - self.start_ticks
        ) / 1000  # Convert milliseconds to seconds
        self.time_left = int(max(0, self.timer_duration - seconds))
        if self.time_left <= 0:
            if self.square_player.shape_counter == self.circle_player.shape_counter:
                self.state_machine.change(
                    "game-over", "NO CONTEST!", pygame.Color(0, 255, 0)
                )
            elif self.square_player.shape_counter > self.circle_player.shape_counter:
                self.state_machine.change(
                    "game-over", "Square Wins!", pygame.Color(255, 0, 0)
                )

            else:
                self.state_machine.change(
                    "game-over", "Circle Wins!", pygame.Color(0, 50, 255)
                )
        # endregion
        self.circle_player.update(dt)
        self.square_player.update(dt)
        self.map.update(self.circle_player, self.square_player, dt)

        if self.check_players_collision(self.circle_player, self.square_player):
            self.circle_player.solve_world_collide()
            self.square_player.solve_world_collide()

        if self.check_player_sides_collision(
            self.circle_player
        ) or self.check_player_obstacle_collision(self.circle_player):
            self.circle_player.solve_world_collide()

        if self.check_player_sides_collision(
            self.square_player
        ) or self.check_player_obstacle_collision(self.square_player):
            self.square_player.solve_world_collide()

        for projectile in self.map.projectiles:
            if projectile.collides(self.circle_player):
                self.circle_player.go_vulnerable()
                self.map.projectiles.remove(projectile)
                continue

            if projectile.collides(self.square_player):
                self.square_player.go_vulnerable()
                self.map.projectiles.remove(projectile)
                continue

        if self.square_player.shape_counter >= settings.SCORE_TO_WIN:
            self.state_machine.change(
                "game-over", "Square Wins!", pygame.Color(255, 0, 0)
            )
        elif self.circle_player.shape_counter >= settings.SCORE_TO_WIN:
            self.state_machine.change(
                "game-over", "Circle Wins!", pygame.Color(0, 50, 255)
            )

    def render(self, surface: pygame.Surface) -> None:
        self.map.render(surface)
        self.circle_player.render(surface)
        self.square_player.render(surface)

        render_text(
            surface,
            f"Circle shapes: " + str(self.circle_player.shape_counter),
            settings.FONTS["medium"],
            settings.TILE_SIZE + 10,
            settings.TILE_SIZE // 4,
            (255, 255, 255),
            center=False,
        )

        render_text(
            surface,
            f"Square shapes: " + str(self.square_player.shape_counter),
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH - settings.TILE_SIZE * 8,
            settings.TILE_SIZE // 4,
            (255, 255, 255),
            center=False,
        )

        render_text(
            surface,
            f"TIME LEFT : {self.time_left}",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.TILE_SIZE // 4,
            (255, 255, 255),
            center=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.circle_player.on_input(input_id, input_data)
        self.circle_player.on_input_throw(input_id, input_data, self.map)

        self.square_player.on_input(input_id, input_data)
        self.square_player.on_input_throw(input_id, input_data, self.map)

    def check_players_collision(self, circle_player, square_player):
        return circle_player.collides(square_player) or square_player.collides(
            circle_player
        )

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
