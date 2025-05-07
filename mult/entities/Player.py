import pygame
from config.sprites import Sprites
from entities.ColiableEntity import ColiableEntity
from entities.enemy.Enemy import Enemy
from utils.helpers import Direction

class Player(ColiableEntity):
    def __init__(self, *args, **kwargs):
        self.__isPowered            = False
        self.__powerDuration        = 10000
        self.__remainingPowertime   = 0
        self.__powerStart           = None
        self.__alive                = True
        super().__init__(
            walkRight   = Sprites.Pudim.walkRight,
            walkLeft    = Sprites.Pudim.walkLeft,
            walkUp      = Sprites.Pudim.walkUp,
            walkDown    = Sprites.Pudim.walkDown,
            *args, 
            **kwargs
        )

    def isAlive(self) -> bool:
        return self.__alive

    def IsPowered(self) -> bool:
        return self.__isPowered
    
    def getPowerDuration(self) -> int:
        return self.__powerDuration
    
    def getRemainingPowerTime(self) -> int:
        return self.__remainingPowertime
    
    def setIsPowered(self, powered: bool) -> None:
        self.__isPowered = powered
        self.__powerStart = pygame.time.get_ticks() if powered else None

    # refact
    def update(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        if self.__isPowered:
            elapsedTime = pygame.time.get_ticks() - self.__powerStart
            self.__remainingPowertime = max(0, (self.__powerDuration - elapsedTime) // 1000)
            if elapsedTime >= self.__powerDuration:
                self.setIsPowered(False)
        self.move(self.direction)
        return super().update()
    
        
    def onCollision(self, entity):
        if isinstance(entity, Enemy) and not self.IsPowered():
            self.__alive = False
            self.kill()
        return super().onCollision(entity)