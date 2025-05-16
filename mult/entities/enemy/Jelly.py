from entities.enemy.Enemy import Enemy
from config.sprites import Sprites

class Jelly(Enemy):
    def __init__(self, ratio, *a, **k):
        super().__init__(
            walkRight   = Sprites.Jelly.walkRight(ratio),
            walkLeft    = Sprites.Jelly.walkLeft(ratio),
            walkUp      = Sprites.Jelly.walkRight(ratio),
            walkDown    = Sprites.Jelly.walkRight(ratio),
            *a, 
            **k
        )

    def onCollision(self, entity):
        return super().onCollision(entity)
    
