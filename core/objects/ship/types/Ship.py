from core.general.IDamageObject import IDamageObject
from core.general.IDamageable import IDamageable
from core.objects.attack.PrimaryShot import PrimaryShot
from core.objects.attack.Shot import Shot
from core.objects.ship.BaseShipEngine import BaseShipEngine
from core.objects.ship.room.motor_room.MotorRoom import MotorRoom
from core.objects.ship.room.motor_room.motor import Motor
from core.utils.Cooldown import Cooldown

class Ship(BaseShipEngine, IDamageable):
    
    def __init__(self, position: tuple, group: object,sprite: str) -> None:
        
        super().__init__(position, group, sprite)

        # will be outside the class on be definied on a factory method
        self.motorRoom = MotorRoom(
            power_required=0.01, motors=[
                Motor(),
                Motor(),
                Motor(),
                Motor()
            ]
        )

        self.rooms = [
            self.motorRoom
        ]

        # not oficial implementation
        self.shoot = Cooldown(200, self.shoot, None)
        self.motorRoom.set_using_all_motors(1)


    def get_speed(self) -> float:
        return self.motorRoom.use()
    
    def acelerate_all(self, aceleration):
        current_aceleration = self.motorRoom.get_avarage_using()
        current_aceleration += (aceleration/100)
        self.motorRoom.set_using_all_motors(current_aceleration)

    ## not oficical implementation
    def collide(self, collision_object: object):
        if collision_object is not self.last_shot:
            return
        
    ## not oficical implementation
    def damage(self, damage_object: IDamageObject):
        total_damage = damage_object.get_damage()
        ## routine in case its a shot
        if isinstance(damage_object, Shot):
            return 
            self.life -= total_damage


    ## not oficial implementation 
    def shoot(self, direction: tuple):
        self.last_shot = PrimaryShot(
            speed=30,
            damage=10,
            position=self.rect.center,
            direction=direction,
            group=self.group,
            shooter=self
        )