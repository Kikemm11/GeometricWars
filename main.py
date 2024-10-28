import settings
from src.GeometricWars import GeometricWars

if __name__ == "__main__":
    geometric_wars = GeometricWars(
        "Geometric Wars",
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH,
        settings.VIRTUAL_HEIGHT,
    )
    geometric_wars.exec()
