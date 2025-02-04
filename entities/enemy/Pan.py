from entities.enemy.Enemy import Enemy
from config.sprites import Sprites
import pygame

class Pan(Enemy):
    def __init__(self, *a, **k):
        super().__init__(
            walkRight   = Sprites.Pan.walk,
            walkLeft    = Sprites.Pan.walk,
            walkUp      = Sprites.Pan.walk,
            walkDown    = Sprites.Pan.walk,
            *a, 
            **k
        )
