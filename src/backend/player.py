# import lib.
import pygame

# import variables / functions
from settings import p_speed, p_size
from support import debug

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2() #self.rect.center -- in ()
        self.speed = p_speed
        
        # animation setup
        self.frame_index = 1
        self.frames = 6
        self.animation_speed = 0.0017
        
        # status
        self.status = 'right'
        self.attack = False
        
        # player image settings 
        self.imgs_idle = []
        self.imgs_run = []
        self.imgs_down = []
        self.imgs_up = []
        
        self.imgs_idle_attack = []
        self.imgs_idle_attack_down = []
        self.imgs_idle_attack_up = []
        
        self.imgs_run_attack = []
        self.imgs_run_attack_down = []
        self.imgs_run_attack_up = []
    
    def update(self, dt, surface):
        pass