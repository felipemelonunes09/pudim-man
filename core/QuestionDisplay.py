import pygame
from config import globals

class Question():
    def __init__(self, question: str, awnsers: list[str], rightIndex: int):
        self.__question = question
        self.__awnsers = awnsers
        self.__rightIndex = rightIndex

    def getQuestion(self) -> str:
        return self.__question
    
    def getAwnsers(self) -> list[str]:
        return self.__awnsers
    
    def getAwnsersLen(self) -> int:
        return len(self.__awnsers)

    def getAwnser(self, index: int):
        return self.__awnsers[index]


class QuestionDisplay(pygame.sprite.Sprite):
    def __init__(self, font: str, size: int, *groups):
        super().__init__(*groups)
        self.margin = 50
        self.color  = (*globals.SCREEN_COLOR, 230)
        self.image  = pygame.Surface((globals.SCREEN_SIZE[0] - self.margin*2, globals.SCREEN_SIZE[1] - self.margin*2), pygame.SRCALPHA)
        self.font   = pygame.font.SysFont(font, size)
        self.rect   = self.image.get_rect(topleft=(self.margin, self.margin))
        self.__question: Question = None
        self.image.fill(self.color)

    def draw(self, surface: pygame.Surface):
        self.image.blit(self.__questionText, self.__questionTextRect)
        for i in range(self.__question.getAwnsersLen()):
             self.image.blit(self.__awnsersText[i], self.__awnsersTextRect[i])
        surface.blit(self.image, (self.margin, self.margin))

    def setQuestion(self, question: Question) -> None:
        self.__question = question
        self.__updateText()

    def __updateText(self):
        
        self.__questionText = self.font.render(self.__question.getQuestion(), True, globals.TEXT_COLOR)
        self.__questionTextRect = self.__questionText.get_rect(topleft=(self.margin, self.margin))
        self.__awnsersText      = [self.font.render(self.__question.getAwnser(index), True, globals.TEXT_COLOR) for index, awnsers in enumerate(self.__question.getAwnsers()) ]
        self.__awnsersTextRect  = [awnswerText.get_rect(topleft=(self.margin, self.margin*index + self.margin*2)) for index, awnswerText in enumerate(self.__awnsersText)]