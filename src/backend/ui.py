import pygame


class Overworld:
    def __init__(self, surface, create_level):

        # setup
        self.display_surface = surface
        self.create_level = create_level

        # movement logic
        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 8

        # time
        self.start_time = pygame.time.get_ticks()
        self.allow_input = False
        self.timer_length = 300

        # background
        self.opacity = 80

        # font setup for text
        self.font = pygame.font.Font(None, 80)  # Default font, size 80
        self.text_color = "white"

    def background(self):
        screen_width = self.display_surface.get_width()
        screen_height = self.display_surface.get_height()
        # background image
        bg = pygame.image.load("./assets/bg.jpg")
        scaled_bg = pygame.transform.scale(bg, (screen_width, screen_height))
        self.display_surface.blit(scaled_bg, (0, 0))

        # background overlay
        self.image = pygame.Surface((screen_height, screen_width))
        self.image.fill("black")
        overlay = pygame.transform.scale(self.image, (screen_width, screen_height))
        overlay.set_alpha(self.opacity)
        self.display_surface.blit(overlay, (0, 0))

    def draw_text(self):
        # Render the text
        text_surface = self.font.render("Harvest Heaven", True, self.text_color)

        # Get the text rectangle and center it
        text_rect = text_surface.get_rect(
            center=(
                self.display_surface.get_width() // 2,
                self.display_surface.get_height() // 2,
            )
        )

        # Blit the text to the display surface
        self.display_surface.blit(text_surface, text_rect)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.create_level()

    def run(self):
        self.background()
        self.draw_text()  # Draw the text
        self.get_input()
