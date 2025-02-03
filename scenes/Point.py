import pygame

class Point(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int, color: tuple[int, int, int]):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Superfície transparente
        self.image.fill((0, 0, 0, 0))  # Garante que o fundo seja totalmente transparente
        pygame.draw.circle(self.image, color, (radius, radius), radius)  # Desenha o círculo
        self.rect = self.image.get_rect(center=(x, y))  # Centraliza a posição
