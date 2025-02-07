from abc import ABCMeta, abstractmethod
from entities.ColiableEntity import ColiableEntity
from entities.Entity import Entity
from utils.helpers import Direction

class Enemy(ColiableEntity, metaclass=ABCMeta):

    def __init__(self, target: Entity, *args, **kwargs):
        self.__target = target
        super().__init__(*args, **kwargs)

    def update(self):
        
        tPos = self.getTargetPosition()

        if tPos[0] > self.rect.x:
            self.move(Direction.RIGHT)
        elif tPos[0] < self.rect.x:
            self.move(Direction.LEFT)
        elif tPos[1] > self.rect.y:
            self.move(Direction.DOWN)
        else:
            self.move(Direction.UP)

        super().update()

    def getTargetPosition(self) -> tuple[int, int]:
        return (self.__target.lastX,self.__target.lastY)

        