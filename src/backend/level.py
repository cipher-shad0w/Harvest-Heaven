# import lib.
import pygame, sys, os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
)
from player import Player
from tiles import Tile, StaticTile
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, zoom


class Level:
    def __init__(self, level_data, surface):
        # get the display surface
        self.display_surface = surface

        soil_layout = import_csv_layout(level_data["soil"])
        self.soil_sprites = self.create_tile_group(soil_layout, "soil")

        ground_layout = import_csv_layout(level_data["ground"])
        self.ground_sprites = self.create_tile_group(ground_layout, "ground")

        fences_layout = import_csv_layout(level_data["fences"])
        self.fences_sprites = self.create_tile_group(fences_layout, "fences")

        player_layout = import_csv_layout(level_data["player"])
        self.player_sprites = self.create_tile_group(player_layout, "player")

    def create_tile_group(self, layout, type):
        # create a sprite group
        sprite_group = pygame.sprite.Group()

        # iterate over the layout and create the sprites
        for y_index, row in enumerate(layout):
            for x_index, cell in enumerate(row):
                if cell != '-1':
                    x = x_index * (tile_size *2)
                    y = y_index * (tile_size * 2)

                    if type == "soil":
                        soil_tile_list = import_cut_graphics("./assets/Tilesets/Tilled_Dirt_Wide.png")
                        tile_surface = soil_tile_list[int(cell)]
                        sprite = StaticTile(x, y, tile_size * 2, tile_surface)
                    if type == "ground":
                        ground_tile_list = import_cut_graphics(
                            "./assets/Tilesets/Grass.png"
                        )
                        tile_surface = ground_tile_list[int(cell)]
                        sprite = StaticTile(x, y, tile_size *2, tile_surface)
                    if type == "fences":
                        fences_tile_list = import_cut_graphics(
                            "./assets/Tilesets/Fences.png"
                        )
                        tile_surface = fences_tile_list[int(cell)]
                        sprite = StaticTile(x, y, tile_size * 2, tile_surface)
                    if type == "player":
                        player_tile_list = import_cut_graphics(
                            "./assets/player/Basic_Charakter_Spritesheet.png"
                        )
                        player_surface = player_tile_list[1]
                        sprite = Player((x, y), player_surface)
                    if sprite:
                        sprite_group.add(sprite)

        return sprite_group

    def update_and_draw(self, surface, dt):
        # update and draw the sprites
        
        self.ground_sprites.draw(surface)
        self.ground_sprites.update(dt, surface)

        self.fences_sprites.draw(surface)
        self.fences_sprites.update(dt, surface)

        self.soil_sprites.draw(surface)
        self.soil_sprites.update(dt, surface)

        # self.player_sprites.draw(surface)
        # self.player_sprites.update(dt, surface)
        
    def run(self, display_surface):
        self.update_and_draw(self.display_surface, 0.1)
