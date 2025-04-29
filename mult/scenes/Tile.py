import pygame
from typing import Tuple, Union  # necessário para Python 3.8
from core.IColiable import IColiable

class Tile(pygame.sprite.Sprite, IColiable):
    def __init__(self, x: int, y: int, width: int, height: int, color: Union[Tuple[int, int, int], str]):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
