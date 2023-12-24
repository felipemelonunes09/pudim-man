

from abc import abstractmethod
import pygame
from core.objects.IObject import IObject

class Object(pygame.sprite.Sprite, IObject):

    def __init__(self, group: any) -> None:
        super().__init__(group)

    @abstractmethod
    def update(self, *args, **kwargs):
        pass