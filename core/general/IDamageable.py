from abc import ABCMeta, abstractmethod

from core.general.IDamageObject import IDamageObject

class IDamageable(metaclass=ABCMeta):

    @abstractmethod
    def damage(self, obj: IDamageObject):
        pass