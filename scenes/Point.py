import pygame
from core.IColiable import IColiable


class Point(pygame.sprite.Sprite, IColiable):
    def __init__(self, x: int, y: int, radius: int, color: tuple[int, int, int]):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA) 
        self.image.fill((0, 0, 0, 0)) 
        pygame.draw.circle(self.image, color, (radius, radius), radius)  
        self.rect = self.image.get_rect(center=(x, y))  

class SuperPoint(Point):
    def __init__(self, *args, **k):
        super().__init__(*args, **k)