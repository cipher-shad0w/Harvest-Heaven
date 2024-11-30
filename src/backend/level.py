# import lib.
import pygame

# import variables / functions
from settings import screen_width, screen_height

# import classes
from player import Player
from tiles import Tile, StaticTile
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, zoom


class Level:
    def __init__(self, level_data, surface):
        # get the display surface
        self.display_surface= surface
        
        # call important methods
        self.setup()
    
    def setup(self):
        # screen_width = 1280
        # screen_height = 720

        # create all sprites
        self.all_sprites = pygame.sprite.Group()
        # self.player = pygame.sprite.GroupSingle()
        
        # player setup
        self.player_pos = (screen_width/2, screen_height/2)
        # player = Player(self.player_pos)
        self.player = Player(self.player_pos)
        # self.player.add(player)
        # self.player ist eine Single-Sprite-Gruppe, in der ein Objekt der Klasse Player ist

    
    def horizontal_movement_collision(self):
        # setup for horizontal movement
        # player = self.player.sprite
        # player.rect.x += player.direction.x * player.speed
        
        # check if a block left or right besides the player
        for sprite in self.all_sprites.sprites():
            if sprite.rect.colliderect(self.player.rect):
                
                # left
                if self.player.direction.x < 0:
                    self.player.rect.left = sprite.rect.right
                    self.current_x = self.player.rect.left
                
                # right
                elif self.player.direction.x > 0:
                    self.player.rect.right = sprite.rect.left
                    self.current_x = self.player.rect.right
    
    def vertical_movement_collision(self):
        # setup for horizontal movement
        # player = self.player.sprite
        
        # process player on ground
        for sprite in self.all_sprites.sprites():
            if sprite.rect.colliderect(self.player.rect):
                
                # player is on a block 
                if self.player.direction.y > 0:
                    self.player.rect.bottom = sprite.rect.top
                    self.player.direction.y = 0
                    self.player.on_ground = True
                
                # player is not on a block
                elif self.player.direction.y < 0:
                    self.player.rect.top = sprite.rect.bottom
                    self.player.direction.y = 0
    
    def out_of_bounds(self):
        if self.player.pos.x < 0:
            self.player.pos.x = 0
        if self.player.pos.y < 0:
            self.player.pos.y = 0
        if self.player.pos.x > screen_width:
            self.player.pos.x = screen_width
        if self.player.pos.y > screen_height:
            self.player.pos.y = screen_height


    def update_and_draw(self, surface, dt):
        # player 
        # self.player.
        
        self.player.update(dt, surface)
        
        
        
        # self.player.pos.x = (self.player.pos.x + self.player.direction.x)
        # self.player.draw(surface)
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
                        sprite = StaticTile(x, y, tile_size * 2, tile_surface)
                    if type == "fences":
                        fences_tile_list = import_cut_graphics(
                            "./assets/Tilesets/Fences.png"
                        )
                        tile_surface = fences_tile_list[int(cell)]
                        sprite = StaticTile(x, y, tile_size *2, tile_surface)
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
        
        # player / wall collision
        # self.horizontal_movement_collision()
        # self.vertical_movement_collision()
        self.out_of_bounds()
