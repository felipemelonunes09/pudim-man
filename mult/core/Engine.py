
import pygame
import json
from config import globals

class Engine:
    def __init__(self):
        self.screen = pygame.display.set_mode(globals.SCREEN_SIZE)
        self.levelConfig  = Engine.loadMap(globals.LEVEL_1)
        self.clock = pygame.time.Clock()
        
        self.running = True

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((40, 255, 0))
            pygame.display.flip()
    
    @staticmethod
    def loadMap(mapFilePath: str):
        with open(mapFilePath, "r", encoding="utf-8") as file:
            return json.load(file)