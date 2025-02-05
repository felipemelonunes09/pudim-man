from entities.Entity import Entity
from core.IColiable import IColiable
from scenes.Tile import Tile


class ColiableEntity(Entity, IColiable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def onCollision(self, entity: Entity):
        if isinstance(entity, Tile):
            
            print("actual:")
            print((self.rect.x, self.rect.y))
            print("last")
            print((self.lastX, self.lastY))
            self.rect.x = self.lastX
            self.rect.y = self.lastY

            print("updated")
            print((self.rect.x, self.rect.y))
            
            print("===========================")
        return super().onCollision(entity)