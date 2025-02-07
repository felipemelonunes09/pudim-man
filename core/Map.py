import pygame
from enum import Enum
from config import globals
from scenes.Point import Point, QuestionPoint
from scenes.Tile import Tile
from utils.helpers import questionGenerator

class Map(pygame.sprite.Group):
    class Objects(Enum):
        POINT = 0
        TILE = 1
        SPECIAL = 2

    def __init__(self, levelData: dict[str, dict], blockSize: int = 32):
        super().__init__()
        self.levelData = levelData
        self.blockSize = blockSize
        self.tiles      = pygame.sprite.Group()
        self.enemies    = pygame.sprite.Group()
        self.items      = pygame.sprite.Group() 
        self.buildMap()
        self.add(self.tiles)
        self.add(self.enemies)
        self.add(self.items)

    def buildMap(self) -> list[pygame.sprite.Group]:
        map: list[list[int]] = self.levelData["map"]
        questions = questionGenerator(self.levelData["questions"])

        for y, row in enumerate(map):
            for x, col in enumerate(row):
                match col:
                    case Map.Objects.POINT.value:
                        self.items.add(Point(x * self.blockSize, y * self.blockSize, self.blockSize // 16, globals.POINT_COLOR))
                    case Map.Objects.SPECIAL.value:
                        self.items.add(QuestionPoint(
                            x=x*self.blockSize, 
                            y=y*self.blockSize, 
                            radius=self.blockSize // 4,
                            color=globals.SPECIAL_COLOR,
                            question=next(questions),
                        ))
                    case Map.Objects.TILE.value:
                        self.tiles.add(Tile(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize, globals.BLOCK_COLOR))

    def getItemsQuantity(self) -> int:
        return len(self.items)
    def getRowSize(self) -> int:
        return len(self.levelData["map"][0])
    