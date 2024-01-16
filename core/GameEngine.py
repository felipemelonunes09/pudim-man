import pygame

from setting import *
from core.Player import *
from core.Camera import *
from core.general.ICollidable import *

from core.hud.Hud import *

from core.objects.ship.BaseEnemy import BaseEnemy
from core.objects.TestObject import TestObject

class GameEngine:
    
    groups = {}

    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT ))
        self.clock = pygame.time.Clock()

        self.running = False

        
        self.camera = Camera()
        self.hud = Hud()
        GameEngine.set_groups(SPRITE_GROUPS)
        

    def start(self) -> None:
        
        TestObject((0, 0, 255), (150, 150), 50, 50, self.camera)
        self.player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2), self.camera) 
        enemy =  BaseEnemy((SCREEN_WIDTH/2,SCREEN_HEIGHT/2), self.camera)

        self.running = True
        
        self.hud.set_player(self.player)

        while self.running:     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill('black')

            self.camera.update()
            self.hud.update()

            self.camera.draw(target=self.player)
            self.hud.draw()
            
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
            