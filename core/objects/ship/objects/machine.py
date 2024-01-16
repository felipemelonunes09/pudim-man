

from abc import ABCMeta, abstractmethod

from core.general.IDamageable import IDamageable
from core.general.IRepairable import IRepairable
from core.general.IDamageObject import IDamageObject


from core.objects.ship.objects.events.common_events import COMMON_EVENTS_DICT
from core.general.error.error_messages import ALL_PARAMETER_MUST_BE_GREATER_THAN_0

from core.general.utils.Cooldown import Cooldown

class IMachine(IDamageable, IRepairable, metaclass=ABCMeta):

    @abstractmethod
    def resfriate(self):
        pass

    @abstractmethod
    def heatup(self):
        pass

    @abstractmethod
    def work(self) -> float:
        pass

    @abstractmethod
    def gain_function() -> float:
        pass


class Machine(IMachine):

    def __init__(
        self,
        gain = 1,
        efficiency_loss = 0.01,
        heat_gain = 0.01,
        heat_loss = 0.2,
        repair_gain = 0.2,
        max_usage = 1.02,
        work_cooldown=((100*10) * 64) # 1 min
    ) -> None:

        if ((gain or efficiency_loss or heat_gain or heat_loss or repair_gain or max_usage) <= 0):
            raise ValueError(ALL_PARAMETER_MUST_BE_GREATER_THAN_0)

        self.life = 1
        self.efficiency = 1
        self.usage = 0
        self.heat = 0

        self.efficiency_loss = efficiency_loss
        self.heat_gain = heat_gain
        self.heat_loss = heat_loss
        self.repair_gain = repair_gain
        self.gain = gain
        self.max_usage = max_usage

        self.active = False
        self.on_fire = False
        
        self.events = COMMON_EVENTS_DICT
        
        self.work = Cooldown(work_cooldown, self.work, self.gain_function_checkers)
        
        
    def repair(self):
        self.heat = 0
        self.life = 100
        self.efficiency = 1 + self.repair_gain
        
    def damage(self, obj: IDamageObject):
        pass

    def increase_usage(self, value: float):
        pre = self.usage + value
        if (pre <= self.max_usage):
            self.usage = pre

    def decrease_usage(self, value: float):
        pre = self.usage - value
        if (pre >= 0):
            self.usage = pre
        
    def activate(self):
        self.active = True

    def deactivate(self):
        self.activate = False

    def heatup(self):
        pre = self.heat + self.heat_gain
        if pre < 1:
            self.heat = pre
        else:
            self.heat = 1

    def resfriate(self):
        pre = self.heat - self.heat_loss
        if pre > 0:
            self.heat = pre
        else:
            self.heat = 0

    def work(self) -> float:

        if (self.active) and (self.heat < 1) and (self.life > 0) :
                        
            work = self.gain_function() * self.efficiency * self.usage
            self.efficiency -= self.efficiency_loss
            self.heatup()
            self.event()

            return work
        
        return 0
    
    def gain_function_checkers(self):
        if (self.active) and (self.heat < 1) and (self.life > 0):
            return self.gain_function() * self.efficiency * self.usage
        else:
            return 0
    
    def event(self):
        for k in self.events:
            ## make the call
            self.events[k]


