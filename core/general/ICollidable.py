

from abc import ABCMeta, abstractmethod


class ICollidable(metaclass=ABCMeta):

    @abstractmethod
    def collide(self, collision_object: object):
        pass

