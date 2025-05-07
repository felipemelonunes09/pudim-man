
from abc import ABCMeta, abstractmethod
from core.input.Event import Event
import pygame

class IInputHandler(metaclass=ABCMeta):

    @abstractmethod
    def translateEvent(self, event: pygame.event) -> Event:
        pass
    

