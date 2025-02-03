from abc import abstractmethod

class IColiable():
    @abstractmethod
    def onCollision(self, entity):
        pass