# import lib.
import pygame, sys, os

# import variables / functions
from backend.settings import screen_width, screen_height

# import classes
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))
from player import Player

class Level():
    def __init__(self, surface):
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
        
        # layer
        # self.all_sprites.draw(surface)
    
    def run(self, dt):
        # call methods to draw sth. on the surface
        self.update_and_draw(self.display_surface, dt)
        
        # player / wall collision
        # self.horizontal_movement_collision()
        # self.vertical_movement_collision()
        self.out_of_bounds()