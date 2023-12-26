from abc import ABCMeta, abstractmethod

class IDamageObject(metaclass=ABCMeta):

    @abstractmethod
    def get_damage(self):
        pass