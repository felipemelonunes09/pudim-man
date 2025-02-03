import json
import pygame
from config import globals
from core.Map import Map
from core.IColiable import IColiable
from entities.Player import Player

class Engine:
    def __init__(self):
        self.screen     = pygame.display.set_mode(globals.SCREEN_SIZE)
        self.clock      = pygame.time.Clock()
        self.allSprites = pygame.sprite.Group()

        self.map        = Map(Engine.loadMap(globals.LEVEL_1), blockSize=globals.BLOCK_SIZE)
        self.player     = Player(globals.PLAYER_IMAGE_DIR)

        self.running    = True
        self.allSprites.add(self.map)
        self.allSprites.add(self.player)

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
                tile.onCollision(self.player)
                print()

        pygame.sprite.spritecollide(self.player, self.map.items, True)
    

    @staticmethod
    def loadMap(mapFilePath: str):
        with open(mapFilePath, "r") as file:
            return json.load(file)