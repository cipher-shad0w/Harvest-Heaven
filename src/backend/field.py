# import lib.
import pygame

# import variables / functions
from support import debug

class Field(pygame.sprite.Sprite):
    def __init__(self, pos: tuple):
        super().__init__()
        
        self.pos = pygame.math.Vector2(pos) #self.rect.center -- in ()
        
        self.field_rect = pygame.Rect(self.pos.x, self.pos.y, 50 ,50)
        
        self.color = pygame.Color(255,10,10)
        
    
        # print(self.pos)

    def draw(self, surface):
        pygame.draw.rect(surface,self.color, self.field_rect)
    
    def update(self, dt, surface):
        # pygame.draw.rect(surface, "orange", temp)
        pass