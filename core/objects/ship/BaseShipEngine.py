from abc import abstractmethod
from core.general.ICollidable import ICollidable
from core.objects.SceneObject import SceneObject
from core.GameProxy import GameProxy

import pygame

class BaseShipEngine(SceneObject, ICollidable):

    def __init__(self, position: tuple, group: object, sprite: str) -> None:
        super().__init__(position, group, sprite)

        self.direction = pygame.math.Vector2()
        self.normal = self.direction.copy()

        self.__image = self.image

        ## temporary by this values comes from __ship
        ## direction should awalys be -1
        self.direction.y = -1

        self.last_shot = None
        self.life = 100

        GameProxy.add_sprite_group(self, ICollidable.__name__)

    def update(self, *args, **kwargs):

        ## remove this on feature
        if self.life <= 0:
            self.kill()

        self.rect.center += self.direction * self.get_speed()
        self.image = pygame.transform.rotate(self.__image, self.direction.angle_to( self.normal ))
    
    def collide(self, collision_object: object):
        ## global collide  method
        pass

    @abstractmethod
    def get_speed(self) -> float:
        pass

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def events():
        pass