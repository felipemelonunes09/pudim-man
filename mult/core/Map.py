import pygame
from enum import Enum
from typing import Dict, List  
from config import globals
from scenes.Point import Point, QuestionPoint
from scenes.Tile import Tile
from utils.helpers import questionGenerator

class Map(pygame.sprite.Group):
    class Objects(Enum):
        POINT = 0
        TILE = 1
        SPECIAL = 2

    def __init__(self, levelData: Dict[str, Dict], blockSize: int = 32):
        super().__init__()
        self.levelData = levelData
        self.blockSize = blockSize
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group() 
        self.buildMap()
        self.add(self.tiles)
        self.add(self.enemies)
        self.add(self.items)

    def buildMap(self) -> List[pygame.sprite.Group]:
        map_data: List[List[int]] = self.levelData["map"]
        questions = questionGenerator(self.levelData["questions"])

        for y, row in enumerate(map_data):
            for x, col in enumerate(row):
                if col == Map.Objects.POINT.value:
                    self.items.add(Point(
                        x * self.blockSize,
                        y * self.blockSize,
                        self.blockSize // 16,
                        globals.POINT_COLOR
                    ))
                elif col == Map.Objects.SPECIAL.value:
                    self.items.add(QuestionPoint(
                        x=x*self.blockSize, 
                        y=y*self.blockSize, 
                        radius=self.blockSize // 4,
                        color=globals.SPECIAL_COLOR,
                        question=next(questions),
                    ))
                elif col == Map.Objects.TILE.value:
                    self.tiles.add(Tile(
                        x * self.blockSize,
                        y * self.blockSize,
                        self.blockSize,
                        self.blockSize,
                        globals.BLOCK_COLOR
                    ))

    def getItemsQuantity(self) -> int:
        return len(self.items)
    
    def getMapData(self) -> List[List[int]]:
        return self.levelData["map"]
    
    def getRowSize(self) -> int:
        return len(self.levelData["map"][0])
