import pygame
from core.IColiable import IColiable

class Tile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int] | str):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))