from core.general.IDamageable import IDamageable
from core.objects.attack.IShot import IShot

class Shot(IShot):

    def __init__(self, speed: float, damage: float, direction: tuple, shooter: object) -> None:

        self.speed = speed
        self.damage = damage
        self.direction = direction
        self.shooter = id(shooter)
        
    def collide(self, collision_object: object):

        if id(collision_object) != self.shooter:
            self.destroy()

        if isinstance(collision_object, IDamageable):
            collision_object.damage(self)

    def get_damage(self):
        return self.damage
        