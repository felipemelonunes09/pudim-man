from entities.enemy.Enemy import Enemy
from config.sprites import Sprites
import pygame

class Pan(Enemy):
    def __init__(self, ratio, *a, **k):
        super().__init__(
            walkRight   = Sprites.Pan.walkRight(ratio),
            walkLeft    = Sprites.Pan.walkLeft(ratio),
            walkUp      = Sprites.Pan.walkRight(ratio),
            walkDown    = Sprites.Pan.walkLeft(ratio),
            *a, 
            **k
        )
