# import lib.
import pygame, sys, os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
)
from player import Player
from tiles import Tile
from support import import_csv_layout
from settings import tile_size


class Level:
    def __init__(self, level_data, surface):
        # get the display surface
        self.display_surface = surface

        soil_layout = import_csv_layout(level_data["soil"])
        self.soil_sprites = self.create_tile_group(soil_layout, "soil")

    def create_tile_group(self, layout, type):
        # create a sprite group
        sprite_group = pygame.sprite.Group()

        # iterate over the layout and create the sprites
        for y_index, row in enumerate(layout):
            for x_index, cell in enumerate(row):
                if cell == "33":
                    sprite = Tile(
                        x_index * tile_size, y_index * tile_size, tile_size
                    )
                    sprite_group.add(sprite)
                elif cell == "34":
                    sprite = Tile(
                        x_index * tile_size, y_index * tile_size, tile_size
                    )
                    sprite_group.add(sprite)
                elif cell == "35":
                    sprite = Tile(
                        x_index * tile_size, y_index * tile_size, tile_size
                    )
                    sprite_group.add(sprite)

        return sprite_group

    def update_and_draw(self, surface, dt):
        # update and draw the sprites
        self.soil_sprites.update(dt, surface)
        self.soil_sprites.draw(surface)

    def run(self, display_surface):
        self.soil_sprites.draw(self.display_surface)
