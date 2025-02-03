import pygame
from entities.Entity import Entity

class Player(Entity):
    def __init__(self, imagePath: str):
        self.image = self.walkLeft[0]
        self.rect = self.image.get_rect()

        super().__init__(
            walkRight   =[pygame.image.load(f"{imagePath}rifht/{i}.png") for i in range(1, 5)],
            walkLeft    =[pygame.image.load(f"{imagePath}left/{i}.png") for i in range(1, 5)],
            walkUp      =[pygame.image.load(f"{imagePath}up/{i}.png") for i in range(1, 5)],
            walkDown    =[pygame.image.load(f"{imagePath}down/{i}.png") for i in range(1, 5)]
        )

    def draw(self):
        pass
