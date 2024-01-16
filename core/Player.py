import pygame
from core.objects.SceneObject import SceneObject
from core.objects.ship.types.Ship import Ship
from setting import *
from pygame.locals import K_RIGHT, K_LEFT, K_0, K_9

class Player(Ship):
    
    def __init__(self, position, camera) -> None:

        super().__init__(position, camera, 'graphics/ship1.png')
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
            
        if pressed_keys[K_0]:
            self.power_room.activate_all_generator()
        
        if pressed_keys[K_9]:
            self.power_room.increase_all_generator_usage(1)

    def events(self):

        clicked = pygame.mouse.get_pressed()
        if (clicked[0]):

            pos = pygame.mouse.get_pos()
            pos = (pos[0] - self.position[0], pos[1] - self.position[1])
            
            obj = self.shoot(pos)

