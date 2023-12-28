
from abc import ABCMeta, abstractmethod

class IRepairable(metaclass=ABCMeta):

    @abstractmethod
    def repair(self):
        pass

