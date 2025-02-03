import pygame
from enum import Enum
from config import globals
from scenes.Point import Point
from scenes.Tile import Tile


class Map(pygame.sprite.Group):
    class Objects(Enum):
        POINT = 0
        TILE = 1
        SPECIAL = 2

    def __init__(self, mapData: dict[str, dict], blockSize: int = 32):
        super().__init__()
        self.mapData = mapData
        self.blockSize = blockSize
        self.tiles      = pygame.sprite.Group()
        self.enemies    = pygame.sprite.Group()
        self.items      = pygame.sprite.Group() 
        self.buildMap()
        self.add(self.tiles)
        self.add(self.enemies)
        self.add(self.items)

    def buildMap(self) -> list[pygame.sprite.Group]:
        map: list[list[int]] = self.mapData["map"]
        
        for y, row in enumerate(map):
            for x, col in enumerate(row):
                match col:
                    case Map.Objects.POINT.value:
                        self.items.add(Point(x * self.blockSize, y * self.blockSize, self.blockSize // 16, globals.POINT_COLOR))
                    case Map.Objects.SPECIAL.value:
                        self.items.add(Point(x * self.blockSize, y * self.blockSize, self.blockSize // 4, globals.SPECIAL_COLOR))
                    case Map.Objects.TILE.value:
                        self.tiles.add(Tile(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize, globals.BLOCK_COLOR))
               