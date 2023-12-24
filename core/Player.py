import pygame
from core.objects.SceneObject import SceneObject
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
from core.objects.ship.BaseShipEngine import BaseShipEngine
from setting import *

class Player(BaseShipEngine):
    
    def __init__(self, position, camera, ship) -> None:

        super().__init__(position, camera, 'graphics/ship1.png', ship)
        self.normal = self.direction.copy()
        


    def update(self, *args, **kargs) -> None:

        pressed_keys = pygame.key.get_pressed()

        self.move(pressed_keys)
        self.events()
        super().update()


    def move(self, pressed_keys):

        if pressed_keys[K_RIGHT]:
            self.direction = self.direction.rotate(2)

        if pressed_keys[K_LEFT]:
            self.direction = self.direction.rotate(-2)

    def events(self):

        clicked = pygame.mouse.get_pressed()
        if (clicked[0]):

            pos = pygame.mouse.get_pos()
            pos = (pos[0] - self.position[0], pos[1] - self.position[1])
            
            obj = self.shoot(pos)
