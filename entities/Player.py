import pygame
from entities.ColiableEntity import ColiableEntity
from utils.helpers import Direction

class Player(ColiableEntity):
    def __init__(self, imagePath: str):
        super().__init__(
            walkRight   =[pygame.transform.smoothscale(pygame.image.load(f"{imagePath}right/{i}.png"), (32, 32)) for i in range(0, 4)],
            walkLeft    =[pygame.transform.smoothscale(pygame.image.load(f"{imagePath}left/{i}.png"), (32, 32)) for i in range(0, 4)],
            walkUp      =[pygame.transform.smoothscale(pygame.image.load(f"{imagePath}up/{i}.png"), (32, 32)) for i in range(0, 4)],
            walkDown    =[pygame.transform.smoothscale(pygame.image.load(f"{imagePath}down/{i}.png"), (32, 32)) for i in range(0, 4)],
        )

    def update(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        return super().update()
    
    def move(self, keys: pygame.key.ScancodeWrapper):
        if keys[pygame.K_LEFT]:
            return super().move(Direction.LEFT)
        elif keys[pygame.K_RIGHT]:
            return super().move(Direction.RIGHT)
        elif keys[pygame.K_UP]:
            return super().move(Direction.UP)
        elif keys[pygame.K_DOWN]:
            return super().move(Direction.DOWN)