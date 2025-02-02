import pygame
from enum import Enum
from scenes.Tile import Tile
from config import globals


class Map(pygame.sprite.Group):
    class Objects(Enum):
        POINT = 0
        TILE = 1

    def __init__(self, mapData: dict[str, dict]):
        super().__init__()
        self.mapData = mapData
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
            for x, tile in enumerate(row):
                if Map.Objects.TILE == 1:
                    self.tiles.add(Tile(x * globals.BLOCK_SIZE, y * globals.BLOCK_SIZE, globals.BLOCK_SIZE, globals.BLOCK_SIZE, globals.BLOCK_COLOR))
        return self.tiles