from abc import ABCMeta, abstractmethod
import math
from core.Map import Map
from entities.ColiableEntity import ColiableEntity
from entities.Entity import Entity
from utils.helpers import Direction
from config import globals
import pygame
import math

class Enemy(ColiableEntity, metaclass=ABCMeta):

    def __init__(self, target: Entity, mapData: list[list[int]], *args, **kwargs):
        self.__target = target
        self.__mapData = mapData
        self.__patience = 0
        self.__patienceReset = globals.BLOCK_SIZE // 2 ## it will commit with tha half of the block size to move
        super().__init__(*args, **kwargs)

    def update(self):
        
        if self.__patience <= 0:
            
            self.direction = Direction.RIGHT
            x, y = self.getAbsolutePosition()
            mx, my = self.getMapPosition()
            tx, ty = self.getTargetAbsolutePosition()
            
            print(self.__mapData[y])
            previewRight  = self.__mapData[y][x + 1]
            previewLeft   = self.__mapData[y][x-1]
            previewUp    = self.__mapData[y - 1][x]
            previewDown   = self.__mapData[y + 1][x]
            
            if tx > mx:
                self.direction = Direction.RIGHT
                if previewRight == Map.Objects.TILE.value:
                    self.changeDirection((previewDown, Direction.DOWN), (previewUp, Direction.UP), (previewLeft, Direction.LEFT))
            if tx < x:
                self.direction = Direction.LEFT
                if previewLeft == Map.Objects.TILE.value:
                    self.changeDirection((previewDown, Direction.DOWN), (previewUp, Direction.UP), (previewRight, Direction.RIGHT))
            if ty > y:
                self.direction = Direction.DOWN
                if previewDown == Map.Objects.TILE.value:
                    self.changeDirection((previewRight, Direction.RIGHT), (previewLeft, Direction.LEFT), (previewUp, Direction.UP))
            if ty < y:
                self.direction = Direction.UP
                if previewUp == Map.Objects.TILE.value:
                    self.changeDirection((previewRight, Direction.RIGHT), (previewLeft, Direction.LEFT), (previewDown, Direction.DOWN))
            self.__patience = self.__patienceReset
        self.move(self.direction)
        self.__patience -= 1
        super().update()
        
    
    def changeDirection(self, preview1: tuple[int, Direction], preview2: tuple[int, Direction], preview3: tuple[int, Direction]):
        if preview1[0] != Map.Objects.TILE.value:
            self.direction = preview1[1]
        elif preview2[0] == Map.Objects.TILE.value:
            self.direction = preview2[1]
        elif preview3[0] == Map.Objects.TILE.value: 
            self.direction = preview3[1]
        
    
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
        return super().onCollision(entity)