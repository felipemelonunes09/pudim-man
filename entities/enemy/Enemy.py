from abc import ABCMeta, abstractmethod
import random
from entities.ColiableEntity import ColiableEntity
from entities.Entity import Entity
from scenes.Tile import Tile
from utils.helpers import Direction
from config import globals
import math

class Enemy(ColiableEntity, metaclass=ABCMeta):

    def __init__(self, target: Entity, mapData: list[list[int]], *args, **kwargs):
        self.__target = target
        super().__init__(*args, **kwargs)

    def update(self):        
        self.move(self.direction)
        super().update()
       

    # consider moving this to a general helper module
    def getAbsolutePosition(self) -> tuple[int, int]:
        return (self.rect.x // globals.BLOCK_SIZE) + 1, (self.rect.y // globals.BLOCK_SIZE) + 1
    
    # consider moving this to a general helper module
    def getMapPosition(self) -> tuple[int, int]:
        
        return ((self.rect.x / globals.BLOCK_SIZE) + 1, (self.rect.y / globals.BLOCK_SIZE) + 1)
    # consider moving this to a general helper module
    def getTargetAbsolutePosition(self) -> tuple[int, int]:
        return ((self.__target.lastX // globals.BLOCK_SIZE)+1,(self.__target.lastY // globals.BLOCK_SIZE)+1)

    def onCollision(self, entity):
        from entities.Player import Player
        if isinstance(entity, Player) and entity.IsPowered():
            self.kill()
        if isinstance(entity, Tile):
            direction = random.randint(0, 3)
            match direction:
                case Direction.LEFT.value:
                    self.direction = Direction.LEFT
                case Direction.RIGHT.value:
                    self.direction = Direction.RIGHT
                case Direction.UP.value:
                    self.direction = Direction.UP
                case Direction.DOWN.value:
                    self.direction = Direction.DOWN
            
        return super().onCollision(entity)