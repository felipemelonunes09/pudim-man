
from core.objects.ship.attack.SpriteShot import SpriteShot


import pygame


## review variable shooter if its really necessary
class PrimaryShot(SpriteShot):

    def __init__(self, speed: float, damage: float, position: any, direction: tuple, group: any, shooter) -> None:
        super().__init__(speed, damage, position, direction, group, shooter, 'graphics/shot1.png')

        self.__image = self.image
        self.rotate_image(shooter.normal)

    def rotate_image(self, normal):
        self.image = pygame.transform.rotate(self.__image, self.direction.angle_to(normal))
