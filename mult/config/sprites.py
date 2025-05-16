from typing import Tuple
import pygame
from config import globals

class _Sprite:
    def __init__(self, path: str):
         self.path = path

    def __call__(self, ratio: Tuple[int, int], size: int = 4) -> list:
        return [pygame.transform.smoothscale(pygame.image.load(f"{self.path}/{i}.png"), ratio) for i in range(0, size)]

class Sprites:
    
    class Pudim:
        walkRight   = _Sprite(f"{globals.PLAYER_IMAGE_DIR}/right")
        walkLeft    = _Sprite(f"{globals.PLAYER_IMAGE_DIR}/left")
        walkUp      = _Sprite(f"{globals.PLAYER_IMAGE_DIR}/up")
        walkDown    = _Sprite(f"{globals.PLAYER_IMAGE_DIR}/down")
    class Pan:
        walkRight        = _Sprite(f"{globals.PAN_IMAGE_DIR}/right")  
        walkLeft         = _Sprite(f"{globals.PAN_IMAGE_DIR}/left")
    class Jelly:
        walkRight        = _Sprite(f"{globals.JELLY_IMAGE_DIR}/right")
        walkLeft         = _Sprite(f"{globals.JELLY_IMAGE_DIR}/left")
