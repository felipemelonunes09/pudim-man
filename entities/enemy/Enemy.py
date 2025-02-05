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

        self.move(Direction.RIGHT) if tPos[0] > self.lastX else self.move(Direction.LEFT)
        self.move(Direction.DOWN) if tPos[1] > self.lastY else self.move(Direction.UP)

        if tPos[1] > self.lastY:
            self.move
        super().update()

    def getTargetPosition(self) -> tuple[int, int]:
        return (self.__target.lastX,self.__target.lastY)

        