import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        # tiled setup
        self.image_ = pygame.Surface((size, size))
        self.image_.fill("grey")
        self.rect = self.image_.get_rect(topleft=(x, y))


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

    def update(self, x_shift):
        self.rect.x += x_shift

class Field(StaticTile):
    def __init__(self, x, y, size, value=None):
        super().__init__(
            size, x, y, pygame.image.load("./assets/Tilesets/Grass.png").convert_alpha()
        )
        img = pygame.Surface((size, size))
        img.fill("green")        
        self.image = pygame.transform.scale(img, (size * 0.6, size * 0.6))
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        print(center_x, center_y)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.value = value

        def draw_field(self, surface):
            surface.blit(self.image, self.rect)