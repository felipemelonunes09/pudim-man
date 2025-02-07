import pygame
from core.IColiable import IColiable
from core.QuestionDisplay import Question

class Point(pygame.sprite.Sprite, IColiable):
    def __init__(self, x: int, y: int, radius: int, color: tuple[int, int, int]):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA) 
        self.image.fill((0, 0, 0, 0)) 
        pygame.draw.circle(self.image, color, (radius, radius), radius)  
        self.rect = self.image.get_rect(center=(x, y))  

class QuestionPoint(Point):
    def __init__(self, question: Question, *args, **k):
        super().__init__(*args, **k)
        self.__question = question

    def getQuestion(self) -> Question:
        return self.__question