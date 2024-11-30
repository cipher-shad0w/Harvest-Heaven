# import lib.
import pygame

# import variables / functions
from settings import p_speed, p_size
from support import debug

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple):
        super().__init__()
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos) #self.rect.center -- in ()
        self.speed = p_speed
        
        # animation setup
        self.frame_index = 1
        self.frames = 6
        self.animation_speed = 0.0017
        
        # status
        self.status = 'right'
        self.interackt = False
        
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
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #  self.direction.x(1)
            self.direction.x = self.speed
            print("right")
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            print("left")
            self.direction.x = self.speed * -1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("up")
            self.direction.y = self.speed * -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("down")
            self.direction.y = self.speed

        # print(self.pos)

    def update(self, dt, surface):
        self.get_input()
        self.pos.x = self.pos.x + (self.direction.x*dt)
        self.pos.y = self.pos.y + (self.direction.y*dt)
        print(self.pos.xy)
        self.direction.x = 0
        self.direction.y = 0
        
        player_rect = pygame.Rect(self.pos.x, self.pos.y, 20 ,20)
        pygame.draw.rect(surface, "green", player_rect)