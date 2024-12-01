# import lib.
import pygame
from settings import screen_height, screen_width, tile_size
from functools import wraps
from typing import Callable, Any
from time import perf_counter
from csv import reader
from os import walk

# import from pygame and set the font
pygame.init()
surface = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 30)


# debugging surface
def debug(info: str, surface, y: int = 1, x: int = 1):
    if not surface:
        display_surf = pygame.display.get_surface()
    else:
        display_surf = surface
    debug_surf = font.render(str(info), True, "white")
    debug_rect = debug_surf.get_rect(topleft=((x * 25 - 15), (y * 25 + 10)))
    pygame.draw.rect(surface, "black", debug_rect)
    display_surf.blit(debug_surf, debug_rect)


def load(path: str):
    pygame.image.load(path).convert_alpha()


# a class to subtract the spritesheet in different small images
class Spritesheet:
    def __init__(self, image):
        self.image = image

    def get_img(
        self, col: int, row: int, width: int, height: int, scale: int, color: str
    ):
        image = pygame.Surface((width, height)).convert_alpha()
        # image.fill('grey')
        image.blit(self.image, (0, 0), ((col * width), (row * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        image.set_colorkey(color)

        return image


def get_time(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # Note that timing your code once isn't the most reliable option
        # for timing your code. Look into the timeit module for more accurate
        # timing.

        # to use the function write @get_time above the function

        start_time: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = perf_counter()

        print(
            f'"{func.__name__}()" took {end_time - start_time:.3f} seconds to execute'
        )
        return result

    return wrapper


def import_csv_layout(path):
    _map = []

    with open(path) as map:
        level = reader(map, delimiter=",")
        for row in level:
            _map.append(list(row))
        return _map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size

            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            new_surf = pygame.transform.scale(
                new_surf, (tile_size * 2, tile_size * 2)
            )  # <== Zoom um Faktor 2
            cut_tiles.append(new_surf)

    return cut_tiles


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
