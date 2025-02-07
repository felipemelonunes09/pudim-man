from abc import ABCMeta, abstractmethod
from entities.ColiableEntity import ColiableEntity
from entities.Entity import Entity
from utils.helpers import Direction
from typing import TYPE_CHECKING

class Enemy(ColiableEntity, metaclass=ABCMeta):

    def __init__(self, target: Entity, *args, **kwargs):
        self.__target = target
        self.__currentDirectionVector = Direction.RIGHT
        super().__init__(*args, **kwargs)

    def update(self):
        super().update()

        tPos = self.getTargetPosition()
        self.move(self.__currentDirectionVector)

    def getTargetPosition(self) -> tuple[int, int]:
        return (self.__target.lastX,self.__target.lastY)

    def onCollision(self, entity):
        from entities.Player import Player
        if isinstance(entity, Player) and entity.IsPowered():
            self.kill()
        return super().onCollision(entity)
    
    def changeDirectionVector(self, tPos: tuple[int, int], excludeDirection: Direction = None) -> None:
        #print(f"should go to the right {tPos[0] > self.rect.x and Direction.RIGHT != excludeDirection}")
        #print(f"should go to the left {tPos[0] < self.rect.x and Direction.LEFT != excludeDirection}")
        #print(f"should go to the down {tPos[1] > self.rect.y and Direction.DOWN != excludeDirection}")
        #print(f"should go to the up {tPos[1] < self.rect.y and Direction.UP != excludeDirection}")
        #print(f"excluded position {excludeDirection}")
        #print("=================================")
        pass
        