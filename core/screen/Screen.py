from abc import ABCMeta, abstractmethod
import pygame

from core.StateManager import StateManager

class ScreenEvents():
    CONTEXT_CHANGE=1

class IScreen(metaclass=ABCMeta):
    @abstractmethod
    def update(self, screen: pygame.Surface) -> None:
        pass

    @abstractmethod
    def getEvents() -> list[object]:
        pass

    @abstractmethod
    def getSurface(self) -> pygame.Surface:
        pass

class Screen(IScreen):
    def __init__(self, static: bool = False, initialState=StateManager.State.DEFAULT) -> None:
        self.__events = []
        self.__static = static
        self.hello = "hello world"
        self.state = StateManager(initialState)
        self.__surface = self.getSurface()

    def addEvent(self, event: object) -> None:
        self.__events.append(event)
    
    def getEvents(self) -> list[object]:
        return self.__events
    
    def update(self, screen):
        if not self.__static:
            self.__surface = self.getSurface()
        screen.blit(self.__surface, (0, 0))