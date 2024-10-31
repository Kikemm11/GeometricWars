import settings
import random

from src.Tile import Tile


class Map():
    def __init__(self):
        self.tiles = []
        self._build_map()

    def _build_map(self):
        
        for y in range(settings.MAP_HEIGHT):
            for x in range(settings.MAP_WIDTH):
                frame = None

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

                tile = Tile(x, y, frame)
                self.tiles.append(tile)


    def render(self, surface):
        for tile in self.tiles:
            tile.render(surface)