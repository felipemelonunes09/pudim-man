import json
import pygame
from config import globals
from core.Map import Map
from core.IColiable import IColiable
from entities.Player import Player
from entities.enemy.Pan import Pan
from enum import Enum

class Engine:
    class EnemiesMap(Enum):
        PAN     = 0
        JELLY   = 1

    def __init__(self):
        self.screen     = pygame.display.set_mode(globals.SCREEN_SIZE)
        self.clock      = pygame.time.Clock()
        
        self.enemies   =  pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        self.levelConfig = Engine.loadMap(globals.LEVEL_1)

        self.map        = Map(self.levelConfig, globals.BLOCK_SIZE)
        self.player     = Player(position=(1, 1))

        self.running    = True

        for enemy in self.levelConfig["enemies"]:
            type = enemy["type"]
            position = enemy["position"]
            match type:
                case Engine.EnemiesMap.PAN.value:
                    self.enemies.add(Pan(position=(position[0], position[1]), target=self.player))
                case Engine.EnemiesMap.JELLY.value:
                    pass
                    #self.enemies.add(Jelly(globals.JELLY_IMAGE_DIR, (position[0], position[1])))
        
        self.allSprites.add(self.map, self.player, self.enemies)

    def start(self):
        while self.running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(globals.SCREEN_COLOR)
            self.allSprites.update()
            self.allSprites.draw(self.screen)
            self.handleCollisions()
            pygame.display.flip()
            self.clock.tick(globals.FPS)
    
    def handleCollisions(self):
        tilesHited = pygame.sprite.spritecollide(self.player, self.map.tiles, False)
        for tile in tilesHited:
            if isinstance(tile, IColiable):
                self.player.onCollision(tile)

        pygame.sprite.spritecollide(self.player, self.map.items, True)
    

    @staticmethod
    def loadMap(mapFilePath: str):
        with open(mapFilePath, "r") as file:
            return json.load(file)