

from core.objects.ship.attack.IShot import IShot


class Shot(IShot):

    def __init__(self, speed: float, damage: float, direction: tuple, shooter: object) -> None:

        self.speed = speed
        self.damage = damage
        self.direction = direction
        self.shooter = id(shooter)
        
    def collide(self, collision_object: object):
        
        if id(collision_object) != self.shooter:
            self.destroy()