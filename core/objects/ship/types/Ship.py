from core.general.IDamageObject import IDamageObject
from core.general.IDamageable import IDamageable
from core.objects.attack.PrimaryShot import PrimaryShot
from core.objects.attack.Shot import Shot
from core.objects.ship.BaseShipEngine import BaseShipEngine
from core.utils.Cooldown import Cooldown

class Ship(BaseShipEngine, IDamageable):
    
    def __init__(
            self, 
            position: tuple, 
            group: object,
            sprite: str 
        ) -> None:
        
        super().__init__(position, group, sprite)
        self.rooms = [
            
        ]

        # not oficial implementation
        self.shoot = Cooldown(200, self.shoot, None)

    def collide(self, collision_object: object):
        if collision_object is not self.last_shot:
            if isinstance(collision_object, PrimaryShot):
                self.life -= 50

    def damage(self, damage_object: IDamageObject):

        total_damage = damage_object.get_damage()

        ## routine in case its a shot
        if isinstance(damage_object, Shot):
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