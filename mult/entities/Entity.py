import pygame
from typing import List, Tuple
from config import globals
from utils.helpers import Direction

class Entity(pygame.sprite.Sprite):

    def __init__(self, walkRight: List[pygame.Surface], walkLeft: List[pygame.Surface], walkUp: List[pygame.Surface], walkDown: List[pygame.Surface], position: Tuple[int, int]):
        super().__init__()

        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.walkUp = walkUp
        self.walkDown = walkDown
        self.image = self.walkLeft[0]
        self.__currentAnimation = self.walkLeft

        self.rect = self.image.get_rect(center=(position[0], position[1]))
        self.direction = Direction.LEFT
        self.speed = 2
        self.frameIndex = 0
        self.animationSpeed = 5
        self.counter = 0 
        self.lastY = self.rect.y
        self.lastX = self.rect.x

    def move(self, direction: Direction):
        self.lastX = self.rect.x
        self.lastY = self.rect.y
        if direction == Direction.RIGHT:
            self.rect.x += self.speed
            self.__currentAnimation = self.walkRight
        elif direction == Direction.LEFT:
            self.rect.x -= self.speed
            self.__currentAnimation = self.walkLeft
        elif direction == Direction.UP:
            self.rect.y -= self.speed
            self.__currentAnimation = self.walkUp
        elif direction == Direction.DOWN:
            self.rect.y += self.speed
            self.__currentAnimation = self.walkDown

    def update(self):
        self.counter += 1
        if self.counter >= self.animationSpeed:
            self.counter = 0
            self.frameIndex = (self.frameIndex + 1) % len(self.__currentAnimation)

        self.image = self.__currentAnimation[self.frameIndex]

    def getCurrentAnimation(self) -> List[pygame.Surface]:
        return self.__currentAnimation
