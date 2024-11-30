# import lib.
import pygame

# import variables / functions
from settings import p_speed, p_size
from support import debug, import_cut_graphics

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        
        self.x, self.y = pos
        self.surface = surface

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

    def draw_player(self):
        
        self.image = pygame.image.load(self.surface)
        height = self.image.get_height()
        width = self.image.get_width()
        self.image = pygame.transform.scale(
            self.image, ((width), (height))
        )
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # self.rect = self.image.get_rect(center=((self.y), (self.x - 50)))

    def update(self, dt, surface):
        self.draw_player()
