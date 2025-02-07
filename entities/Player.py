import pygame
from config.sprites import Sprites
from entities.ColiableEntity import ColiableEntity
from utils.helpers import Direction

class Player(ColiableEntity):
    def __init__(self, *args, **kwargs):
        self.__isPowered = False
        super().__init__(
            walkRight   = Sprites.Pudim.walkRight,
            walkLeft    = Sprites.Pudim.walkLeft,
            walkUp      = Sprites.Pudim.walkUp,
            walkDown    = Sprites.Pudim.walkDown,
            *args, 
            **kwargs
        )

    def getIsPowered(self) -> bool:
        return self.__isPowered
    
    def setIsPowered(self, powered: bool) -> None:
        self.__isPowered = powered

    def update(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        return super().update()
    
    def move(self, keys: pygame.key.ScancodeWrapper):
        if keys[pygame.K_LEFT]:
            return super().move(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            return super().move(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            return super().move(Direction.UP)
        elif keys[pygame.K_DOWN]:
            return super().move(Direction.DOWN)
        