from core.general.IDamageObject import IDamageObject
from core.general.IDamageable import IDamageable
from core.objects.attack.PrimaryShot import PrimaryShot
from core.objects.attack.Shot import Shot
from core.objects.ship.BaseShipEngine import BaseShipEngine
from core.objects.ship.rooms.power_room.PowerRoom import PowerRoom
from core.objects.ship.objects.Generator import Generator
from core.general.utils.Cooldown import Cooldown

## should damageable and reaperable
class Ship(BaseShipEngine, IDamageable):
    
    def __init__(self, position: tuple, group: object,sprite: str) -> None:
        
        super().__init__(position, group, sprite)

        # not oficial implementation
        self.shoot = Cooldown(200, self.shoot, None)
        
        self.power_room = PowerRoom(generators=[
            Generator(),
            Generator(),
            Generator(),
            Generator()
        ])
        
    def update(self, *a, **k):
        
        self.power_room.generate_power()
        
        super().update(a, k)

    def get_speed(self) -> float:
        return 2
    
    def acelerate_all(self, aceleration):
        pass

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