from typing import Any
import pygame
from core.general.ICollidable import ICollidable
from core.objects.IObject import IObject
from core.GameProxy import GameProxy
from core.objects.SceneObject import SceneObject


class TestObject(pygame.sprite.Sprite, IObject, ICollidable):
    
    def __init__(self, color, position, width, height, group: object) -> None:

        super().__init__(group)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect(center=position)

        GameProxy.add_sprite_group(self, ICollidable.__name__)
        GameProxy.add_sprite_group(self, SceneObject.__name__)


    def update(self, *args: Any, **kwargs: Any) -> None:
        return super().update(*args, **kwargs)

    def collide(self, collision_object: object):
        print("collided")
    