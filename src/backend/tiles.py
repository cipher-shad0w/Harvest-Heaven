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

    def update(self, x_shift):
        self.rect.x += x_shift


class Field():
    def __init__(self, pos, size, path):
        super().__init__()
        self.image = pygame.image.load("assets/field.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)