from entities.enemy.Enemy import Enemy
from config.sprites import Sprites
import pygame

class Jelly(Enemy):
    def __init__(self, *a, **k):
        super().__init__(
            walkRight   = Sprites.Jelly.walkRight,
            walkLeft    = Sprites.Jelly.walkLeft,
            walkUp      = Sprites.Jelly.walkRight,
            walkDown    = Sprites.Jelly.walkRight,
            *a, 
            **k
        )
