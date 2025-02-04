import pygame
from config import globals


SPRITE_SCALE_RATIO = (32, 32)

class Sprites:
    class Pudim:
        walkRight   = [pygame.transform.smoothscale(pygame.image.load(f"{globals.PLAYER_IMAGE_DIR}right/{i}.png"), SPRITE_SCALE_RATIO) for i in range(0, 4)]
        walkLeft    = [pygame.transform.smoothscale(pygame.image.load(f"{globals.PLAYER_IMAGE_DIR}left/{i}.png"), SPRITE_SCALE_RATIO) for i in range(0, 4)]
        walkUp      = [pygame.transform.smoothscale(pygame.image.load(f"{globals.PLAYER_IMAGE_DIR}up/{i}.png"), SPRITE_SCALE_RATIO) for i in range(0, 4)]
        walkDown    = [pygame.transform.smoothscale(pygame.image.load(f"{globals.PLAYER_IMAGE_DIR}down/{i}.png"), SPRITE_SCALE_RATIO) for i in range(0, 4)]
    class Pan:
        walk        = [pygame.transform.smoothscale(pygame.image.load(f"{globals.PAN_IMAGE_DIR}/{i}.png"), SPRITE_SCALE_RATIO) for i in range(0, 4)]
    class Jelly:
        pass
