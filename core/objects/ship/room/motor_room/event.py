from abc import ABCMeta, abstractmethod

from traitlets import Any
from random import uniform


class MotorEvent(metaclass=ABCMeta):

    def __init__(self, motor) -> None:
        self.motor = motor

    def __call__(self) -> Any:
        if(self.trigger()):
            self.call()
    
    @abstractmethod
    def call(self) -> None:
        pass

    @abstractmethod
    def trigger(self, final_probility) -> bool:
        return (uniform(0, 1) < final_probility)

"""
[MECHANICAL BREAK LOW EVENT]

-> happens on 
    [probability 1] it can happen at any times with a probability on 0.1% propability pern turn
    [probability 2] if effiency is lower than 0.2 it can with a probality of 0.03% pern turn
    [probability 3] if heat is above 0.9 it can happen with a probability of 0.05% per turn 
-> it takes
    it only reduces the effiency of the machine by 0.1% per event

-> desire proporsion
    at 100 updates -> 1 event
"""

class MechanicalBreakLowEvent(MotorEvent):

    def __init__(self, motor) -> None:
        super().__init__(motor)

        self.__effiency_trigger_1 = 0.2
        self.__heat_trigger_1 = 0.9

        self.__probability_1 = 0.001
        self.__probability_2 = 0.003
        self.__probability_3 = 0.005

        self.__take_away_effiency = 0.001
    
    def trigger(self) -> bool:

        final = self.__probability_1
        if (self.motor.eficiency < self.__effiency_trigger_1):
            final = self.__probability_2
        
        if (self.motor.heat > self.__heat_trigger_1):
            final += self.__probability_3

        return super().trigger(final)
        
    def call(self) -> None:
        self.motor.eficiency -= self.__take_away_effiency
        
        

    
