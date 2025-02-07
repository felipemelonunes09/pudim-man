import json
import pygame
from config import globals
from core.Map import Map
from core.IColiable import IColiable
from core.StateManager import StateManager
from core.QuestionTrial import QuestionTrial
from entities.Player import Player
from entities.enemy.Pan import Pan
from entities.enemy.Jelly import Jelly
from scenes.Point import QuestionPoint
from enum import Enum

class Engine:
    class EnemiesMap(Enum):
        PAN     = 0
        JELLY   = 1
    class Display:
        def __init__(self, font: str, size: int, anchorX: int):
            self.font   = pygame.font.SysFont(font, size)
            self.offset = 20 
            self.anchorX = anchorX
            self.updatePointText(0)

        def updatePointText(self, number: int) -> None:
            self.pointText = self.font.render(f"Points: {number}", True, globals.TEXT_COLOR)
            self.pointTextRect = self.pointText.get_rect(center=(self.anchorX*globals.BLOCK_SIZE + globals.BLOCK_SIZE + self.offset, 20)) 

        def draw(self, surface: pygame.Surface):
            surface.blit(self.pointText, self.pointTextRect)


    def __init__(self):
        self.screen     = pygame.display.set_mode(globals.SCREEN_SIZE)
        self.clock      = pygame.time.Clock()
        
        self.entities   = pygame.sprite.Group()
        self.enemies    = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()

        self.levelConfig  = Engine.loadMap(globals.LEVEL_1)
        self.stateManager = StateManager(state=StateManager.State.RUNNING)

        self.map              = Map(self.levelConfig, globals.BLOCK_SIZE)
        self.display          = Engine.Display(globals.FONT, globals.FONT_SIZE, anchorX=self.map.getRowSize())
        self.questionManager  = QuestionTrial(globals.FONT, globals.FONT_SIZE)
        # harded coded position, it shoud be defined in the level data
        self.player           = Player(position=(10, 9))
        
        self.running    = True
        self.pointsCount = 0

        ### Vars to set the game mechanism
        self.displayQuestion = False

        for enemy in self.levelConfig["enemies"]:
            type = enemy["type"]
            position = enemy["position"]
            match type:
                case Engine.EnemiesMap.PAN.value:
                    self.enemies.add(Pan(position=(position[0], position[1]), target=self.player))
                case Engine.EnemiesMap.JELLY.value:
                    self.enemies.add(Jelly(position=(position[0], position[1]), target=self.player))
        
        self.entities.add(self.player, self.enemies)
        self.allSprites.add(self.map, self.player, self.enemies, self.entities)

    def start(self):
        while self.running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(globals.SCREEN_COLOR)
            self.allSprites.draw(self.screen)
            self.display.draw(self.screen)
            
            match self.stateManager.getState():
                case StateManager.State.RUNNING:
                    self.allSprites.update()
                    self.handleCollisions()
                case StateManager.State.QUESTIONING:
                    self.questionManager.draw(self.screen)
                    self.questionManager.update()
                    completed, correct = self.questionManager.testCompletion()
                    if completed:
                        self.stateManager.setState(StateManager.State.RUNNING)
                        self.player.setIsPowered(True)

            pygame.display.flip()
            self.clock.tick(globals.FPS)
    
    def handleCollisions(self):

        ## In this game there are two type of colission
        ## 1 -> Object Colision that needs to be resolved inside the onCollision() method
        ## 2 -> Engine Colision that is resolved inside the method handleCollisions()
        
        ##
        ## Objects Colisions 
        ##

        collisions = pygame.sprite.groupcollide(self.entities, self.map.tiles, False, False)
        for collision in collisions.items():
            collisionEntityA: IColiable = collision[0]
            collisionEntityB: object = collision[1] if not isinstance(collision[1], list) else collision[1][0]
            
            collisionEntityA.onCollision(collisionEntityB)

        ##
        ## Engine Colisions
        ##

        collisions = pygame.sprite.spritecollide(self.player, self.map.items, True)
        for colision in collisions:
            self.pointsCount += 1
            self.display.updatePointText(self.pointsCount)

            if isinstance(colision, QuestionPoint):
                self.stateManager.setState(StateManager.State.QUESTIONING)
                self.questionManager.setQuestion(colision.getQuestion())

    @staticmethod
    def loadMap(mapFilePath: str):
        with open(mapFilePath, "r", encoding="utf-8") as file:
            return json.load(file)