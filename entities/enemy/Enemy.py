from abc import ABCMeta, abstractmethod
from entities.ColiableEntity import ColiableEntity
from entities.Entity import Entity

class Enemy(ColiableEntity, metaclass=ABCMeta):

    def __init__(self, target: Entity, *args, **kwargs):
        self.__target = target
        super().__init__(*args, **kwargs)

    def update(self):
        tPos = self.getTargetPosition()
        super().update()


    def getTargetPosition(tPos) -> tuple[int, int]:
        return (0,1)

        