import pygame
from abc import abstractmethod, ABCMeta

class IObject(metaclass=ABCMeta):

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
        
