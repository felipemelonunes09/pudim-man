from abc import ABCMeta, abstractmethod
from random import uniform

from traitlets import Any

class Event():

    def __init__(self, obj) -> None:
        self.obj = obj

    def __call__(self) -> Any:
        if(self.trigger()):
            self.call()
    
    @abstractmethod
    def call(self) -> None:
        pass

    @abstractmethod
    def trigger(self, probability) -> bool:
        return (uniform(0, 1) < probability)