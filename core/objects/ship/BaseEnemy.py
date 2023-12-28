import pygame
from core.objects.ship.types.Ship import Ship

class BaseEnemy(Ship):

    def __init__(self, position: tuple, group: object) -> None:
        super().__init__(position, group, 'graphics/ship1.png')
        self.normal = self.direction.copy()

    def move(self):
        pass

    def events(self):
        pass