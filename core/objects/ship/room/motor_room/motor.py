from typing import Any

from abc import abstractmethod, ABCMeta
from core.general.IDamageObject import IDamageObject

from core.general.IDamageable import IDamageable
from core.general.IRepairable import IRepairable
from core.objects.ship.room.motor_room.event import MechanicalBreakLowEvent


class IMotor(IDamageable, IRepairable, metaclass=ABCMeta):

    @abstractmethod 
    def use(self):
        pass

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

class Motor(IMotor):

    def __init__(
            self, 
            life = 100, 
            eficiency_loss = 0.001, 
            propulsion_gain = 0.2,
            max_use = 1.5,
            repair_bonus = 0.1,
            heat_gain = 0.001,
            heat_loss = 0.02
        ) -> None:

        if (life or eficiency_loss or propulsion_gain or max_use or repair_bonus or heat_gain) <= 0:
            raise ValueError("atribute has to be higher than 0")

        self.eficiency_loss = eficiency_loss
        self.life = life
        self.max_use = max_use
        self.propulsion_gain = propulsion_gain
        self.repair_bonus = repair_bonus
        self.heat_gain = heat_gain
        self.heat_loss = heat_loss

        self.events = {
            "MECHANICAL_BREAK_LOW": MechanicalBreakLowEvent(self),
        }

        self.eficiency = 1
        self.using = 0
        self.heat = 0

        self.active = True
        super().__init__()

    def activate(self):
        self.active = True

    def deactivate(self):
        self.use = 0
        self.deactivate = False

    def use(self) -> int:

        if self.activate:

            self.eficiency -= self.eficiency_loss
            self.__events()

            if self.eficiency <= 0:
                self.eficiency = 0
                return self.eficiency 

            self.heat += self.heat_gain * self.using
            propulsion = self.propulsion_gain * self.eficiency * self.using


            return propulsion
        return 0
        
    def damage(self, obj: IDamageObject):
        return super().damage(obj)
    
    def repair(self):
        self.eficiency = (1 + self.repair_bonus)
        self.heat = 0
        return super().repair()
    
    def resfriate(self):
        self.heat -= self.heat_loss
    
    def __events(self):
        for event in self.events:
            self.events[event]()

    def acelerate(self, using: int):
        if (using < 0):
            raise ValueError("using can not be negative")
        
        self.using = using
        pass

    def deacelerate(self, using: int):
        if (using < 0):
            raise ValueError("using can not be negative")
        self.using = using
        pass


def motor_factory():
    raise Exception("method not implemented")


    

