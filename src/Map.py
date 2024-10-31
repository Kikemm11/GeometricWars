import settings
import random

from src.Tile import Tile
from src.Obstacle import Obstacle


class Map():
    def __init__(self):
        self.tiles = set()
        self.obstacles = set()
        self.collidable_tiles = set()
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

                if collidable:
                    self.collidable_tiles.add(tile)


    def _generate_obstacles(self):
        
        floor_tiles = list(self.tiles - self.collidable_tiles)
        
        for _ in range(settings.OBSTACLES):
            tile = random.choice(floor_tiles)
            obstacle = Obstacle(tile.x, tile.y)
           
            self.obstacles.add(obstacle)


    def render(self, surface):
        for tile in self.tiles:
            tile.render(surface)

        for obstacle in self.obstacles:
            obstacle.render(surface)