import json
import random
import pygame
from typing import List, Dict  
from config import globals
from core.Map import Map
from core.IColiable import IColiable
from core.StateManager import StateManager
from core.QuestionTrial import QuestionTrial
from entities.Player import Player
from entities.enemy.Pan import Pan
from entities.enemy.Jelly import Jelly
from core.input.Event import DirectionInputEvent, PointInputEvent
from core.input.InputHandler import IInputHandler
from scenes.Point import QuestionPoint
from enum import Enum
from collections import deque

class Engine:
    class EnemiesMap(Enum):
        PAN = 0
        JELLY = 1

    class Display:
        def __init__(self, font: str, size: int, anchorX: int):
            self.font = pygame.font.SysFont(font, size)
            self.offset = 20
            self.anchorX = anchorX
            self.updatePointText(0)
            self.updateCountDownText(0)

        def updatePointText(self, number: object) -> None:
            self.pointText = self.font.render(f"Points: {number}", True, globals.TEXT_COLOR)
            self.pointTextRect = self.pointText.get_rect(topleft=(self.getX(), 20))

        def updateCountDownText(self, str_: object) -> None:
            self.countDownText = self.font.render(f"Powered time: {str_}s", True, globals.TEXT_COLOR)
            self.countDownTextRect = self.countDownText.get_rect(topleft=(self.getX(), 45))

        def draw(self, surface: pygame.Surface):
            surface.blit(self.pointText, self.pointTextRect)
            surface.blit(self.countDownText, self.countDownTextRect)

        def getX(self):
            return self.anchorX * globals.BLOCK_SIZE

    def __init__(self, inputHandler: IInputHandler):
        self.screen = pygame.display.set_mode(globals.SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.entities = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()

        self.levelConfig = Engine.loadMap(globals.LEVEL_1)
        self.stateManager = StateManager(state=StateManager.State.RUNNING)

        self.questionManager = QuestionTrial(globals.FONT, globals.FONT_SIZE)

        self.running = True
        self.pointsCount = 0
        self.enemiesQuantity = 0
        self.displayQuestion = False

        self.inputHandler = inputHandler
        self.map = Map(self.levelConfig, blockSize=globals.BLOCK_SIZE)
        
        if globals.TARGET_DEVICE == globals.Platform.ANDROID:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.screenSize = self.screen.get_size()
            self.blockSize = self.screenSize[1] // self.map.getColSize()
        elif globals.TARGET_DEVICE == globals.Platform.PC:
            self.screen = pygame.display.set_mode(globals.SCREEN_SIZE)
            self.screenSize = globals.SCREEN_SIZE
            self.blockSize = self.screenSize[1] // self.map.getColSize()

        self.map.setBlockSize(self.blockSize)
        self.scaleRatio = (self.blockSize * 0.8, self.blockSize * 0.8)
        self.map.buildMap()

        # posição inicial hardcoded
        self.player = Player(position=(8*self.blockSize, 8*self.blockSize), ratio=self.scaleRatio)

        self.display = Engine.Display(globals.FONT, globals.FONT_SIZE, anchorX=self.map.getRowSize())

        self.entities.add(self.player, self.enemies)
        self.allSprites.add(self.map, self.player, self.enemies, self.entities)

        print(f"(+) [Engine Specs] --ScreenSize: {self.screenSize} --BlockSize: {self.blockSize}")
    
    def start(self):
        while self.running:
            gameEventQueue: deque = deque()
            ## this may change --should implement a version of consuming the eventDeque in all states
            inputDirection: DirectionInputEvent = None
            inputPoint: PointInputEvent = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                gameEvent = self.inputHandler.translateEvent(event)
                if gameEvent != None:
                    gameEventQueue.append(gameEvent)

            for gameEvent in gameEventQueue:
                if isinstance(gameEvent, DirectionInputEvent):
                    print("(+) [DirectionInputEvent] Direction: ", gameEvent.cardinalDirection)
                    inputDirection = gameEvent 
                if isinstance(gameEvent, PointInputEvent):
                    print("(+) [PointInputEvent] Position: ", gameEvent.position)
                    inputPoint = gameEvent

            self.screen.fill(globals.SCREEN_COLOR)
            self.allSprites.draw(self.screen)
            self.display.draw(self.screen)

            state = self.stateManager.getState()
            if state == StateManager.State.RUNNING:
                self.allSprites.update()
                self.handleCollisions()
                if self.player.IsPowered():
                    self.display.updateCountDownText(self.player.getRemainingPowerTime())

                if not self.player.isAlive() or self.map.getItemsQuantity() == 0:
                    self.stateManager.setState(StateManager.State.ENDGAME)

                if inputDirection != None:
                    self.player.direction = inputDirection.cardinalDirection

                self.handleEnemies()

            elif state == StateManager.State.QUESTIONING:
                self.questionManager.draw(self.screen)
                completed, correct = self.questionManager.testCompletion()
                if completed:
                    print(f"(+) [Question] Completed: {completed} Correct: {correct}")
                    self.stateManager.setState(StateManager.State.RUNNING)
                    if correct:
                        self.player.setIsPowered(True)
                        self.display.updateCountDownText(self.player.getPowerDuration())
                if inputPoint != None:
                    if globals.TARGET_DEVICE == globals.Platform.ANDROID:
                        print("\t(*) [Detected correction for device] --NormalizedValue: ", inputPoint.position, " --ScreenSize: ", self.screenSize)
                        inputPoint.position = (inputPoint.position[0] * self.screenSize[0], inputPoint.position[1] * self.screenSize[1])
                    self.questionManager.update(inputPoint.position)

            elif state == StateManager.State.ENDGAME:
                self.running = False
                return

            pygame.display.flip()
            self.clock.tick(globals.FPS)

    def getRandomEnemy(self) -> Dict[str, object]:
        entities = self.levelConfig["enemies"]["entities"]
        return entities[random.randint(0, len(entities) - 1)]

    def handleEnemies(self):
        if len(self.enemies) <= self.levelConfig["enemies"]["maxNumber"]:
            if self.levelConfig["enemies"]["respaw"]:
                enemy = self.getRandomEnemy()
                position = enemy["position"]
                self.enemiesQuantity += 1

                if enemy["type"] == Engine.EnemiesMap.PAN.value:
                    self.enemies.add(Pan(ratio=self.scaleRatio, position=(position[0]*self.blockSize, position[1]*self.blockSize), target=self.player, mapData=self.map.getMapData()))
                elif enemy["type"] == Engine.EnemiesMap.JELLY.value:
                    self.enemies.add(Jelly(ratio=self.scaleRatio, position=(position[0]*self.blockSize, position[1]*self.blockSize), target=self.player, mapData=self.map.getMapData()))

                self.entities.add(self.enemies)
                self.allSprites.add(self.enemies)

    def handleCollisions(self):
        # 1.1 One way collision
        collisions: Dict[IColiable, object] = pygame.sprite.groupcollide(self.entities, self.map.tiles, False, False)
        for entityA, entityB in collisions.items():
            collisionEntityA: IColiable = entityA
            collisionEntityB: object = entityB if not isinstance(entityB, list) else entityB[0]
            collisionEntityA.onCollision(collisionEntityB)

        # 1.2 Two way collision
        collisions: List[IColiable] = pygame.sprite.spritecollide(self.player, self.enemies, False)
        for collision in collisions:
            self.player.onCollision(collision)
            collision.onCollision(self.player)

        # Engine Collisions
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
