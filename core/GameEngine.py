import pygame

from setting import *
from core.Player import *
from core.Camera import *
from core.general.ICollidable import *

from core.objects.ship.BaseEnemy import BaseEnemy
from core.objects.TestObject import TestObject
from core import GameProxy


class GameEngine:

    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT ))
        self.clock = pygame.time.Clock()

        self.running = False
        self.camera = Camera()

        GameEngine.set_groups(SPRITE_GROUPS)
        

    def start(self) -> None:

        self.running = True

        TestObject((0, 0, 255), (150, 150), 50, 50, self.camera)
        self.player = Player((SCREEN_HEIGHT/2, SCREEN_WIDTH/2), self.camera, None) 
        enemy =  BaseEnemy((SCREEN_HEIGHT/2, SCREEN_WIDTH/2), self.camera, None)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill('black')

            self.camera.update()
            self.camera.draw(target=self.player)

            self.handle_colision()

            self.clock.tick(FRAME_RATE)
            pygame.display.flip()

        pygame.quit()

    def handle_colision(self):
        global_colisions = pygame.sprite.groupcollide(
            groupa=GameEngine.groups[ICollidable.__name__],
            groupb=GameEngine.groups[ICollidable.__name__],
            dokilla=False,
            dokillb=False,
        )

        ## maybe need an to optmize ## review
        for obj in global_colisions:
            if (isinstance(obj, ICollidable)):
                for collision_object in global_colisions[obj]:
                    if collision_object is not obj:
                        obj.collide( collision_object )            

    @classmethod
    def set_groups(cls, group_list): 
        cls.groups = {}
        for group in group_list:
            cls.groups[group] = pygame.sprite.Group()
            