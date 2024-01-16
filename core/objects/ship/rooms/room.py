
from core.general.IDamageable import IDamageable
from core.general.IRepairable import IRepairable


ROOM_TYPE = {
    "POWER": 1
}

class IRoom(IDamageable, IRepairable):
    pass

class Room():

    def __init__(self, type) -> None:

        self.life = 100
        self.power_required = 0.01
        self.type = type
    
