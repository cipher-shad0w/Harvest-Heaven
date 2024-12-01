# import lib.
import pygame, sys

# import variables / functions
from backend.settings import screen_width, screen_height

# import classes
from backend.level import Level
from backend.game_data import level_0
from backend.ui import Overworld

class Game():

    def __init__(self):
        # call the method to create the level
        # self.create_level()
        self.status = "overworld"
        self.create_overworld()

    def create_overworld(self):
        self.overworld = Overworld(display_surface, self.create_level)
        self.status = "overworld"

    def create_level(self):
        # create the level with the class Level
        self.status = 'level'
        self.level = Level(level_0 ,display_surface)

    def run(self, dt):
        if self.status == "overworld":
            # call the run method on overworld (IMPORTANT)
            self.overworld.run()
        if self.status == "level":
            # call the run method on level (IMPORTANT)
            self.level.run(display_surface, dt)

# Pygame setup
pygame.init()
display_surface = pygame.display.set_mode((screen_width * 2,screen_height * 2))
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
game = Game()

# window setup (only needed if the screen is not fullscreen)
pygame.display.set_caption("Harvest Heaven")
pygame_icon = pygame.image.load("./assets/img.jpg")
pygame.display.set_icon(pygame_icon)

while True:
    # to get a user input
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        # to quite the game
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            pygame.quit()
            sys.exit()

    # overwrite the old level layer (IMPORTANT)
    display_surface.fill("#c0d470")

    # for the performance (FPS)
    dt = clock.tick() / 100
    print(dt)
    y = display_surface.get_height()
    x = display_surface.get_width()

    # run the game
    game.run(dt)
    pygame.display.update()
