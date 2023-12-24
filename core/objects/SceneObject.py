from abc import abstractmethod
from core.objects.IObject import IObject
from core.GameProxy import GameProxy


import pygame

class SceneObject(pygame.sprite.Sprite, IObject): 

    def __init__(self, position: tuple, group: object, sprite: str) -> None:

        super().__init__(group)

        self.group = group
        
        self.position = position
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=position)

        GameProxy.add_sprite_group(self, SceneObject.__name__)



    @staticmethod
    def add_sprite_group(scene_object: pygame.sprite.Sprite, group_flag: str):
        if isinstance(scene_object, SceneObject):
            GameProxy.add_sprite_group(scene_object, group_flag)


    @abstractmethod
    def update(self, *args, **kwargs):
        pass
        
