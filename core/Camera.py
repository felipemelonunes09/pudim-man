import pygame

class Camera(pygame.sprite.Group): 
    
    def __init__(self) -> None:
        super().__init__()

        self.offset = pygame.math.Vector2()
        self.display_surface = pygame.display.get_surface()

        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def track(self, target):

        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw(self, target = None):

        if target is not None:
            self.track(target)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)