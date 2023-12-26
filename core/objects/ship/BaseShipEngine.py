from abc import abstractmethod
from core.general.ICollidable import ICollidable
from core.general.IDamageObject import IDamageObject
from core.general.IDamageable import IDamageable
from core.objects.SceneObject import SceneObject
from core.objects.attack.PrimaryShot import PrimaryShot
from core.objects.attack.Shot import Shot
from core.utils.Cooldown import Cooldown
from core.GameProxy import GameProxy

import pygame

class BaseShipEngine(SceneObject, ICollidable, IDamageable):

    def __init__(self, position: tuple, group: object, sprite: str, ship: object) -> None:
        super().__init__(position, group, sprite)


        self.direction = pygame.math.Vector2()
        self.normal = self.direction.copy()

        self.__image = self.image
        self.__ship = ship

        ## temporary by this values comes from __ship
        ## direction should awalys be -1
        self.direction.y = -1
        self.speed = 2

        self.shoot = Cooldown(200, self.shoot, None)
        self.last_shot = None
        self.life = 100

        GameProxy.add_sprite_group(self, ICollidable.__name__)

    def update(self, *args, **kwargs):
        
        if self.life <= 0:
            self.kill()

        self.rect.center += self.direction * self.speed
        self.image = pygame.transform.rotate(self.__image, self.direction.angle_to( self.normal ))

    def shoot(self, direction: tuple):
        self.last_shot = PrimaryShot(
            speed=30,
            damage=10,
            position=self.rect.center,
            direction=direction,
            group=self.group,
            shooter=self
        )
    
    def collide(self, collision_object: object):
        if collision_object is not self.last_shot:
            if isinstance(collision_object, PrimaryShot):
                self.life -= 50
    
    def damage(self, damage_object: IDamageObject):

        total_damage = damage_object.get_damage()

        ## routine in case its a shot
        if isinstance(damage_object, Shot):
            self.life -= total_damage

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def events():
        pass