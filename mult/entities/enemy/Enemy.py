from abc import ABCMeta, abstractmethod
import random
from typing import List, Tuple
from entities.ColiableEntity import ColiableEntity
from entities.Entity import Entity
from scenes.Tile import Tile
from utils.helpers import Direction
from config import globals
import math

class Enemy(ColiableEntity, metaclass=ABCMeta):

    def __init__(self, target: Entity, mapData: List[List[int]], *args, **kwargs):
        self.__target = target
        self.__currentDirectionVector = Direction.RIGHT
        super().__init__(*args, **kwargs)

    def update(self):        
        self.move(self.direction)
        super().update()
       
    # consider moving this to a general helper module
    def getAbsolutePosition(self) -> Tuple[int, int]:
        return (self.rect.x // globals.BLOCK_SIZE) + 1, (self.rect.y // globals.BLOCK_SIZE) + 1
    
    # consider moving this to a general helper module
    def getMapPosition(self) -> Tuple[int, int]:
        return ((self.rect.x / globals.BLOCK_SIZE) + 1, (self.rect.y / globals.BLOCK_SIZE) + 1)
    
    # consider moving this to a general helper module
    def getTargetAbsolutePosition(self) -> Tuple[int, int]:
        return ((self.__target.lastX // globals.BLOCK_SIZE) + 1, (self.__target.lastY // globals.BLOCK_SIZE) + 1)

    def onCollision(self, entity):
        from entities.Player import Player
        if isinstance(entity, Player) and entity.IsPowered():
            self.kill()
        if isinstance(entity, Tile):
            direction = random.randint(0, 3)
            if direction == Direction.LEFT.value:
                self.direction = Direction.LEFT
            elif direction == Direction.RIGHT.value:
                self.direction = Direction.RIGHT
            elif direction == Direction.UP.value:
                self.direction = Direction.UP
            elif direction == Direction.DOWN.value:
                self.direction = Direction.DOWN
            
        return super().onCollision(entity)
