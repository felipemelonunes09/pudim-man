import pygame
from utils.helpers import Direction

class Entity(pygame.sprite.Sprite):

    def __init__(self, walkRight: list, walkLeft: list, walkUp: list, walkDown: list):
        super().__init__()

        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.walkUp = walkUp
        self.walkDown = walkDown
        self.image = self.walkLeft[0]
        self.__currentAnimation = self.walkLeft

        self.direction = Direction.LEFT
        self.speed = 5
        self.frameIndex = 0
        self.animationSpeed = 5
        self.counter = 0 

    def draw(self):
        pass

    def update(self):
        self.counter += 1
        if self.counter >= self.animationSpeed:
            self.counter = 0
            self.frameIndex += (self.frameIndex + 1) % len(self.walkLeft)
        
        self.image = self.__currentAnimation[self.frameIndex]