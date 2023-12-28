from abc import ABCMeta, abstractmethod

from core.general.IDamageable import IDamageable
from core.general.IRepairable import IRepairable


TYPE = {
    "BRIDGE":       1,
    "ENGINE":       2,
    "MOTOR":        3,
    "ELETRICAL":    4,
    "STORAGE":      3,
    "IDLE":         4
}

ROOM_LIFE = 100

class IRoom(IDamageable, IRepairable, metaclass=ABCMeta):
    
    @abstractmethod
    def is_active(self):
        pass


class Room(IRoom):
    
    def __init__(self, type: int, life: float, power_required: float) -> None:
        
        if (life or power_required) <= 0:
            raise ValueError("Life or power_required atribute has to be higher than 0")

        self.life = life
        self.power_required = power_required
        self.critical = True
        self.active = True

    def is_active(self):
        return self.active