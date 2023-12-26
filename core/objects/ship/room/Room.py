from abc import ABCMeta, abstractmethod

from core.general.IDamageable import IDamageable

class IRoom(IDamageable, metaclass=ABCMeta):
    pass

type = {
    "BRIDGE":       1,
    "ENGINE":       2,
    "MOTOR":        3,
    "ELETRICAL":    4,
    "STORAGE":      3,
    "IDLE":         4
}

class Room(IRoom):
    
    def __init__(self, type: int, life: float, power_required: float) -> None:
        
        if (life or property) <= 0:
            raise ValueError("Life atribute has to be higher than 0")
        

        self.life = life
        self.power_required = power_required
        self.critical = True