import settings
import random

from src.Tile import Tile


class Map():
    def __init__(self):
        self.tiles = []
        self._build_map()

    def _build_map(self):
        
        for i in range(settings.MAP_HEIGHT):
            for j in range(settings.MAP_WIDTH):
                frame = None

                if i == 0 and j == 0:
                    frame = settings.TILE_CORNER
                elif i == 0 and j == settings.MAP_WIDTH-1:
                    frame = settings.TILE_CORNER
                elif i == settings.MAP_HEIGHT-1 and j == 0:
                    frame = settings.TILE_CORNER
                elif i == settings.MAP_HEIGHT-1 and j == settings.MAP_WIDTH-1:
                    frame = settings.TILE_CORNER
                elif i == 0 or i == settings.MAP_HEIGHT-1 or j == 0 or j == settings.MAP_WIDTH-1:
                    frame = settings.TILE_SIDE
                else:
                    frame = random.choice(settings.TILE_FLOOR)

                tile = Tile(i, j, frame)
                self.tiles.append(tile)


    def render(self, surface):
        for tile in self.tiles:
            tile.render(surface)