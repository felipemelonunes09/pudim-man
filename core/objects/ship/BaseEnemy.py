import pygame

from core.objects.ship.BaseShipEngine import BaseShipEngine


class BaseEnemy(BaseShipEngine):

    def __init__(self, position: tuple, group: object, ship: object) -> None:
        super().__init__(position, group, 'graphics/ship1.png', ship)
        self.normal = self.direction.copy()

    def move(self):
        pass

    def events(self):
        pass