import settings
import random

from src.Tile import Tile
from src.Obstacle import Obstacle
from src.Item import Item
from src.CirclePlayer import CirclePortal, CirclePlayer
from src.SquarePlayer import SquarePortal, SquarePlayer

from gale.timer import Timer


class Map:
    def __init__(self):
        self.tiles = set()
        self.obstacles = []
        self.collidable_tiles = set()
        self.projectiles = []
        self.items = []
        self.circle_tile = None
        self.square_tile = None
        self.circle_portal = None
        self.square_portal = None
        self._build_map()
        self._generate_obstacles()
        self._generate_circle_items()
        self._generate_square_items()

    def _build_map(self):

        for y in range(settings.MAP_HEIGHT):
            for x in range(settings.MAP_WIDTH):
                frame = None
                collidable = True
                occupied = True

                if y == 0 and x == 0:
                    frame = settings.TILE_CORNER
                elif y == 0 and x == settings.MAP_WIDTH - 1:
                    frame = settings.TILE_CORNER
                elif y == settings.MAP_HEIGHT - 1 and x == 0:
                    frame = settings.TILE_CORNER
                elif y == settings.MAP_HEIGHT - 1 and x == settings.MAP_WIDTH - 1:
                    frame = settings.TILE_CORNER
                elif (
                    y == 0
                    or y == settings.MAP_HEIGHT - 1
                    or x == 0
                    or x == settings.MAP_WIDTH - 1
                ):
                    frame = settings.TILE_SIDE
                else:
                    frame = random.choice(settings.TILE_FLOOR)
                    collidable = False
                    occupied = False

                tile = Tile(x, y, frame)
                tile.occupied = occupied
                self.tiles.add(tile)

                if x == 1 and y == 5:
                    self.circle_tile = tile
                    self.circle_portal = CirclePortal(tile.x, tile.y)

                if x == settings.MAP_WIDTH - 2 and y == 5:
                    self.square_tile = tile
                    self.square_portal = SquarePortal(tile.x, tile.y)

                if collidable:
                    self.collidable_tiles.add(tile)

    def _generate_obstacles(self):

        floor_tiles = list(self.tiles - self.collidable_tiles)
        floor_tiles.remove(self.circle_tile)
        floor_tiles.remove(self.square_tile)

        for _ in range(settings.OBSTACLES):
            tile = random.choice(floor_tiles)
            tile.occupied = True
            obstacle = Obstacle(tile.x, tile.y)

            self.obstacles.append(obstacle)

    def _generate_circle_items(self):
        floor_tiles = list(self.tiles - self.collidable_tiles)
        available_tiles = [tile for tile in floor_tiles if not tile.occupied]
        # MENINO MODIFICA ACA EL RANGO DE TILES PA QUE NO TOME EN CUENTA LOS BORDES
        for _ in range(settings.ITEMS):
            tile = random.choice(available_tiles)
            tile.occupied = True
            item = Item(
                tile.x,
                tile.y,
                settings.CIRCLE_ITEM_SIZE,
                settings.CIRCLE_ITEM_SIZE,
                "circle_item",
                "circle_item",
                CirclePlayer,
            )

            self.items.append(item)

    def _generate_square_items(self):
        floor_tiles = list(self.tiles - self.collidable_tiles)
        available_tiles = [tile for tile in floor_tiles if not tile.occupied]
        # MENINO MODIFICA ACA EL RANGO DE TILES PA QUE NO TOME EN CUENTA LOS BORDES

        for _ in range(settings.ITEMS):
            tile = random.choice(available_tiles)
            tile.occupied = True
            item = Item(
                tile.x,
                tile.y,
                settings.SQUARE_ITEM_WIDTH,
                settings.SQUARE_ITEM_HEIGHT,
                "square_item",
                "square_item",
                SquarePlayer,
            )

            self.items.append(item)

    def update(self, circle_player, square_player, dt):
        self.update_projectiles(dt)
        self.update_taken_items(circle_player, square_player)
        self.release_item(circle_player, square_player)

    def render(self, surface):
        for tile in self.tiles:
            tile.render(surface)

        for obstacle in self.obstacles:
            obstacle.render(surface)

        self.circle_portal.render(surface)
        self.square_portal.render(surface)

        for projectile in self.projectiles:
            projectile.render(surface)

        for item in self.items:
            item.render(surface)

    def update_projectiles(self, dt):
        for projectile in self.projectiles:
            collidable_objects = self.obstacles + list(self.collidable_tiles)
            projectile.update(dt, collidable_objects, self)

    def update_taken_items(self, circle_player, square_player):
        for item in self.items:
            if (
                not item.taken
                and circle_player.collides(item)
                and not circle_player.item
                and isinstance(circle_player, item.belongs)
            ):
                item.taken = True
                item.belongs = circle_player
                circle_player.item = item
            elif (
                not item.taken
                and square_player.collides(item)
                and not square_player.item
                and isinstance(square_player, item.belongs)
            ):
                item.taken = True
                item.belongs = square_player
                square_player.item = item

            if item.taken and not item.released:
                item.update()

    def release_item(self, circle_player, square_player):

        def release(item, player):
            player.item = None
            player.shape_counter += 1

        if circle_player.item and circle_player.collides(self.circle_portal):
            item = circle_player.item
            portal = self.circle_portal
            item.released = True

            Timer.tween(
                1,
                [
                    (
                        item,
                        {
                            "x": portal.x + (portal.size // 2) - (item.width // 2),
                            "y": portal.y + (portal.size // 2) - (item.height // 2),
                        },
                    ),
                ],
                on_finish=release(item, circle_player),
            )

        elif square_player.item and square_player.collides(self.square_portal):
            item = square_player.item
            portal = self.square_portal
            item.released = True

            Timer.tween(
                1,
                [
                    (
                        item,
                        {
                            "x": portal.x + (portal.size // 2) - (item.width // 2),
                            "y": portal.y + (portal.size // 2) - (item.height // 2),
                        },
                    ),
                ],
                on_finish=release(item, square_player),
            )
