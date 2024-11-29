import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        # tiled setup
        self.image = pygame.Surface((size, size))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft=(x, y))


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface


class Field(StaticTile):
    def __init__(self, x, y, size, value=None):
        super().__init__(
            size, x, y, pygame.image.load("./assets/Tilesets/Grass.png").convert_alpha()
        )       
        self.x = x
        self.y = y

    def update(self, dt, surface):
        pass