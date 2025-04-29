from entities.enemy.Enemy import Enemy
from config.sprites import Sprites
import pygame

class Pan(Enemy):
    def __init__(self, *a, **k):
        super().__init__(
            walkRight   = Sprites.Pan.walkRight,
            walkLeft    = Sprites.Pan.walkLeft,
            walkUp      = Sprites.Pan.walkRight,
            walkDown    = Sprites.Pan.walkLeft,
            *a, 
            **k
        )
