import settings


class Tile():
    def __init__(self, x, y, frame):
        self.size = settings.TILE_SIZE
        self.x = x * self.size
        self.y = y * self.size
        self.frame = frame
        self.occupied = False 

    def render(self, surface):
        texture = settings.TEXTURES["tilesheet"]
        surface.blit(texture, (self.x, self.y), settings.FRAMES["tilesheet"][self.frame])