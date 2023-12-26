

from core.general.ICollidable import ICollidable
from core.objects.SceneObject import SceneObject
from core.objects.attack.Shot import Shot

import pygame

class SpriteShot(SceneObject, Shot):
    def __init__(self, speed: float, damage: float, position: any, direction: tuple, group: any, shooter: object, sprite: str) -> None:
        
        super().__init__(position, group, sprite)
        Shot.__init__(self, speed, damage, direction, shooter)

        self.direction = pygame.math.Vector2(self.direction[0], self.direction[1]).normalize()
        
        SceneObject.add_sprite_group(self, Shot.__name__)
        SceneObject.add_sprite_group(self, ICollidable.__name__)

    def update(self, *args, **kwargs):
        self.rect.center += self.direction * self.speed

    def destroy(self):
        self.kill()
        

        

