from core.general.IDamageObject import IDamageObject
from core.objects.ship.room.room import Room, TYPE, ROOM_LIFE

## class that is used to "produce" movement

class MotorRoom(Room):
    def __init__(self, power_required: float, motors: list) -> None:
        self.motors = motors
        super().__init__(TYPE['MOTOR'], ROOM_LIFE, power_required)

    def use(self) -> int:

        propulsion = 0
        for motor in self.motors:
            propulsion += motor.use()

        return propulsion

    def damage(self, obj: IDamageObject):
        return super().damage(obj)

    def repair(self):
        return super().repair()
    
    def acelerate_all_motors(self, using: int):
        for motor in self.motors:
            motor.acelerate(using)

    def acelerate_one(self, using: int, indice: int):
        self.motors[indice].acelerate(using)
