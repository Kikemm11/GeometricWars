import settings
import random

from src.Tile import Tile
from src.Obstacle import Obstacle


class Map():
    def __init__(self):
        self.tiles = set()
        self.obstacles = []
        self.collidable_tiles = set()
        self.projectiles = []
        self.circle_tile = None
        self.square_tile = None
        self._build_map()
        self._generate_obstacles()


    def _build_map(self):
        
        for y in range(settings.MAP_HEIGHT):
            for x in range(settings.MAP_WIDTH):
                frame = None
                collidable = True

                if y == 0 and x == 0:
                    frame = settings.TILE_CORNER
                elif y == 0 and x == settings.MAP_WIDTH-1:
                    frame = settings.TILE_CORNER
                elif y == settings.MAP_HEIGHT-1 and x == 0:
                    frame = settings.TILE_CORNER
                elif y == settings.MAP_HEIGHT-1 and x == settings.MAP_WIDTH-1:
                    frame = settings.TILE_CORNER
                elif y == 0 or y == settings.MAP_HEIGHT-1 or x == 0 or x == settings.MAP_WIDTH-1:
                    frame = settings.TILE_SIDE
                else:
                    frame = random.choice(settings.TILE_FLOOR)
                    collidable = False

                tile = Tile(x, y, frame)
                self.tiles.add(tile)

                if x == 1 and y == 5:
                    self.circle_tile = tile
                
                if x == settings.MAP_WIDTH - 2 and y == 5:
                    self.square_tile = tile

                if collidable:
                    self.collidable_tiles.add(tile)


    def _generate_obstacles(self):
        
        floor_tiles = list(self.tiles - self.collidable_tiles)
        floor_tiles.remove(self.circle_tile)
        floor_tiles.remove(self.square_tile)
        
        for _ in range(settings.OBSTACLES):
            tile = random.choice(floor_tiles)
            obstacle = Obstacle(tile.x, tile.y)
           
            self.obstacles.append(obstacle)

    def update(self, dt):
        for projectile in self.projectiles:
            collidable_objects = self.obstacles + list(self.collidable_tiles)
            projectile.update(dt, collidable_objects, self)


    def render(self, surface):
        for tile in self.tiles:
            tile.render(surface)

        for obstacle in self.obstacles:
            obstacle.render(surface)

        for projectile in self.projectiles:
            projectile.render(surface)