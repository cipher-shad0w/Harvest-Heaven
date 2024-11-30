import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        # tiled setup
        self.image = pygame.Surface((size, size))
        self.image = pygame.transform.scale(self.image, (size * 2, size * 2))
        self.rect = self.image.get_rect(topleft=(x, y))

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

class FieldTile(StaticTile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y, pygame.image.load('./assets/Tilesets/Tilled_Dirt_Wide.png').convert_alpha())
        

class AnimatedTile(Tile):
    def __init__(self, size, x, y, surface_list):
        super().__init__(size, x, y)
        self.surface_list = surface_list
        self.frame_index = 0
        self.animation_speed = 0.1

    def update(self, dt, surface):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.surface_list):
            self.frame_index = 0
        self.image = self.surface_list[int(self.frame_index)]